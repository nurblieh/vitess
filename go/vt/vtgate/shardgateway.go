// Copyright 2015, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package vtgate

import (
	"fmt"
	"strings"
	"sync"
	"time"

	"golang.org/x/net/context"

	mproto "github.com/youtube/vitess/go/mysql/proto"
	"github.com/youtube/vitess/go/stats"
	pb "github.com/youtube/vitess/go/vt/proto/topodata"
	tproto "github.com/youtube/vitess/go/vt/tabletserver/proto"
	"github.com/youtube/vitess/go/vt/tabletserver/tabletconn"
)

const (
	gatewayImplementation = "shardconn"
)

func init() {
	RegisterGatewayCreator(gatewayImplementation, createShardGateway)
}

func createShardGateway(serv SrvTopoServer, cell string, retryDelay time.Duration, retryCount int, connTimeoutTotal, connTimeoutPerConn, connLife time.Duration, connTimings *stats.MultiTimings) Gateway {
	return &shardGateway{
		toposerv:           serv,
		cell:               cell,
		retryDelay:         retryDelay,
		retryCount:         retryCount,
		connTimeoutTotal:   connTimeoutTotal,
		connTimeoutPerConn: connTimeoutPerConn,
		connLife:           connLife,
		connTimings:        connTimings,
		shardConns:         make(map[string]*ShardConn),
	}
}

// A Gateway is the query processing module for each shard.
type shardGateway struct {
	toposerv           SrvTopoServer
	cell               string
	retryDelay         time.Duration
	retryCount         int
	connTimeoutTotal   time.Duration
	connTimeoutPerConn time.Duration
	connLife           time.Duration
	connTimings        *stats.MultiTimings

	mu         sync.Mutex
	shardConns map[string]*ShardConn
}

// Dial creates the ShardConn for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) Dial(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType) error {
	return sg.getConnection(ctx, keyspace, shard, tabletType).Dial(ctx)
}

// Execute executes the non-streaming query for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) Execute(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, query string, bindVars map[string]interface{}, transactionID int64) (*mproto.QueryResult, error) {
	return sg.getConnection(ctx, keyspace, shard, tabletType).Execute(ctx, query, bindVars, transactionID)
}

// ExecuteBatch executes a group of queries for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) ExecuteBatch(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, queries []tproto.BoundQuery, asTransaction bool, transactionID int64) (*tproto.QueryResultList, error) {
	return sg.getConnection(ctx, keyspace, shard, tabletType).ExecuteBatch(ctx, queries, asTransaction, transactionID)
}

// StreamExecute executes a streaming query for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) StreamExecute(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, query string, bindVars map[string]interface{}, transactionID int64) (<-chan *mproto.QueryResult, tabletconn.ErrFunc) {
	return sg.getConnection(ctx, keyspace, shard, tabletType).StreamExecute(ctx, query, bindVars, transactionID)
}

// Begin starts a transaction for the specified keyspace, shard, and tablet type.
// It returns the transaction ID.
func (sg *shardGateway) Begin(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType) (int64, error) {
	return sg.getConnection(ctx, keyspace, shard, tabletType).Begin(ctx)
}

// Commit commits the current transaction for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) Commit(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, transactionID int64) error {
	return sg.getConnection(ctx, keyspace, shard, tabletType).Commit(ctx, transactionID)
}

// Rollback rolls back the current transaction for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) Rollback(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, transactionID int64) error {
	return sg.getConnection(ctx, keyspace, shard, tabletType).Rollback(ctx, transactionID)
}

// SplitQuery splits a query into sub-queries for the specified keyspace, shard, and tablet type.
func (sg *shardGateway) SplitQuery(ctx context.Context, keyspace string, shard string, tabletType pb.TabletType, sql string, bindVars map[string]interface{}, splitColumn string, splitCount int) ([]tproto.QuerySplit, error) {
	return sg.getConnection(ctx, keyspace, shard, tabletType).SplitQuery(ctx, sql, bindVars, splitColumn, splitCount)
}

// Close shuts down the underlying connections.
func (sg *shardGateway) Close() error {
	sg.mu.Lock()
	defer sg.mu.Unlock()
	for _, v := range sg.shardConns {
		v.Close()
	}
	sg.shardConns = make(map[string]*ShardConn)
	return nil
}

func (sg *shardGateway) getConnection(ctx context.Context, keyspace, shard string, tabletType pb.TabletType) *ShardConn {
	sg.mu.Lock()
	defer sg.mu.Unlock()

	key := fmt.Sprintf("%s.%s.%s", keyspace, shard, strings.ToLower(tabletType.String()))
	sdc, ok := sg.shardConns[key]
	if !ok {
		sdc = NewShardConn(ctx, sg.toposerv, sg.cell, keyspace, shard, tabletType, sg.retryDelay, sg.retryCount, sg.connTimeoutTotal, sg.connTimeoutPerConn, sg.connLife, sg.connTimings)
		sg.shardConns[key] = sdc
	}
	return sdc
}
