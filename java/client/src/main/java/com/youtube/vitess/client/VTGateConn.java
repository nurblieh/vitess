package com.youtube.vitess.client;

import com.google.common.collect.Iterables;

import com.youtube.vitess.proto.Query.QueryResult;
import com.youtube.vitess.proto.Topodata.KeyRange;
import com.youtube.vitess.proto.Topodata.SrvKeyspace;
import com.youtube.vitess.proto.Topodata.TabletType;
import com.youtube.vitess.proto.Vtgate.BeginRequest;
import com.youtube.vitess.proto.Vtgate.BeginResponse;
import com.youtube.vitess.proto.Vtgate.BoundKeyspaceIdQuery;
import com.youtube.vitess.proto.Vtgate.BoundShardQuery;
import com.youtube.vitess.proto.Vtgate.ExecuteBatchKeyspaceIdsRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteBatchKeyspaceIdsResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteBatchShardsRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteBatchShardsResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteEntityIdsRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteEntityIdsResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteKeyRangesRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteKeyRangesResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteKeyspaceIdsRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteKeyspaceIdsResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteResponse;
import com.youtube.vitess.proto.Vtgate.ExecuteShardsRequest;
import com.youtube.vitess.proto.Vtgate.ExecuteShardsResponse;
import com.youtube.vitess.proto.Vtgate.GetSrvKeyspaceRequest;
import com.youtube.vitess.proto.Vtgate.GetSrvKeyspaceResponse;
import com.youtube.vitess.proto.Vtgate.SplitQueryRequest;
import com.youtube.vitess.proto.Vtgate.SplitQueryResponse;
import com.youtube.vitess.proto.Vtgate.StreamExecuteKeyRangesRequest;
import com.youtube.vitess.proto.Vtgate.StreamExecuteKeyspaceIdsRequest;
import com.youtube.vitess.proto.Vtgate.StreamExecuteRequest;
import com.youtube.vitess.proto.Vtgate.StreamExecuteShardsRequest;

import java.io.Closeable;
import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * VTGateConn manages a VTGate connection.
 *
 * <p>Usage:
 *
 * <pre>
 *   CallerID callerId = CallerID.newBuilder().setPrincipal("username").build();
 *   Context ctx = Context.getDefault()
 *                     .withDeadlineAfter(Duration.millis(500))
 *                     .withCallerId(callerId);
 *   RpcClient client = rpcClientFactory.create(ctx, new InetSocketAddress("host", port));
 *   VTGateConn conn = new VTGateConn(client);
 *
 *   try {
 *     byte ksid[] = computeKeyspaceId(...);
 *     QueryResult result = conn.executeKeyspaceIds(ctx,
 *         "INSERT INTO test_table (col1,col2) VALUES(:val1,:val2)",
 *         "test_keyspace",     // keyspace
 *         Arrays.asList(ksid), // keyspaceIds
 *         ImmutableMap.of(     // bindVars
 *            "val1", 123,
 *            "val2", 456
 *            ),
 *         TabletType.MASTER    // tabletType
 *         );
 *
 *     for (Row row : result.getRowsList()) {
 *       // process each row.
 *     }
 *   } catch (VitessException e) {
 *     // ...
 *   } catch (VitessRpcException e) {
 *     // ...
 *   }
 * </pre>
 * */
public class VTGateConn implements Closeable {
  private RpcClient client;

  public VTGateConn(RpcClient client) {
    this.client = client;
  }

  public QueryResult execute(Context ctx, String query, Map<String, ?> bindVars,
      TabletType tabletType) throws VitessException, VitessRpcException {
    ExecuteRequest.Builder requestBuilder =
        ExecuteRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteResponse response = client.execute(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResult();
  }

  public QueryResult executeShards(Context ctx, String query, String keyspace,
      Iterable<String> shards, Map<String, ?> bindVars, TabletType tabletType)
      throws VitessException, VitessRpcException {
    ExecuteShardsRequest.Builder requestBuilder =
        ExecuteShardsRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllShards(shards)
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteShardsResponse response = client.executeShards(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResult();
  }

  public QueryResult executeKeyspaceIds(Context ctx, String query, String keyspace,
      Iterable<byte[]> keyspaceIds, Map<String, ?> bindVars, TabletType tabletType)
      throws VitessException, VitessRpcException {
    ExecuteKeyspaceIdsRequest.Builder requestBuilder =
        ExecuteKeyspaceIdsRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllKeyspaceIds(Iterables.transform(keyspaceIds, Proto.BYTE_ARRAY_TO_BYTE_STRING))
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteKeyspaceIdsResponse response = client.executeKeyspaceIds(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResult();
  }

  public QueryResult executeKeyRanges(Context ctx, String query, String keyspace,
      Iterable<? extends KeyRange> keyRanges, Map<String, ?> bindVars, TabletType tabletType)
      throws VitessException, VitessRpcException {
    ExecuteKeyRangesRequest.Builder requestBuilder =
        ExecuteKeyRangesRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllKeyRanges(keyRanges)
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteKeyRangesResponse response = client.executeKeyRanges(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResult();
  }

  public QueryResult executeEntityIds(Context ctx, String query, String keyspace,
      String entityColumnName, Map<byte[], ?> entityKeyspaceIds, Map<String, ?> bindVars,
      TabletType tabletType) throws VitessException, VitessRpcException {
    ExecuteEntityIdsRequest.Builder requestBuilder =
        ExecuteEntityIdsRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .setEntityColumnName(entityColumnName)
            .addAllEntityKeyspaceIds(Iterables.transform(
                entityKeyspaceIds.entrySet(), Proto.MAP_ENTRY_TO_ENTITY_KEYSPACE_ID))
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteEntityIdsResponse response = client.executeEntityIds(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResult();
  }

  public List<QueryResult> executeBatchShards(Context ctx,
      Iterable<? extends BoundShardQuery> queries, TabletType tabletType, boolean asTransaction)
      throws VitessException, VitessRpcException {
    ExecuteBatchShardsRequest.Builder requestBuilder =
        ExecuteBatchShardsRequest.newBuilder()
            .addAllQueries(queries)
            .setTabletType(tabletType)
            .setAsTransaction(asTransaction);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteBatchShardsResponse response = client.executeBatchShards(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResultsList();
  }

  public List<QueryResult> executeBatchKeyspaceIds(Context ctx,
      Iterable<? extends BoundKeyspaceIdQuery> queries, TabletType tabletType,
      boolean asTransaction) throws VitessException, VitessRpcException {
    ExecuteBatchKeyspaceIdsRequest.Builder requestBuilder =
        ExecuteBatchKeyspaceIdsRequest.newBuilder()
            .addAllQueries(queries)
            .setTabletType(tabletType)
            .setAsTransaction(asTransaction);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    ExecuteBatchKeyspaceIdsResponse response =
        client.executeBatchKeyspaceIds(ctx, requestBuilder.build());
    Proto.checkError(response.getError());
    return response.getResultsList();
  }

  public StreamIterator<QueryResult> streamExecute(Context ctx, String query,
      Map<String, ?> bindVars, TabletType tabletType) throws VitessRpcException {
    StreamExecuteRequest.Builder requestBuilder =
        StreamExecuteRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    return client.streamExecute(ctx, requestBuilder.build());
  }

  public StreamIterator<QueryResult> streamExecuteShards(Context ctx, String query, String keyspace,
      Iterable<String> shards, Map<String, ?> bindVars, TabletType tabletType)
      throws VitessRpcException {
    StreamExecuteShardsRequest.Builder requestBuilder =
        StreamExecuteShardsRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllShards(shards)
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    return client.streamExecuteShards(ctx, requestBuilder.build());
  }

  public StreamIterator<QueryResult> streamExecuteKeyspaceIds(Context ctx, String query,
      String keyspace, Iterable<byte[]> keyspaceIds, Map<String, ?> bindVars, TabletType tabletType)
      throws VitessRpcException {
    StreamExecuteKeyspaceIdsRequest.Builder requestBuilder =
        StreamExecuteKeyspaceIdsRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllKeyspaceIds(Iterables.transform(keyspaceIds, Proto.BYTE_ARRAY_TO_BYTE_STRING))
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    return client.streamExecuteKeyspaceIds(ctx, requestBuilder.build());
  }

  public StreamIterator<QueryResult> streamExecuteKeyRanges(Context ctx, String query,
      String keyspace, Iterable<? extends KeyRange> keyRanges, Map<String, ?> bindVars,
      TabletType tabletType) throws VitessRpcException {
    StreamExecuteKeyRangesRequest.Builder requestBuilder =
        StreamExecuteKeyRangesRequest.newBuilder()
            .setQuery(Proto.bindQuery(query, bindVars))
            .setKeyspace(keyspace)
            .addAllKeyRanges(keyRanges)
            .setTabletType(tabletType);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    return client.streamExecuteKeyRanges(ctx, requestBuilder.build());
  }

  public VTGateTx begin(Context ctx) throws VitessException, VitessRpcException {
    BeginRequest.Builder requestBuilder = BeginRequest.newBuilder();
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    BeginResponse response = client.begin(ctx, requestBuilder.build());
    return VTGateTx.withRpcClientAndSession(client, response.getSession());
  }

  public List<SplitQueryResponse.Part> splitQuery(Context ctx, String keyspace, String query,
      Map<String, ?> bindVars, String splitColumn, long splitCount)
      throws VitessException, VitessRpcException {
    SplitQueryRequest.Builder requestBuilder =
        SplitQueryRequest.newBuilder()
            .setKeyspace(keyspace)
            .setQuery(Proto.bindQuery(query, bindVars))
            .setSplitColumn(splitColumn)
            .setSplitCount(splitCount);
    if (ctx.getCallerId() != null) {
      requestBuilder.setCallerId(ctx.getCallerId());
    }
    SplitQueryResponse response = client.splitQuery(ctx, requestBuilder.build());
    return response.getSplitsList();
  }

  public SrvKeyspace getSrvKeyspace(Context ctx, String keyspace)
      throws VitessException, VitessRpcException {
    GetSrvKeyspaceRequest.Builder requestBuilder =
        GetSrvKeyspaceRequest.newBuilder().setKeyspace(keyspace);
    GetSrvKeyspaceResponse response = client.getSrvKeyspace(ctx, requestBuilder.build());
    return response.getSrvKeyspace();
  }

  @Override
  public void close() throws IOException {
    client.close();
  }
}
