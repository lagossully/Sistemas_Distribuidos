import json
from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
from wtforms import Form, StringField, SelectField
from Producer import funcproducer
g= open('../Jsons/blocked.json')
BDD_Blocked=json.load(g)
app = flask.Flask(__name__)
app.config["DEBUG"] = True





@app.route('/', methods=['GET'])
def home():
    intento = funcproducer()
    return str(intento)

@app.route('/Bloquear', methods=['GET'])
def Bloquear(cuenta):
    for i in range(0,len(BDD_Blocked)):
        if cuenta == BDD_Blocked[i]["ID"]:
            BDD_Blocked[i]["blocked"] = "1"
    with open('../Jsons/blocked.json',"w") as file:
        json.dump(BDD_Blocked,file)


@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=444)