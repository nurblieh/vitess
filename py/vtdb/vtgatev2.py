# Copyright 2013 Google Inc. All Rights Reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

from itertools import izip
import logging
import re

from net import bsonrpc
from net import gorpc
from vtdb import cursor
from vtdb import dbexceptions
from vtdb import field_types


_errno_pattern = re.compile('\(errno (\d+)\)')
# Map specific errors to specific classes.
_errno_map = {
    1062: dbexceptions.IntegrityError,
}


__error_counter_callback = None


def register_error_counter_callback(func):
  global __error_counter_callback
  __error_counter_callback = func


def convert_exception(exc, *args):
  new_args = exc.args + args
  # increment the error counter
  global __error_counter_callback
  if __error_counter_callback is not None:
    __error_counter_callback()

  if isinstance(exc, gorpc.TimeoutError):
    return dbexceptions.TimeoutError(new_args)
  elif isinstance(exc, gorpc.AppError):
    msg = str(exc[0]).lower()
    match = _errno_pattern.search(msg)
    if match:
      mysql_errno = int(match.group(1))
      return _errno_map.get(mysql_errno, dbexceptions.DatabaseError)(new_args)
    return dbexceptions.DatabaseError(new_args)
  elif isinstance(exc, gorpc.ProgrammingError):
    return dbexceptions.ProgrammingError(new_args)
  elif isinstance(exc, gorpc.GoRpcError):
    return dbexceptions.FatalError(new_args)
  return exc


def _create_req_with_keyspace_ids(sql, new_binds, keyspace, tablet_type, keyspace_ids):
  req = {
        'Sql': sql,
        'BindVariables': new_binds,
        'Keyspace': self.keyspace,
        'TabletType': self.tablet_type,
        'KeyspaceIds': keyspace_ids,
        }
  return req


def _create_req_with_keyranges(sql, new_binds, keyspace, tablet_type, keyranges):
  req = {
        'Sql': sql,
        'BindVariables': new_binds,
        'Keyspace': self.keyspace,
        'TabletType': self.tablet_type,
        'KeyRanges': keyranges,
        }
  return req


# A simple, direct connection to the vttablet query server.
# This is shard-unaware and only handles the most basic communication.
# If something goes wrong, this object should be thrown away and a new one instantiated.
class VtgateConnection(object):
  session = None
  tablet_type = None
  cursorclass = cursor.TabletCursor
  _stream_fields = None
  _stream_conversions = None
  _stream_result = None
  _stream_result_index = None

  def __init__(self, addr, timeout, user=None, password=None, encrypted=False, keyfile=None, certfile=None):
    self.addr = addr
    self.timeout = timeout
    self.client = bsonrpc.BsonRpcClient(addr, timeout, user, password, encrypted=encrypted, keyfile=keyfile, certfile=certfile)

  def __str__(self):
    return '<VtgateConnection %s >' % self.addr

  def dial(self):
    try:
      if not self.is_closed():
        self.close()
      self.client.dial()
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self))

  def close(self):
    if self.session:
      self.rollback()
    self.client.close()

  def is_closed(self):
    return self.client.is_closed()

  def begin(self):
    try:
      response = self.client.call('VTGate.Begin', None)
      self.session = response.reply
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self))

  def commit(self):
    try:
      session = self.session
      self.session = None
      self.client.call('VTGate.Commit', session)
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self))

  def rollback(self):
    try:
      session = self.session
      self.session = None
      self.client.call('VTGate.Rollback', session)
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self))

  def cursor(self, cursorclass=None, **kargs):
    if cursorclass is not None:
      # cursorclass can only be overwritten by a compatible cursor
      if cursorclass != cursor.StreamCursor:
        raise DatabaseException('invalid cursor type for VtgateConnection',
                                cursorclass)
      return cursorclass(self, **kargs)
    return self.cursorclass(self, **kargs)

  def _add_session(self, req):
    if self.session:
      req['Session'] = self.session

  def _update_session(self, response):
    if 'Session' in response.reply:
      self.session = response.reply['Session']

  def _execute(self, sql, bind_variables, keyspace, tablet_type, keyspace_ids=None, keyranges=None):
    new_binds = field_types.convert_bind_vars(bind_variables)
    exec_method = None
    req = None
    if keyspace_ids is not None:
      req = self._create_req_with_keyspace_ids(sql, new_binds, keyspace, tablet_type, keyspace_ids)
      exec_method = 'VTGate.ExecuteKeyspaceIds'
    elif keyrange is not None:
      req = self._create_req_with_keyranges(sql, new_binds, keyspace, tablet_type, keyranges)
      exec_method = 'VTGate.ExecuteKeyRanges'
    else:
      raise dbexceptions.ProgrammingError('_execute called without specifying keyspace_ids or keyranges')


    self._add_session(req)

    fields = []
    conversions = []
    results = []
    try:
      response = self.client.call(exec_method, req)
      self._update_session(response)
      reply = response.reply
      if 'Error' in response.reply:
        raise gorpc.AppError(response.reply['Error'], exec_method)

      for field in reply['Fields']:
        fields.append((field['Name'], field['Type']))
        conversions.append(field_types.conversions.get(field['Type']))

      for row in reply['Rows']:
        results.append(tuple(_make_row(row, conversions)))

      rowcount = reply['RowsAffected']
      lastrowid = reply['InsertId']
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self), sql, bind_variables)
    except:
      logging.exception('gorpc low-level error')
      raise
    return results, rowcount, lastrowid, fields

  def _execute_entity_ids(self, sql, bind_variables, keyspace, tablet_type, entity_keyspace_id_map, entity_column_name):
    new_binds = field_types.convert_bind_vars(bind_variables)
    req = {
        'Sql': sql,
        'BindVariables': new_binds,
        'Keyspace': self.keyspace,
        'TabletType': self.tablet_type,
        'EntityKeyspaceIdMap': entity_keyspace_id_map,
        'EntityColumnName': entity_column_name,
        }

    self._add_session(req)

    fields = []
    conversions = []
    results = []
    try:
      response = self.client.call('VTGate.ExecuteEntityIds', req)
      self._update_session(response)
      reply = response.reply
      if 'Error' in response.reply:
        raise gorpc.AppError(response.reply['Error'], 'VTGate.ExecuteEntityIds')

      for field in reply['Fields']:
        fields.append((field['Name'], field['Type']))
        conversions.append(field_types.conversions.get(field['Type']))

      for row in reply['Rows']:
        results.append(tuple(_make_row(row, conversions)))

      rowcount = reply['RowsAffected']
      lastrowid = reply['InsertId']
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self), sql, bind_variables)
    except:
      logging.exception('gorpc low-level error')
      raise
    return results, rowcount, lastrowid, fields


  def _execute_batch(self, sql_list, bind_variables_list, keyspace, tablet_type, keyspace_ids):
    query_list = []
    for sql, bind_vars in zip(sql_list, bind_variables_list):
      query = {}
      query['Sql'] = sql
      query['BindVariables'] = field_types.convert_bind_vars(bind_vars)
      query_list.append(query)

    rowsets = []

    try:
      req = {
          'Queries': query_list,
          'Keyspace': keyspace,
          'TabletType': tablet_type,
          'KeyspaceIds': keyspace_ids,
      }
      self._add_session(req)
      response = self.client.call('VTGate.ExecuteBatchKeyspaceIds', req)
      self._update_session(response)
      if 'Error' in response.reply:
        raise gorpc.AppError(response.reply['Error'], 'VTGate.ExecuteBatchKeyspaceIds')
      for reply in response.reply['List']:
        fields = []
        conversions = []
        results = []
        rowcount = 0

        for field in reply['Fields']:
          fields.append((field['Name'], field['Type']))
          conversions.append(field_types.conversions.get(field['Type']))

        for row in reply['Rows']:
          results.append(tuple(_make_row(row, conversions)))

        rowcount = reply['RowsAffected']
        lastrowid = reply['InsertId']
        rowsets.append((results, rowcount, lastrowid, fields))
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self), sql_list, bind_variables_list)
    except:
      logging.exception('gorpc low-level error')
      raise
    return rowsets

  # we return the fields for the response, and the column conversions
  # the conversions will need to be passed back to _stream_next
  # (that way we avoid using a member variable here for such a corner case)
  def _stream_execute(self, sql, bind_variables, keyspace, tablet_type, keyspace_ids=None, keyranges=None):
    new_binds = field_types.convert_bind_vars(bind_variables)
    exec_method = None
    req = None
    if keyspace_ids is not None:
      req = self._create_req_with_keyspace_ids(sql, new_binds, keyspace, tablet_type, keyspace_ids)
      exec_method = 'VTGate.StreamExecuteKeyspaceIds'
    elif keyrange is not None:
      req = self._create_req_with_keyranges(sql, new_binds, keyspace, tablet_type, keyranges)
      exec_method = 'VTGate.StreamExecuteKeyRanges'
    else:
      raise dbexceptions.ProgrammingError('_execute called without specifying keyspace_ids or keyranges')

    self._add_session(req)

    self._stream_fields = []
    self._stream_conversions = []
    self._stream_result = None
    self._stream_result_index = 0
    try:
      self.client.stream_call(exec_method, req)
      first_response = self.client.stream_next()
      reply = first_response.reply

      for field in reply['Fields']:
        self._stream_fields.append((field['Name'], field['Type']))
        self._stream_conversions.append(field_types.conversions.get(field['Type']))
    except gorpc.GoRpcError as e:
      raise convert_exception(e, str(self), sql, bind_variables)
    except:
      logging.exception('gorpc low-level error')
      raise
    return None, 0, 0, self._stream_fields

  def _stream_next(self):
    # Terminating condition
    if self._stream_result_index is None:
      return None

    # See if we need to read more or whether we just pop the next row.
    while self._stream_result is None:
      try:
        self._stream_result = self.client.stream_next()
        if self._stream_result is None:
          self._stream_result_index = None
          return None
        # A session message, if any comes separately with no rows
        if 'Session' in self._stream_result.reply:
          self.session = self._stream_result.reply['Session']
          self._stream_result = None
          continue
      except gorpc.GoRpcError as e:
        raise convert_exception(e, str(self))
      except:
        logging.exception('gorpc low-level error')
        raise

    row = tuple(_make_row(self._stream_result.reply['Rows'][self._stream_result_index], self._stream_conversions))

    # If we are reading the last row, set us up to read more data.
    self._stream_result_index += 1
    if self._stream_result_index == len(self._stream_result.reply['Rows']):
      self._stream_result = None
      self._stream_result_index = 0

    return row


def _make_row(row, conversions):
  converted_row = []
  for conversion_func, field_data in izip(conversions, row):
    if field_data is None:
      v = None
    elif conversion_func:
      v = conversion_func(field_data)
    else:
      v = field_data
    converted_row.append(v)
  return converted_row


def get_params_for_vtgate_conn(vtgate_addrs, timeout, encrypted=False, user=None, password=None):
  db_params_list = []
  addrs = []
  if isinstance(vtgate_addrs, dict):
    service = '_vt'
    if encrypted:
      service = '_vts'
    if service not in vtgate_addrs:
      raise Exception("required vtgate service addrs %s not exist" % service)
    addrs = vtgate_addrs[service]
    random.shuffle(addrs)
  elif isinstance(vtgate_addrs, list):
    random.shuffle(vtgate_addrs)
    addrs = vtgate_addrs
  else:
    raise dbexceptions.Error("Wrong type for vtgate addrs %s" % vtgate_addrs)

  for addr in vtgate_addrs:
    vt_params = dict()
    vt_params['addr'] = addr
    vt_params['timeout'] = timeout
    vt_params['encrypted'] = encrypted
    vt_params['user'] = user
    vt_params['password'] = password
    db_params_list.append(vt_params)
  return db_params_list


def connect(vtgate_addrs, timeout, encrypted=False, user=None, password=None):
  db_params = get_params_for_vtgate_conn(vtgate_addrs, timeout,
                                         encrypted=encrypted, user=user,
                                         password=password)

  if not db_params_list:
   raise dbexceptions.OperationalError("empty db params list - no db instance available for vtgate_addrs %s" % vtgate_addrs)

  db_exception = None
  host_addr = None
  for params in db_params_list:
    try:
      db_params = params.copy()
      host_addr = db_params['addr']
      conn = VtgateConnection(**db_params)
      conn.dial()
      return conn
    except Exception as e:
      db_exception = e
      logging.warning('db connection failed: %s, %s', host_addr, e)

  raise dbexceptions.OperationalError(
    'unable to create vt connection', host_addr, db_exception)