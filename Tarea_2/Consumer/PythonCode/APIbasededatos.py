from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import json
from datetime import datetime
from Tarea_2.Consumer.PythonCode.consumer import consumermain
import consumer

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    consumermain()
    return 


@app.route('/blocked', methods=['GET', 'POST'])
def block():
    g= open('../Jsons/blocked.json')
    Blocked=json.load(g)
    return str(Blocked)


#@app.route('/block', methods=['GET', 'POST'])
#def otro():


#@app.route('/unblock', methods=['GET', 'POST'])
#def otro1():



@app.route('/correctID', methods=['GET', 'POST'])
def CoID():
    g= open('../Jsons/BDD_ID.json')
    CID=json.load(g)
    return str(CID)
    
@app.route('/Login', methods=['GET', 'POST'])
def LoginTry(Logindata):
    return str(Logindata)


@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
