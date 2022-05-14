
from concurrent import futures
import logging
from mensaje_pb2_grpc import ItemService
from mensaje_pb2 import Response

import grpc




class ServicioItems(ItemService):
    def GetItem(self,request,context):
        
        return Response()
    



# class Greeter(helloworld_pb2_grpc.GreeterServicer):

#     def SayHello(self, request, context):
#         return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()




