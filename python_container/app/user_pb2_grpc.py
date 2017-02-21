# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import user_pb2 as user__pb2


class UserdbStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddUser = channel.unary_unary(
        '/user.Userdb/AddUser',
        request_serializer=user__pb2.User.SerializeToString,
        response_deserializer=user__pb2.Status.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/user.Userdb/DeleteUser',
        request_serializer=user__pb2.User_Name.SerializeToString,
        response_deserializer=user__pb2.Status.FromString,
        )
    self.GetUsers = channel.unary_unary(
        '/user.Userdb/GetUsers',
        request_serializer=user__pb2.User_list.SerializeToString,
        response_deserializer=user__pb2.Users.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/user.Userdb/GetUser',
        request_serializer=user__pb2.User_Name.SerializeToString,
        response_deserializer=user__pb2.User.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/user.Userdb/UpdateUser',
        request_serializer=user__pb2.User.SerializeToString,
        response_deserializer=user__pb2.Status.FromString,
        )


class UserdbServicer(object):

  def AddUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsers(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserdbServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddUser': grpc.unary_unary_rpc_method_handler(
          servicer.AddUser,
          request_deserializer=user__pb2.User.FromString,
          response_serializer=user__pb2.Status.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=user__pb2.User_Name.FromString,
          response_serializer=user__pb2.Status.SerializeToString,
      ),
      'GetUsers': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsers,
          request_deserializer=user__pb2.User_list.FromString,
          response_serializer=user__pb2.Users.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=user__pb2.User_Name.FromString,
          response_serializer=user__pb2.User.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=user__pb2.User.FromString,
          response_serializer=user__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'user.Userdb', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
