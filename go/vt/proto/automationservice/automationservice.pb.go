// Code generated by protoc-gen-go.
// source: automationservice.proto
// DO NOT EDIT!

/*
Package automationservice is a generated protocol buffer package.

It is generated from these files:
	automationservice.proto

It has these top-level messages:
*/
package automationservice

import proto "github.com/golang/protobuf/proto"
import automation "github.com/youtube/vitess/go/vt/proto/automation"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// Client API for Automation service

type AutomationClient interface {
	// Start a cluster operation.
	EnqueueClusterOperation(ctx context.Context, in *automation.EnqueueClusterOperationRequest, opts ...grpc.CallOption) (*automation.EnqueueClusterOperationResponse, error)
	// TODO(mberlin): Polling this is bad. Implement a subscribe mechanism to wait for changes?
	// Get all details of an active cluster operation.
	GetClusterOperationDetails(ctx context.Context, in *automation.GetClusterOperationDetailsRequest, opts ...grpc.CallOption) (*automation.GetClusterOperationDetailsResponse, error)
}

type automationClient struct {
	cc *grpc.ClientConn
}

func NewAutomationClient(cc *grpc.ClientConn) AutomationClient {
	return &automationClient{cc}
}

func (c *automationClient) EnqueueClusterOperation(ctx context.Context, in *automation.EnqueueClusterOperationRequest, opts ...grpc.CallOption) (*automation.EnqueueClusterOperationResponse, error) {
	out := new(automation.EnqueueClusterOperationResponse)
	err := grpc.Invoke(ctx, "/automationservice.Automation/EnqueueClusterOperation", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *automationClient) GetClusterOperationDetails(ctx context.Context, in *automation.GetClusterOperationDetailsRequest, opts ...grpc.CallOption) (*automation.GetClusterOperationDetailsResponse, error) {
	out := new(automation.GetClusterOperationDetailsResponse)
	err := grpc.Invoke(ctx, "/automationservice.Automation/GetClusterOperationDetails", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for Automation service

type AutomationServer interface {
	// Start a cluster operation.
	EnqueueClusterOperation(context.Context, *automation.EnqueueClusterOperationRequest) (*automation.EnqueueClusterOperationResponse, error)
	// TODO(mberlin): Polling this is bad. Implement a subscribe mechanism to wait for changes?
	// Get all details of an active cluster operation.
	GetClusterOperationDetails(context.Context, *automation.GetClusterOperationDetailsRequest) (*automation.GetClusterOperationDetailsResponse, error)
}

func RegisterAutomationServer(s *grpc.Server, srv AutomationServer) {
	s.RegisterService(&_Automation_serviceDesc, srv)
}

func _Automation_EnqueueClusterOperation_Handler(srv interface{}, ctx context.Context, codec grpc.Codec, buf []byte) (interface{}, error) {
	in := new(automation.EnqueueClusterOperationRequest)
	if err := codec.Unmarshal(buf, in); err != nil {
		return nil, err
	}
	out, err := srv.(AutomationServer).EnqueueClusterOperation(ctx, in)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func _Automation_GetClusterOperationDetails_Handler(srv interface{}, ctx context.Context, codec grpc.Codec, buf []byte) (interface{}, error) {
	in := new(automation.GetClusterOperationDetailsRequest)
	if err := codec.Unmarshal(buf, in); err != nil {
		return nil, err
	}
	out, err := srv.(AutomationServer).GetClusterOperationDetails(ctx, in)
	if err != nil {
		return nil, err
	}
	return out, nil
}

var _Automation_serviceDesc = grpc.ServiceDesc{
	ServiceName: "automationservice.Automation",
	HandlerType: (*AutomationServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "EnqueueClusterOperation",
			Handler:    _Automation_EnqueueClusterOperation_Handler,
		},
		{
			MethodName: "GetClusterOperationDetails",
			Handler:    _Automation_GetClusterOperationDetails_Handler,
		},
	},
	Streams: []grpc.StreamDesc{},
}
