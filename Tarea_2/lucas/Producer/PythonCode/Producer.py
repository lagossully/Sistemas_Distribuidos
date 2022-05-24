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
    
    BDD_ID = requests.get('localhost:80/correctID')
    
    Blocked=json.load(g)
    print(BDD_ID)
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
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
    producer.send('sample', json.dumps(login_try).encode('utf-8'))
       
       

        

