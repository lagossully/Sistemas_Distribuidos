from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import json
from datetime import datetime
from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'],port=3000)
session = cluster.connect()
session.execute('CREATE KEYSPACE IF NOT EXISTS Cass')
session.execute('CREATE TABLE IF NOT EXISTS paciente (rut int, nombre text, apellido text, email text, fecha_nacimiento text, PRIMARY KEY (rut))')
session.execute('CREATE TABLE IF NOT EXISTS receta (id_paciente int, comentario text, farmacos text, doctor text, PRIMARY KEY (id_paciente)')


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return 

@app.route('/create', methods=['GET', 'POST'])
def home():
    return 

@app.route('/edit', methods=['GET', 'POST'])
def home():
    return

@app.route('/delete', methods=['GET', 'POST'])
def home():
    return 