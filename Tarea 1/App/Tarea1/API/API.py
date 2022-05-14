from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import sqlite3
from wtforms import Form, StringField, SelectField
import os 
import Test

app = flask.Flask(__name__)
app.config["DEBUG"] = True





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "¨POST":
        os.system("python Test.py")  
        return "Por favor revisar la consola"
    os.system("python Test.py")
    return "Por favor revisar la consola"




@app.route('/all', methods=['GET'])
def api_all():
    return "Por favor revisar la consola"


@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404


app.run()