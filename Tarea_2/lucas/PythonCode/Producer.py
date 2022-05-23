from ensurepip import bootstrap
import time
import json
from datetime import datetime
from login  import getlogin
from kafka import KafkaProducer
import requests


def serializer(login):
    return json.dumps(login).encode('uft-8')

def funcproducer():
    #f= open('../Jsons/BDD_ID.json')
    #BDD_ID=json.load(f)
    ##LUCAAS ENVÉS DE ESTAS DOS LINEAS: response = requests.get('localhost:80/algoalgo' ) O response = requests.post('localhost:80/algoalgo', data = {'key':'value'})
    BDD_ID = requests.get('localhost:80/correctID')
    g= open('../Jsons/blocked.json')
    Blocked=json.load(g)
    ##LUCAAS ENVÉS DE ESTAS DOS LINEAS: response = requests.get('localhost:80/algoalgo' ) O response = requests.post('localhost:80/algoalgo', data = {'key':'value'})
    print(BDD_ID)
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
             api_version=(0,11,5)
    )
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
            return stringOk + stringlogin

        else:
            stringNo = "Acceso Denegado"
            print(stringNo)
            print(stringlogin)
            return stringNo + stringlogin
            producer.send('sample', json.dumps(login_try, default=json_util.default).encode('utf-8'))
            
    else:
        stringDenied = "Lo sentimos su cuenta se encuentra Bloqueada"
        print(stringDenied)
        print(stringlogin)
        return stringDenied + stringlogin

        # # enviar intento de login
        # print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        # producer.send('topic',login_try)

#kafka Producer
#producer = KafkaProducer(
#    bootstrap_servers =['localhost:9092'],
#    value_serializer=Serializer()
#)
# print(getlogin())

       

        

