from distutils.log import Log
import time
import datetime
import json
import requests


g= open('../Jsons/blocked.json')
j= open('../Jsons/BDD_logs.json')
f= open('../Jsons/BDD_ID.json')
BDD_ID=json.load(f)
BDD_Blocked=json.load(g)
BDD_logs=json.load(j)
print(BDD_logs)
def addLog(Login,Acceso):
    entry={
        "ID": Login["ID"],
        "Acceso": str(Acceso),
        "Fecha":Login["Date"]
    }
    BDD_logs.append(entry)
    print(BDD_logs)
    with open('../Jsons/BDD_logs.json',"w") as file:
        json.dump(BDD_logs,file)

    return
def Blockeado(login_try):
    userblocked = [x for x in BDD_Blocked if x["ID"] == login_try["ID"]]
    print(userblocked[0]["blocked"])
    if(userblocked[0]["blocked"] =='0'):
        return True
    else:
        return False
        
def authenticator(login_try):
    loginTry={
                "ID":login_try["ID"],
                "Pass":login_try["Pass"]
            }
    stringlogin = str(loginTry)
    if(loginTry in BDD_ID ):
        stringOk = "Acceso Correcto"
        print(stringOk)
        print(stringlogin)
        addLog(login_try,"True")
        respuesta = requests.get('localhost:80/Login', params= stringOk + stringlogin) 
        return stringOk + stringlogin

    else:
        stringNo = "Acceso Denegado"
        print(stringNo)
        print(stringlogin)
        addLog(login_try,"False")
        return stringNo + stringlogin


if __name__ == "__main__":
    loginTry = {
        "ID":"Lucas",
        "Pass":"1234",
        "Date": "05/23/22 18:48:30"
    }
    print(Blockeado(loginTry))
    authenticator(loginTry)