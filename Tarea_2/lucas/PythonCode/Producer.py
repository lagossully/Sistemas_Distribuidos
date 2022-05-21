from ensurepip import bootstrap
import time
import json
from datetime import datetime
from login  import getlogin
from kafka import KafkaProducer



#kafka Producer
producer = KafkaProducer(
    bootstrap_servers =['localhost:9092'],
    value_serializer=serializer
)

if __name__ == "__main__":
    while True:
        # generar intento de login
        login_try = getlogin()
        

        # enviar intento de login
        print(f'intento de login @{datetime.now()} | login = {str(login_try)}')
        producer.send('topic',login_try)

        

