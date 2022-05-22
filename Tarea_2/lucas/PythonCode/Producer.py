from ensurepip import bootstrap
import time
import json
from datetime import datetime
from login  import getlogin
from kafka import KafkaProducer
f= open('../Jsons/BDD_ID.json')
g= open('../Jsons/bloked.json')
BDD_ID=json.load(f)
Blocked=json.load(g)
print(BDD_ID)
def serializer(login):
    return json.dumps(login).encode('uft-8')

# #kafka Producer
# producer = KafkaProducer(
#     bootstrap_servers =['localhost:9092'],
#     value_serializer=Serializer
# )
# print(getlogin())
if __name__ == "__main__":
    # while True:
        # generar intento de login
        login_try = getlogin()

        print(login_try)
        userblocked = [x for x in Blocked if x["ID"] == login_try["ID"]]
        print(userblocked[0]["blocked"])
        if(userblocked[0]["blocked"] =='0'):
            if(login_try in BDD_ID ):
                print("Acceso Correcto")
            else:
                print("Acceso Denegado")
        else:
            print("Lo sentimos su cuenta se encuentra Bloqueada")

        # # enviar intento de login
        # print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        # producer.send('topic',login_try)

        

