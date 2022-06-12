from tkinter.tix import Form
import flask
from flask import Flask, request, redirect, render_template, jsonify, make_response
import json
from datetime import datetime
from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'],port=3000)
session = cluster.connect('cityinfo',wait_for_all_pools=True)
session.execute('USE cityinfo')
rows = session.execute('SELECT * FROM users')
for row in rows:
    print(row.age,row.name,row.username)


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