from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import json
from datetime import datetime
from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'],port=3000)
session = cluster.connect()
session.execute('CREATE KEYSPACE IF NOT EXISTS Cass')
session.execute('CREATE TABLE IF NOT EXISTS paciente (id int, rut int, nombre text, apellido text, email text, fecha_nacimiento text, PRIMARY KEY (rut))')
session.execute('CREATE TABLE IF NOT EXISTS receta (id,id_paciente int, comentario text, farmacos text, doctor text, PRIMARY KEY (id_paciente)')
session.execute(
    """
    INSERT INTO paciente (id, rut, nombre, apellido, email, fecha_nacimiento)
    VALUES (%(id)s, %(rut)s, %(nombre)s, %(apellido)s, %(email)s, %(fecha_nacimiento)s)
    """,
    {'id': 1, 'rut': 196469060, 'nombre': "Lucas", 'apellido': "Moreno", 'email': "lucas.moreno@gmail.com", 'fecha_nacimiento': "08/04/1997"}
    )
session.execute(
    """
    INSERT INTO paciente (id, rut, nombre, apellido, email, fecha_nacimiento)
    VALUES (%(id)s, %(rut)s, %(nombre)s, %(apellido)s, %(email)s, %(fecha_nacimiento)s)
    """,
    {'id': 2, 'rut': 191293718, 'nombre': "Ignacio", 'apellido': "Boetcher", 'email': "boetcher.ignacio@gmail.com", 'fecha_nacimiento': "01/11/1997"}
    )
session.execute(
    """
    INSERT INTO paciente (id, rut, nombre, apellido, email, fecha_nacimiento)
    VALUES (%(id)s, %(rut)s, %(nombre)s, %(apellido)s, %(email)s, %(fecha_nacimiento)s)
    """,
    {'id': 3, 'rut': 193423483, 'nombre': "Cristian", 'apellido': "Villavicencio", 'email': "Criss.Villa@gmail.com", 'fecha_nacimiento': "22/07/1997"}
    )
session.execute(
    """
    INSERT INTO paciente (id, rut, nombre, apellido, email, fecha_nacimiento)
    VALUES (%(id)s, %(rut)s, %(nombre)s, %(apellido)s, %(email)s, %(fecha_nacimiento)s)
    """,
    {'id': 4, 'rut': 203249283, 'nombre': "Diego", 'apellido': "Lagos", 'email': "diego.lagos@gmail.com", 'fecha_nacimiento': "15/07/1997"}
    )
session.execute(
    """
    INSERT INTO paciente (id, rut, nombre, apellido, email, fecha_nacimiento)
    VALUES (%(id)s, %(rut)s, %(nombre)s, %(apellido)s, %(email)s, %(fecha_nacimiento)s)
    """,
    {'id': 5, 'rut': 196868943, 'nombre': "Iman", 'apellido': "Jarufe", 'email': "iman.jarufe@gmail.com", 'fecha_nacimiento': "14/10/1997"}
    )


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return 

@app.route('/create', methods=['GET', 'POST'])
def home():
    session.execute(
    """
    INSERT INTO receta (id, id_paciente, comentario, farmacos, doctor)
    VALUES (%(id)s, %(id_paciente)s, %(comentario)s, %(farmacos)s, %(doctor)s)
    """,
    {'id':1,'id_paciente':1, 'comentario':" uno por dia, tomar despues del desayuno, los efectos duran aproximadamente 8 horas", 'farmacos':"Samexid 50mg", 'doctor': "Yuri Dragcnic" }
)
    return 

@app.route('/edit', methods=['GET', 'POST'])
def home():
    return

@app.route('/delete', methods=['GET', 'POST'])
def home():
    return 