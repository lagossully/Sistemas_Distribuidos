from concurrent.futures import thread
from ensurepip import bootstrap
import json
from kafka import KafkaConsumer
import time
import datetime
from numpy import tri
from pyparsing import trace_parse_action
from Tarea_2.lucas.Consumer.PythonCode.verificador import BDD_ID, BDD_logs, authenticator, Bloquear
import verificador as V
import threading



def consume():
    consumer = KafkaConsumer(
        'sample',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest'
    )
    for loginT in consumer:
        print(json.loads(loginT.value))
        if(V.Blockeado()):         
            authenticator(loginT)
        else:
            stringlogin=str(loginT)
            stringDenied = "Lo sentimos su cuenta se encuentra Bloqueada"
            print(stringDenied)
            print(stringlogin)
            stringDenied + stringlogin
        ##ACÁ GUARDAR EN JSON LA HORA Y EL USUARIO 
def Seguridad():
    for data in BDD_ID:
        triblock = [x for x in BDD_logs if x["ID"] == data["ID"] and x["Acceso"]=="False"]
        
        for i in range(0,len(triblock)):
            if(triblock[i]["Fecha"] - triblock[i-1]["Fecha"] <= datetime.datetime.strptime("01",'%M') and triblock[i]["Fecha"] - triblock[i-2]["Fecha"]<= datetime.datetime.strptime("01",'%M') and triblock[i]["Fecha"] - triblock[i-3]["Fecha"]<= datetime.datetime.strptime("01",'%M') and triblock[i]["Fecha"] - triblock[i-4]["Fecha"]<= datetime.datetime.strptime("01",'%M')):
                Bloquear(data)
    return

def consumermain():
    while True:
        Hilo1 = threading.Thread(target=consume())
        Hilo2 = threading.Thread(target=Seguridad())
    
    
    
