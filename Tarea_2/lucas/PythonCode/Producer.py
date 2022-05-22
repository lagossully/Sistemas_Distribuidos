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

def funcproducer():
    login_try = getlogin()
    stringlogin = str(login_try)
    print(login_try)
    userblocked = [x for x in Blocked if x["ID"] == login_try["ID"]]
    print(userblocked[0]["blocked"])
    if(userblocked[0]["blocked"] =='0'):
        if(login_try in BDD_ID ):
            stringOk = "Acceso Correcto"
            print(stringOk)
            print(stringlogin)
            return stringlogin + stringOk

        else:
            stringNo = "Acceso Denegado"
            print(stringNo)
            print(stringlogin)
            return stringlogin + stringNo
    else:
        stringDenied = "Lo sentimos su cuenta se encuentra Bloqueada"
        print(stringDenied)
        print(stringlogin)
        return stringlogin + stringDenied

        # # enviar intento de login
        # print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        # producer.send('topic',login_try)

# #kafka Producer
# producer = KafkaProducer(
#     bootstrap_servers =['localhost:9092'],
#     value_serializer=Serializer
# )
# print(getlogin())

       

        

