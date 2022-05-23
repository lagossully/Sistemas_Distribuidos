import time
import datetime
import json



g= open('../Jsons/blocked.json')
BDD_Blocked=json.load(g)
f= open('../Jsons/BDD_ID.json')
BDD_ID=json.load(f)
def authenticator(login_try):
    userblocked = [x for x in BDD_Blocked if x["ID"] == login_try["ID"]]
    print(userblocked[0]["blocked"])
    stringlogin = str(login_try)
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
            
            
    else:
        stringDenied = "Lo sentimos su cuenta se encuentra Bloqueada"
        print(stringDenied)
        print(stringlogin)
        return stringDenied + stringlogin
