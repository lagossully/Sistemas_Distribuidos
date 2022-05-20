from ensurepip import bootstrap
import time
import json
import random
from datetime import datetime

from kafka import KafkaProducer




def serializer(loginT):
    return json.dumps(loginT).encode('utf-8')

#kafka Producer
producer = KafkaProducer(
    bootstrap_servers =['localhost:9092'],
    value_serializer=serializer
)

if __name__ == "__main__":
    while true:
        # generar intento de login
        login_try = get_login()


        # enviar intento de login
        print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        producer.send('topic',login_try)

        

