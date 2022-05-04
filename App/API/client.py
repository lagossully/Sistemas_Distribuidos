from __future__ import print_function

import logging
import mensaje_pb2_grpc
import mensaje_pb2
import grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mensaje_pb2_grpc.GreeterStub(channel)
        response = stub.GetItem(mensaje_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
