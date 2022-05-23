from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
from wtforms import Form, StringField, SelectField
from Producer import funcproducer

app = flask.Flask(__name__)
app.config["DEBUG"] = True





@app.route('/', methods=['GET'])
def home():
    intento = funcproducer()
    return str(intento)





@app.errorhandler(404)
def no_encontrado(e):
    return "<h1>404</h1><p>No se encontró la página</p><a href ='/'>Inicio</a>", 404


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=444)