from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import sqlite3
from wtforms import Form, StringField, SelectField
import os 

app = flask.Flask(__name__)
app.config["DEBUG"] = True





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "¨POST":
        os.system("Test.py 1")
    os.system("Test.py 1")




@app.route('/all', methods=['GET'])
def api_all():
    return render_template('home.html')


@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404


@app.route('/productos', methods=['GET'])
def api_filter():
    return render_template('home.html')

app.run()