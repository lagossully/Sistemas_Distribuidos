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
        return "hola"
    os.system("python Test.py kotor")
    return "hola"




@app.route('/all', methods=['GET'])
def api_all():
    return render_template('home.html')


@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404


app.run()