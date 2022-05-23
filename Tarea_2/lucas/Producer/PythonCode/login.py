import json
import random
f=open('../Jsons/credencialesRandomID.json')
g= open('../Jsons/credencialesRandomPass.json')
datosID=json.load(f)
datosPass=json.load(g)

# print(datosID)
# print(datosPass)

valorID=list(range(0,4))
ValorPass=list(range(0,9))

def getlogin():
    ValorRaID = random.choice(valorID)
    ValorRaPass = random.choice(ValorPass)

    aux1 = datosID[ValorRaID]
    aux2 = datosPass[ValorRaPass]

    # print("############################################################################ \n")
    # print(aux1["ID"])
    # print(aux2["Pass"])    
    respond = {
            'ID': aux1["ID"],
            'Pass': aux2["Pass"]
        }
    return respond
    
if __name__ == "__main__":
    getlogin()
