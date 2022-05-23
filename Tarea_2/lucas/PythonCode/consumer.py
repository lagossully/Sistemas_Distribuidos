from ensurepip import bootstrap
import json
from kafka import KafkaConsumer



if __name__ == "__main__":
    

    #kafka consumer
    consumer = KafkaConsumer(
        'sample',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest'
    )
    for loginT in consumer:
        print(json.loads(loginT.value))
    
    for message in consumer:
        print (message)
