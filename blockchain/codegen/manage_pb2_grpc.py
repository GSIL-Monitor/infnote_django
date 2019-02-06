# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import manage_pb2 as manage__pb2


class IFCManageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPeers = channel.unary_stream(
        '/manage.IFCManage/GetPeers',
        request_serializer=manage__pb2.PeerRequest.SerializeToString,
        response_deserializer=manage__pb2.PeerResponse.FromString,
        )
    self.GetChains = channel.unary_stream(
        '/manage.IFCManage/GetChains',
        request_serializer=manage__pb2.ChainRequest.SerializeToString,
        response_deserializer=manage__pb2.ChainResponse.FromString,
        )
    self.GetBlocks = channel.unary_stream(
        '/manage.IFCManage/GetBlocks',
        request_serializer=manage__pb2.BlockRequest.SerializeToString,
        response_deserializer=manage__pb2.BlockResponse.FromString,
        )
    self.CreateChain = channel.unary_unary(
        '/manage.IFCManage/CreateChain',
        request_serializer=manage__pb2.ChainCreationRequest.SerializeToString,
        response_deserializer=manage__pb2.ChainCreationResponse.FromString,
        )
    self.CreateBlock = channel.unary_unary(
        '/manage.IFCManage/CreateBlock',
        request_serializer=manage__pb2.BlockCreationRequest.SerializeToString,
        response_deserializer=manage__pb2.BlockCreationResponse.FromString,
        )


class IFCManageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPeers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChains(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlocks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateChain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IFCManageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPeers': grpc.unary_stream_rpc_method_handler(
          servicer.GetPeers,
          request_deserializer=manage__pb2.PeerRequest.FromString,
          response_serializer=manage__pb2.PeerResponse.SerializeToString,
      ),
      'GetChains': grpc.unary_stream_rpc_method_handler(
          servicer.GetChains,
          request_deserializer=manage__pb2.ChainRequest.FromString,
          response_serializer=manage__pb2.ChainResponse.SerializeToString,
      ),
      'GetBlocks': grpc.unary_stream_rpc_method_handler(
          servicer.GetBlocks,
          request_deserializer=manage__pb2.BlockRequest.FromString,
          response_serializer=manage__pb2.BlockResponse.SerializeToString,
      ),
      'CreateChain': grpc.unary_unary_rpc_method_handler(
          servicer.CreateChain,
          request_deserializer=manage__pb2.ChainCreationRequest.FromString,
          response_serializer=manage__pb2.ChainCreationResponse.SerializeToString,
      ),
      'CreateBlock': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBlock,
          request_deserializer=manage__pb2.BlockCreationRequest.FromString,
          response_serializer=manage__pb2.BlockCreationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'manage.IFCManage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
