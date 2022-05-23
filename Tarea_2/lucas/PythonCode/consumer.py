from ensurepip import bootstrap
import json
from kafka import KafkaConsumer
import time
import datetime


if __name__ == "__main__":
    

    #kafka consumer
    consumer = KafkaConsumer(
        'sample',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest'
    )
    for loginT in consumer:
        print(json.loads(loginT.value))
        ##ACÁ GUARDAR EN JSON LA HORA Y EL USUARIO
    
    for message in consumer:
        print (message)
        ##ACÁ GUARDAR EN JSON LA HORA Y EL USUARIO
