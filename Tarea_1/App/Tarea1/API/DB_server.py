
from concurrent import futures
import logging
import mensaje_pb2_grpc as mensajepb2
from mensaje_pb2_grpc import ItemService
from mensaje_pb2 import Response
import grpc
import psycopg2
import sys


conn = psycopg2.connect(
    host="localhost",
    database="tiendita",
    user="postgres",
    password="marihuana")
cur = conn.cursor()


class ServicioItems(ItemService):
    def GetItem(self,request,context):
        introredis = str(sys.argv[1])
        cur.execute('SELECT * FROM ITEMS WHERE Name LIKE %s OR Price LIKE %s OR Category LIKE %s  OR Count LIKE %s')(introredis)
        return Response()
    




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # mensaje_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    print("Servidor Arriba")

if __name__ == '__main__':
    serve()





