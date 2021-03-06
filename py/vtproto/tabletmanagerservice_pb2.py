# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tabletmanagerservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import tabletmanagerdata_pb2 as tabletmanagerdata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tabletmanagerservice.proto',
  package='tabletmanagerservice',
  syntax='proto3',
  serialized_pb=_b('\n\x1atabletmanagerservice.proto\x12\x14tabletmanagerservice\x1a\x17tabletmanagerdata.proto2\x83 \n\rTabletManager\x12I\n\x04Ping\x12\x1e.tabletmanagerdata.PingRequest\x1a\x1f.tabletmanagerdata.PingResponse\"\x00\x12L\n\x05Sleep\x12\x1f.tabletmanagerdata.SleepRequest\x1a .tabletmanagerdata.SleepResponse\"\x00\x12^\n\x0b\x45xecuteHook\x12%.tabletmanagerdata.ExecuteHookRequest\x1a&.tabletmanagerdata.ExecuteHookResponse\"\x00\x12X\n\tGetSchema\x12#.tabletmanagerdata.GetSchemaRequest\x1a$.tabletmanagerdata.GetSchemaResponse\"\x00\x12g\n\x0eGetPermissions\x12(.tabletmanagerdata.GetPermissionsRequest\x1a).tabletmanagerdata.GetPermissionsResponse\"\x00\x12^\n\x0bSetReadOnly\x12%.tabletmanagerdata.SetReadOnlyRequest\x1a&.tabletmanagerdata.SetReadOnlyResponse\"\x00\x12\x61\n\x0cSetReadWrite\x12&.tabletmanagerdata.SetReadWriteRequest\x1a\'.tabletmanagerdata.SetReadWriteResponse\"\x00\x12[\n\nChangeType\x12$.tabletmanagerdata.ChangeTypeRequest\x1a%.tabletmanagerdata.ChangeTypeResponse\"\x00\x12L\n\x05Scrap\x12\x1f.tabletmanagerdata.ScrapRequest\x1a .tabletmanagerdata.ScrapResponse\"\x00\x12\x61\n\x0cRefreshState\x12&.tabletmanagerdata.RefreshStateRequest\x1a\'.tabletmanagerdata.RefreshStateResponse\"\x00\x12g\n\x0eRunHealthCheck\x12(.tabletmanagerdata.RunHealthCheckRequest\x1a).tabletmanagerdata.RunHealthCheckResponse\"\x00\x12\x61\n\x0cReloadSchema\x12&.tabletmanagerdata.ReloadSchemaRequest\x1a\'.tabletmanagerdata.ReloadSchemaResponse\"\x00\x12j\n\x0fPreflightSchema\x12).tabletmanagerdata.PreflightSchemaRequest\x1a*.tabletmanagerdata.PreflightSchemaResponse\"\x00\x12^\n\x0b\x41pplySchema\x12%.tabletmanagerdata.ApplySchemaRequest\x1a&.tabletmanagerdata.ApplySchemaResponse\"\x00\x12p\n\x11\x45xecuteFetchAsDba\x12+.tabletmanagerdata.ExecuteFetchAsDbaRequest\x1a,.tabletmanagerdata.ExecuteFetchAsDbaResponse\"\x00\x12p\n\x11\x45xecuteFetchAsApp\x12+.tabletmanagerdata.ExecuteFetchAsAppRequest\x1a,.tabletmanagerdata.ExecuteFetchAsAppResponse\"\x00\x12^\n\x0bSlaveStatus\x12%.tabletmanagerdata.SlaveStatusRequest\x1a&.tabletmanagerdata.SlaveStatusResponse\"\x00\x12g\n\x0eMasterPosition\x12(.tabletmanagerdata.MasterPositionRequest\x1a).tabletmanagerdata.MasterPositionResponse\"\x00\x12X\n\tStopSlave\x12#.tabletmanagerdata.StopSlaveRequest\x1a$.tabletmanagerdata.StopSlaveResponse\"\x00\x12m\n\x10StopSlaveMinimum\x12*.tabletmanagerdata.StopSlaveMinimumRequest\x1a+.tabletmanagerdata.StopSlaveMinimumResponse\"\x00\x12[\n\nStartSlave\x12$.tabletmanagerdata.StartSlaveRequest\x1a%.tabletmanagerdata.StartSlaveResponse\"\x00\x12\x8b\x01\n\x1aTabletExternallyReparented\x12\x34.tabletmanagerdata.TabletExternallyReparentedRequest\x1a\x35.tabletmanagerdata.TabletExternallyReparentedResponse\"\x00\x12\x82\x01\n\x17TabletExternallyElected\x12\x31.tabletmanagerdata.TabletExternallyElectedRequest\x1a\x32.tabletmanagerdata.TabletExternallyElectedResponse\"\x00\x12X\n\tGetSlaves\x12#.tabletmanagerdata.GetSlavesRequest\x1a$.tabletmanagerdata.GetSlavesResponse\"\x00\x12j\n\x0fWaitBlpPosition\x12).tabletmanagerdata.WaitBlpPositionRequest\x1a*.tabletmanagerdata.WaitBlpPositionResponse\"\x00\x12R\n\x07StopBlp\x12!.tabletmanagerdata.StopBlpRequest\x1a\".tabletmanagerdata.StopBlpResponse\"\x00\x12U\n\x08StartBlp\x12\".tabletmanagerdata.StartBlpRequest\x1a#.tabletmanagerdata.StartBlpResponse\"\x00\x12^\n\x0bRunBlpUntil\x12%.tabletmanagerdata.RunBlpUntilRequest\x1a&.tabletmanagerdata.RunBlpUntilResponse\"\x00\x12m\n\x10ResetReplication\x12*.tabletmanagerdata.ResetReplicationRequest\x1a+.tabletmanagerdata.ResetReplicationResponse\"\x00\x12[\n\nInitMaster\x12$.tabletmanagerdata.InitMasterRequest\x1a%.tabletmanagerdata.InitMasterResponse\"\x00\x12\x82\x01\n\x17PopulateReparentJournal\x12\x31.tabletmanagerdata.PopulateReparentJournalRequest\x1a\x32.tabletmanagerdata.PopulateReparentJournalResponse\"\x00\x12X\n\tInitSlave\x12#.tabletmanagerdata.InitSlaveRequest\x1a$.tabletmanagerdata.InitSlaveResponse\"\x00\x12\x61\n\x0c\x44\x65moteMaster\x12&.tabletmanagerdata.DemoteMasterRequest\x1a\'.tabletmanagerdata.DemoteMasterResponse\"\x00\x12\x85\x01\n\x18PromoteSlaveWhenCaughtUp\x12\x32.tabletmanagerdata.PromoteSlaveWhenCaughtUpRequest\x1a\x33.tabletmanagerdata.PromoteSlaveWhenCaughtUpResponse\"\x00\x12m\n\x10SlaveWasPromoted\x12*.tabletmanagerdata.SlaveWasPromotedRequest\x1a+.tabletmanagerdata.SlaveWasPromotedResponse\"\x00\x12X\n\tSetMaster\x12#.tabletmanagerdata.SetMasterRequest\x1a$.tabletmanagerdata.SetMasterResponse\"\x00\x12p\n\x11SlaveWasRestarted\x12+.tabletmanagerdata.SlaveWasRestartedRequest\x1a,.tabletmanagerdata.SlaveWasRestartedResponse\"\x00\x12\x8e\x01\n\x1bStopReplicationAndGetStatus\x12\x35.tabletmanagerdata.StopReplicationAndGetStatusRequest\x1a\x36.tabletmanagerdata.StopReplicationAndGetStatusResponse\"\x00\x12\x61\n\x0cPromoteSlave\x12&.tabletmanagerdata.PromoteSlaveRequest\x1a\'.tabletmanagerdata.PromoteSlaveResponse\"\x00\x12Q\n\x06\x42\x61\x63kup\x12 .tabletmanagerdata.BackupRequest\x1a!.tabletmanagerdata.BackupResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[tabletmanagerdata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
class EarlyAdopterTabletManagerServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Sleep(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ExecuteHook(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetSchema(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetPermissions(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetReadOnly(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetReadWrite(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ChangeType(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Scrap(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RefreshState(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RunHealthCheck(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ReloadSchema(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PreflightSchema(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ApplySchema(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ExecuteFetchAsDba(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ExecuteFetchAsApp(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SlaveStatus(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def MasterPosition(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StopSlave(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StopSlaveMinimum(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StartSlave(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def TabletExternallyReparented(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def TabletExternallyElected(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetSlaves(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def WaitBlpPosition(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StopBlp(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StartBlp(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RunBlpUntil(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def ResetReplication(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InitMaster(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PopulateReparentJournal(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InitSlave(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DemoteMaster(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PromoteSlaveWhenCaughtUp(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SlaveWasPromoted(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetMaster(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SlaveWasRestarted(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StopReplicationAndGetStatus(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PromoteSlave(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Backup(self, request, context):
    raise NotImplementedError()
class EarlyAdopterTabletManagerServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterTabletManagerStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request):
    raise NotImplementedError()
  Ping.async = None
  @abc.abstractmethod
  def Sleep(self, request):
    raise NotImplementedError()
  Sleep.async = None
  @abc.abstractmethod
  def ExecuteHook(self, request):
    raise NotImplementedError()
  ExecuteHook.async = None
  @abc.abstractmethod
  def GetSchema(self, request):
    raise NotImplementedError()
  GetSchema.async = None
  @abc.abstractmethod
  def GetPermissions(self, request):
    raise NotImplementedError()
  GetPermissions.async = None
  @abc.abstractmethod
  def SetReadOnly(self, request):
    raise NotImplementedError()
  SetReadOnly.async = None
  @abc.abstractmethod
  def SetReadWrite(self, request):
    raise NotImplementedError()
  SetReadWrite.async = None
  @abc.abstractmethod
  def ChangeType(self, request):
    raise NotImplementedError()
  ChangeType.async = None
  @abc.abstractmethod
  def Scrap(self, request):
    raise NotImplementedError()
  Scrap.async = None
  @abc.abstractmethod
  def RefreshState(self, request):
    raise NotImplementedError()
  RefreshState.async = None
  @abc.abstractmethod
  def RunHealthCheck(self, request):
    raise NotImplementedError()
  RunHealthCheck.async = None
  @abc.abstractmethod
  def ReloadSchema(self, request):
    raise NotImplementedError()
  ReloadSchema.async = None
  @abc.abstractmethod
  def PreflightSchema(self, request):
    raise NotImplementedError()
  PreflightSchema.async = None
  @abc.abstractmethod
  def ApplySchema(self, request):
    raise NotImplementedError()
  ApplySchema.async = None
  @abc.abstractmethod
  def ExecuteFetchAsDba(self, request):
    raise NotImplementedError()
  ExecuteFetchAsDba.async = None
  @abc.abstractmethod
  def ExecuteFetchAsApp(self, request):
    raise NotImplementedError()
  ExecuteFetchAsApp.async = None
  @abc.abstractmethod
  def SlaveStatus(self, request):
    raise NotImplementedError()
  SlaveStatus.async = None
  @abc.abstractmethod
  def MasterPosition(self, request):
    raise NotImplementedError()
  MasterPosition.async = None
  @abc.abstractmethod
  def StopSlave(self, request):
    raise NotImplementedError()
  StopSlave.async = None
  @abc.abstractmethod
  def StopSlaveMinimum(self, request):
    raise NotImplementedError()
  StopSlaveMinimum.async = None
  @abc.abstractmethod
  def StartSlave(self, request):
    raise NotImplementedError()
  StartSlave.async = None
  @abc.abstractmethod
  def TabletExternallyReparented(self, request):
    raise NotImplementedError()
  TabletExternallyReparented.async = None
  @abc.abstractmethod
  def TabletExternallyElected(self, request):
    raise NotImplementedError()
  TabletExternallyElected.async = None
  @abc.abstractmethod
  def GetSlaves(self, request):
    raise NotImplementedError()
  GetSlaves.async = None
  @abc.abstractmethod
  def WaitBlpPosition(self, request):
    raise NotImplementedError()
  WaitBlpPosition.async = None
  @abc.abstractmethod
  def StopBlp(self, request):
    raise NotImplementedError()
  StopBlp.async = None
  @abc.abstractmethod
  def StartBlp(self, request):
    raise NotImplementedError()
  StartBlp.async = None
  @abc.abstractmethod
  def RunBlpUntil(self, request):
    raise NotImplementedError()
  RunBlpUntil.async = None
  @abc.abstractmethod
  def ResetReplication(self, request):
    raise NotImplementedError()
  ResetReplication.async = None
  @abc.abstractmethod
  def InitMaster(self, request):
    raise NotImplementedError()
  InitMaster.async = None
  @abc.abstractmethod
  def PopulateReparentJournal(self, request):
    raise NotImplementedError()
  PopulateReparentJournal.async = None
  @abc.abstractmethod
  def InitSlave(self, request):
    raise NotImplementedError()
  InitSlave.async = None
  @abc.abstractmethod
  def DemoteMaster(self, request):
    raise NotImplementedError()
  DemoteMaster.async = None
  @abc.abstractmethod
  def PromoteSlaveWhenCaughtUp(self, request):
    raise NotImplementedError()
  PromoteSlaveWhenCaughtUp.async = None
  @abc.abstractmethod
  def SlaveWasPromoted(self, request):
    raise NotImplementedError()
  SlaveWasPromoted.async = None
  @abc.abstractmethod
  def SetMaster(self, request):
    raise NotImplementedError()
  SetMaster.async = None
  @abc.abstractmethod
  def SlaveWasRestarted(self, request):
    raise NotImplementedError()
  SlaveWasRestarted.async = None
  @abc.abstractmethod
  def StopReplicationAndGetStatus(self, request):
    raise NotImplementedError()
  StopReplicationAndGetStatus.async = None
  @abc.abstractmethod
  def PromoteSlave(self, request):
    raise NotImplementedError()
  PromoteSlave.async = None
  @abc.abstractmethod
  def Backup(self, request):
    raise NotImplementedError()
  Backup.async = None
def early_adopter_create_TabletManager_server(servicer, port, private_key=None, certificate_chain=None):
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  method_service_descriptions = {
    "ApplySchema": utilities.unary_unary_service_description(
      servicer.ApplySchema,
      tabletmanagerdata_pb2.ApplySchemaRequest.FromString,
      tabletmanagerdata_pb2.ApplySchemaResponse.SerializeToString,
    ),
    "Backup": utilities.unary_stream_service_description(
      servicer.Backup,
      tabletmanagerdata_pb2.BackupRequest.FromString,
      tabletmanagerdata_pb2.BackupResponse.SerializeToString,
    ),
    "ChangeType": utilities.unary_unary_service_description(
      servicer.ChangeType,
      tabletmanagerdata_pb2.ChangeTypeRequest.FromString,
      tabletmanagerdata_pb2.ChangeTypeResponse.SerializeToString,
    ),
    "DemoteMaster": utilities.unary_unary_service_description(
      servicer.DemoteMaster,
      tabletmanagerdata_pb2.DemoteMasterRequest.FromString,
      tabletmanagerdata_pb2.DemoteMasterResponse.SerializeToString,
    ),
    "ExecuteFetchAsApp": utilities.unary_unary_service_description(
      servicer.ExecuteFetchAsApp,
      tabletmanagerdata_pb2.ExecuteFetchAsAppRequest.FromString,
      tabletmanagerdata_pb2.ExecuteFetchAsAppResponse.SerializeToString,
    ),
    "ExecuteFetchAsDba": utilities.unary_unary_service_description(
      servicer.ExecuteFetchAsDba,
      tabletmanagerdata_pb2.ExecuteFetchAsDbaRequest.FromString,
      tabletmanagerdata_pb2.ExecuteFetchAsDbaResponse.SerializeToString,
    ),
    "ExecuteHook": utilities.unary_unary_service_description(
      servicer.ExecuteHook,
      tabletmanagerdata_pb2.ExecuteHookRequest.FromString,
      tabletmanagerdata_pb2.ExecuteHookResponse.SerializeToString,
    ),
    "GetPermissions": utilities.unary_unary_service_description(
      servicer.GetPermissions,
      tabletmanagerdata_pb2.GetPermissionsRequest.FromString,
      tabletmanagerdata_pb2.GetPermissionsResponse.SerializeToString,
    ),
    "GetSchema": utilities.unary_unary_service_description(
      servicer.GetSchema,
      tabletmanagerdata_pb2.GetSchemaRequest.FromString,
      tabletmanagerdata_pb2.GetSchemaResponse.SerializeToString,
    ),
    "GetSlaves": utilities.unary_unary_service_description(
      servicer.GetSlaves,
      tabletmanagerdata_pb2.GetSlavesRequest.FromString,
      tabletmanagerdata_pb2.GetSlavesResponse.SerializeToString,
    ),
    "InitMaster": utilities.unary_unary_service_description(
      servicer.InitMaster,
      tabletmanagerdata_pb2.InitMasterRequest.FromString,
      tabletmanagerdata_pb2.InitMasterResponse.SerializeToString,
    ),
    "InitSlave": utilities.unary_unary_service_description(
      servicer.InitSlave,
      tabletmanagerdata_pb2.InitSlaveRequest.FromString,
      tabletmanagerdata_pb2.InitSlaveResponse.SerializeToString,
    ),
    "MasterPosition": utilities.unary_unary_service_description(
      servicer.MasterPosition,
      tabletmanagerdata_pb2.MasterPositionRequest.FromString,
      tabletmanagerdata_pb2.MasterPositionResponse.SerializeToString,
    ),
    "Ping": utilities.unary_unary_service_description(
      servicer.Ping,
      tabletmanagerdata_pb2.PingRequest.FromString,
      tabletmanagerdata_pb2.PingResponse.SerializeToString,
    ),
    "PopulateReparentJournal": utilities.unary_unary_service_description(
      servicer.PopulateReparentJournal,
      tabletmanagerdata_pb2.PopulateReparentJournalRequest.FromString,
      tabletmanagerdata_pb2.PopulateReparentJournalResponse.SerializeToString,
    ),
    "PreflightSchema": utilities.unary_unary_service_description(
      servicer.PreflightSchema,
      tabletmanagerdata_pb2.PreflightSchemaRequest.FromString,
      tabletmanagerdata_pb2.PreflightSchemaResponse.SerializeToString,
    ),
    "PromoteSlave": utilities.unary_unary_service_description(
      servicer.PromoteSlave,
      tabletmanagerdata_pb2.PromoteSlaveRequest.FromString,
      tabletmanagerdata_pb2.PromoteSlaveResponse.SerializeToString,
    ),
    "PromoteSlaveWhenCaughtUp": utilities.unary_unary_service_description(
      servicer.PromoteSlaveWhenCaughtUp,
      tabletmanagerdata_pb2.PromoteSlaveWhenCaughtUpRequest.FromString,
      tabletmanagerdata_pb2.PromoteSlaveWhenCaughtUpResponse.SerializeToString,
    ),
    "RefreshState": utilities.unary_unary_service_description(
      servicer.RefreshState,
      tabletmanagerdata_pb2.RefreshStateRequest.FromString,
      tabletmanagerdata_pb2.RefreshStateResponse.SerializeToString,
    ),
    "ReloadSchema": utilities.unary_unary_service_description(
      servicer.ReloadSchema,
      tabletmanagerdata_pb2.ReloadSchemaRequest.FromString,
      tabletmanagerdata_pb2.ReloadSchemaResponse.SerializeToString,
    ),
    "ResetReplication": utilities.unary_unary_service_description(
      servicer.ResetReplication,
      tabletmanagerdata_pb2.ResetReplicationRequest.FromString,
      tabletmanagerdata_pb2.ResetReplicationResponse.SerializeToString,
    ),
    "RunBlpUntil": utilities.unary_unary_service_description(
      servicer.RunBlpUntil,
      tabletmanagerdata_pb2.RunBlpUntilRequest.FromString,
      tabletmanagerdata_pb2.RunBlpUntilResponse.SerializeToString,
    ),
    "RunHealthCheck": utilities.unary_unary_service_description(
      servicer.RunHealthCheck,
      tabletmanagerdata_pb2.RunHealthCheckRequest.FromString,
      tabletmanagerdata_pb2.RunHealthCheckResponse.SerializeToString,
    ),
    "Scrap": utilities.unary_unary_service_description(
      servicer.Scrap,
      tabletmanagerdata_pb2.ScrapRequest.FromString,
      tabletmanagerdata_pb2.ScrapResponse.SerializeToString,
    ),
    "SetMaster": utilities.unary_unary_service_description(
      servicer.SetMaster,
      tabletmanagerdata_pb2.SetMasterRequest.FromString,
      tabletmanagerdata_pb2.SetMasterResponse.SerializeToString,
    ),
    "SetReadOnly": utilities.unary_unary_service_description(
      servicer.SetReadOnly,
      tabletmanagerdata_pb2.SetReadOnlyRequest.FromString,
      tabletmanagerdata_pb2.SetReadOnlyResponse.SerializeToString,
    ),
    "SetReadWrite": utilities.unary_unary_service_description(
      servicer.SetReadWrite,
      tabletmanagerdata_pb2.SetReadWriteRequest.FromString,
      tabletmanagerdata_pb2.SetReadWriteResponse.SerializeToString,
    ),
    "SlaveStatus": utilities.unary_unary_service_description(
      servicer.SlaveStatus,
      tabletmanagerdata_pb2.SlaveStatusRequest.FromString,
      tabletmanagerdata_pb2.SlaveStatusResponse.SerializeToString,
    ),
    "SlaveWasPromoted": utilities.unary_unary_service_description(
      servicer.SlaveWasPromoted,
      tabletmanagerdata_pb2.SlaveWasPromotedRequest.FromString,
      tabletmanagerdata_pb2.SlaveWasPromotedResponse.SerializeToString,
    ),
    "SlaveWasRestarted": utilities.unary_unary_service_description(
      servicer.SlaveWasRestarted,
      tabletmanagerdata_pb2.SlaveWasRestartedRequest.FromString,
      tabletmanagerdata_pb2.SlaveWasRestartedResponse.SerializeToString,
    ),
    "Sleep": utilities.unary_unary_service_description(
      servicer.Sleep,
      tabletmanagerdata_pb2.SleepRequest.FromString,
      tabletmanagerdata_pb2.SleepResponse.SerializeToString,
    ),
    "StartBlp": utilities.unary_unary_service_description(
      servicer.StartBlp,
      tabletmanagerdata_pb2.StartBlpRequest.FromString,
      tabletmanagerdata_pb2.StartBlpResponse.SerializeToString,
    ),
    "StartSlave": utilities.unary_unary_service_description(
      servicer.StartSlave,
      tabletmanagerdata_pb2.StartSlaveRequest.FromString,
      tabletmanagerdata_pb2.StartSlaveResponse.SerializeToString,
    ),
    "StopBlp": utilities.unary_unary_service_description(
      servicer.StopBlp,
      tabletmanagerdata_pb2.StopBlpRequest.FromString,
      tabletmanagerdata_pb2.StopBlpResponse.SerializeToString,
    ),
    "StopReplicationAndGetStatus": utilities.unary_unary_service_description(
      servicer.StopReplicationAndGetStatus,
      tabletmanagerdata_pb2.StopReplicationAndGetStatusRequest.FromString,
      tabletmanagerdata_pb2.StopReplicationAndGetStatusResponse.SerializeToString,
    ),
    "StopSlave": utilities.unary_unary_service_description(
      servicer.StopSlave,
      tabletmanagerdata_pb2.StopSlaveRequest.FromString,
      tabletmanagerdata_pb2.StopSlaveResponse.SerializeToString,
    ),
    "StopSlaveMinimum": utilities.unary_unary_service_description(
      servicer.StopSlaveMinimum,
      tabletmanagerdata_pb2.StopSlaveMinimumRequest.FromString,
      tabletmanagerdata_pb2.StopSlaveMinimumResponse.SerializeToString,
    ),
    "TabletExternallyElected": utilities.unary_unary_service_description(
      servicer.TabletExternallyElected,
      tabletmanagerdata_pb2.TabletExternallyElectedRequest.FromString,
      tabletmanagerdata_pb2.TabletExternallyElectedResponse.SerializeToString,
    ),
    "TabletExternallyReparented": utilities.unary_unary_service_description(
      servicer.TabletExternallyReparented,
      tabletmanagerdata_pb2.TabletExternallyReparentedRequest.FromString,
      tabletmanagerdata_pb2.TabletExternallyReparentedResponse.SerializeToString,
    ),
    "WaitBlpPosition": utilities.unary_unary_service_description(
      servicer.WaitBlpPosition,
      tabletmanagerdata_pb2.WaitBlpPositionRequest.FromString,
      tabletmanagerdata_pb2.WaitBlpPositionResponse.SerializeToString,
    ),
  }
  return implementations.server("tabletmanagerservice.TabletManager", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_TabletManager_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  import tabletmanagerdata_pb2
  method_invocation_descriptions = {
    "ApplySchema": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ApplySchemaRequest.SerializeToString,
      tabletmanagerdata_pb2.ApplySchemaResponse.FromString,
    ),
    "Backup": utilities.unary_stream_invocation_description(
      tabletmanagerdata_pb2.BackupRequest.SerializeToString,
      tabletmanagerdata_pb2.BackupResponse.FromString,
    ),
    "ChangeType": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ChangeTypeRequest.SerializeToString,
      tabletmanagerdata_pb2.ChangeTypeResponse.FromString,
    ),
    "DemoteMaster": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.DemoteMasterRequest.SerializeToString,
      tabletmanagerdata_pb2.DemoteMasterResponse.FromString,
    ),
    "ExecuteFetchAsApp": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ExecuteFetchAsAppRequest.SerializeToString,
      tabletmanagerdata_pb2.ExecuteFetchAsAppResponse.FromString,
    ),
    "ExecuteFetchAsDba": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ExecuteFetchAsDbaRequest.SerializeToString,
      tabletmanagerdata_pb2.ExecuteFetchAsDbaResponse.FromString,
    ),
    "ExecuteHook": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ExecuteHookRequest.SerializeToString,
      tabletmanagerdata_pb2.ExecuteHookResponse.FromString,
    ),
    "GetPermissions": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.GetPermissionsRequest.SerializeToString,
      tabletmanagerdata_pb2.GetPermissionsResponse.FromString,
    ),
    "GetSchema": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.GetSchemaRequest.SerializeToString,
      tabletmanagerdata_pb2.GetSchemaResponse.FromString,
    ),
    "GetSlaves": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.GetSlavesRequest.SerializeToString,
      tabletmanagerdata_pb2.GetSlavesResponse.FromString,
    ),
    "InitMaster": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.InitMasterRequest.SerializeToString,
      tabletmanagerdata_pb2.InitMasterResponse.FromString,
    ),
    "InitSlave": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.InitSlaveRequest.SerializeToString,
      tabletmanagerdata_pb2.InitSlaveResponse.FromString,
    ),
    "MasterPosition": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.MasterPositionRequest.SerializeToString,
      tabletmanagerdata_pb2.MasterPositionResponse.FromString,
    ),
    "Ping": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.PingRequest.SerializeToString,
      tabletmanagerdata_pb2.PingResponse.FromString,
    ),
    "PopulateReparentJournal": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.PopulateReparentJournalRequest.SerializeToString,
      tabletmanagerdata_pb2.PopulateReparentJournalResponse.FromString,
    ),
    "PreflightSchema": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.PreflightSchemaRequest.SerializeToString,
      tabletmanagerdata_pb2.PreflightSchemaResponse.FromString,
    ),
    "PromoteSlave": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.PromoteSlaveRequest.SerializeToString,
      tabletmanagerdata_pb2.PromoteSlaveResponse.FromString,
    ),
    "PromoteSlaveWhenCaughtUp": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.PromoteSlaveWhenCaughtUpRequest.SerializeToString,
      tabletmanagerdata_pb2.PromoteSlaveWhenCaughtUpResponse.FromString,
    ),
    "RefreshState": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.RefreshStateRequest.SerializeToString,
      tabletmanagerdata_pb2.RefreshStateResponse.FromString,
    ),
    "ReloadSchema": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ReloadSchemaRequest.SerializeToString,
      tabletmanagerdata_pb2.ReloadSchemaResponse.FromString,
    ),
    "ResetReplication": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ResetReplicationRequest.SerializeToString,
      tabletmanagerdata_pb2.ResetReplicationResponse.FromString,
    ),
    "RunBlpUntil": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.RunBlpUntilRequest.SerializeToString,
      tabletmanagerdata_pb2.RunBlpUntilResponse.FromString,
    ),
    "RunHealthCheck": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.RunHealthCheckRequest.SerializeToString,
      tabletmanagerdata_pb2.RunHealthCheckResponse.FromString,
    ),
    "Scrap": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.ScrapRequest.SerializeToString,
      tabletmanagerdata_pb2.ScrapResponse.FromString,
    ),
    "SetMaster": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SetMasterRequest.SerializeToString,
      tabletmanagerdata_pb2.SetMasterResponse.FromString,
    ),
    "SetReadOnly": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SetReadOnlyRequest.SerializeToString,
      tabletmanagerdata_pb2.SetReadOnlyResponse.FromString,
    ),
    "SetReadWrite": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SetReadWriteRequest.SerializeToString,
      tabletmanagerdata_pb2.SetReadWriteResponse.FromString,
    ),
    "SlaveStatus": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SlaveStatusRequest.SerializeToString,
      tabletmanagerdata_pb2.SlaveStatusResponse.FromString,
    ),
    "SlaveWasPromoted": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SlaveWasPromotedRequest.SerializeToString,
      tabletmanagerdata_pb2.SlaveWasPromotedResponse.FromString,
    ),
    "SlaveWasRestarted": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SlaveWasRestartedRequest.SerializeToString,
      tabletmanagerdata_pb2.SlaveWasRestartedResponse.FromString,
    ),
    "Sleep": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.SleepRequest.SerializeToString,
      tabletmanagerdata_pb2.SleepResponse.FromString,
    ),
    "StartBlp": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StartBlpRequest.SerializeToString,
      tabletmanagerdata_pb2.StartBlpResponse.FromString,
    ),
    "StartSlave": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StartSlaveRequest.SerializeToString,
      tabletmanagerdata_pb2.StartSlaveResponse.FromString,
    ),
    "StopBlp": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StopBlpRequest.SerializeToString,
      tabletmanagerdata_pb2.StopBlpResponse.FromString,
    ),
    "StopReplicationAndGetStatus": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StopReplicationAndGetStatusRequest.SerializeToString,
      tabletmanagerdata_pb2.StopReplicationAndGetStatusResponse.FromString,
    ),
    "StopSlave": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StopSlaveRequest.SerializeToString,
      tabletmanagerdata_pb2.StopSlaveResponse.FromString,
    ),
    "StopSlaveMinimum": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.StopSlaveMinimumRequest.SerializeToString,
      tabletmanagerdata_pb2.StopSlaveMinimumResponse.FromString,
    ),
    "TabletExternallyElected": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.TabletExternallyElectedRequest.SerializeToString,
      tabletmanagerdata_pb2.TabletExternallyElectedResponse.FromString,
    ),
    "TabletExternallyReparented": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.TabletExternallyReparentedRequest.SerializeToString,
      tabletmanagerdata_pb2.TabletExternallyReparentedResponse.FromString,
    ),
    "WaitBlpPosition": utilities.unary_unary_invocation_description(
      tabletmanagerdata_pb2.WaitBlpPositionRequest.SerializeToString,
      tabletmanagerdata_pb2.WaitBlpPositionResponse.FromString,
    ),
  }
  return implementations.stub("tabletmanagerservice.TabletManager", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)
# @@protoc_insertion_point(module_scope)
