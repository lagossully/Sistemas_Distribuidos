import redis

r = redis.Redis(host='localhost', port=6379)

r.set("lol","league of legends")
r.set("kotor","knigths of the old republic")



print("Ingrese parametros")
b = input()

if (r.exists(b)):
    print((r.get("lol")))
else:
    print("no existe")
    ###PREGUNTAR A GRPC CLIENT QUE LE DIGA A GRPC SERVER BUSCAR LOS DATOS
    ###RECIBIR LOS DATOS Y GUARDARLOS ACÁ EN REDIS
    ###IMPRIMIRLOS