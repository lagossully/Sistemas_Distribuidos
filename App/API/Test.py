import redis
import sys

r = redis.Redis(host='localhost', port=6379)

r.set("lol","league of legends")
r.set("kotor","knigths of the old republic")


def redis_consulta():
        try:
            print("Ingrese parametros")
            b = str(sys.argv[1])

            if (r.exists(b)):
                print((r.get(b)))
            else:
                print("no existe")
            ###PREGUNTAR A GRPC CLIENT QUE LE DIGA A GRPC SERVER BUSCAR LOS DATOS
            ###RECIBIR LOS DATOS Y GUARDARLOS ACÁ EN REDIS
            ###IMPRIMIRLOS
        except Exception as e:
            print(e)

def redis_interger():
    try:
        r.set("number","100")
        num = r.get("number")
        r.incr("number")
        num_incr = r.get("number")
        print(num)
        print(num_incr)
    except:
        print("algo salió mal")

if __name__ == "__main__":
        redis_consulta()
        redis_interger()