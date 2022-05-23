from ensurepip import bootstrap
import time
import json
import datetime
from login  import getlogin
from kafka import KafkaProducer
import requests
# getlog = getlogin()
# ahora = datetime.datetime.now()
# Horalogin = ahora.strftime("%x %X")

# login_try = {
#     "ID" : getlog["ID"],
#     "Pass" : getlog["Pass"],
#     "Date" : Horalogin
# }


# print(login_try)

def serializer(login):
    return json.dumps(login).encode('uft-8')

def funcproducer():
    
    ##LUCAAS ENVÉS DE ESTAS DOS LINEAS: response = requests.get('localhost:80/algoalgo' ) O response = requests.post('localhost:80/algoalgo', data = {'key':'value'})
    BDD_ID = requests.get('localhost:80/correctID')
    
    Blocked=json.load(g)
    ##LUCAAS ENVÉS DE ESTAS DOS LINEAS: response = requests.get('localhost:80/algoalgo' ) O response = requests.post('localhost:80/algoalgo', data = {'key':'value'})
    print(BDD_ID)
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
             api_version=(0,11,5)
    )
    getlog = getlogin()
    ahora = datetime.datetime.now()
    Horalogin = ahora.strftime("%x %X")
    
    login_try = {
        "ID" : getlog["ID"],
        "Pass" : getlog["Pass"],
        "Date" : Horalogin
    }
    
    
    print(login_try)
    producer.send('sample', json.dumps(login_try, default=json_util.default).encode('utf-8'))
        # # enviar intento de login
        # print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        # producer.send('topic',login_try)

#kafka Producer
#producer = KafkaProducer(
#    bootstrap_servers =['localhost:9092'],
#    value_serializer=Serializer()
#)
# print(getlogin())

       

        

