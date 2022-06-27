from re import A
import flask as F
from flask import Flask, request, redirect, render_template, jsonify, make_response
import json
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import random
import os
import socket

def isOpen(ip, port):
   test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      test.connect((ip, int(port)))
      test.shutdown(1)
      return True
   except:
      return False

def fakeLoadBalancer():
    ips = []
    port = 9042
    for ip in os.environ.get('CASSANDRA_SEEDS').split(','):
        if isOpen(ip, port):
            ips.append(ip)
    return ips
def ConectCassandraCluster():
    nodos = ['cassandra_node_1', 'cassandra_node_2', 'cassandra_node_3']
    port = 9042
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(contact_points=nodos, port=port, auth_provider= auth_provider)
    session = cluster.connect()
    session.execute('USE Cass')
    print(session.execute('SELECT * FROM paciente'))
    return session

app = F.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def cassandra():
    cluster = Cluster(fakeLoadBalancer(), port=9042, auth_provider=PlainTextAuthProvider(username='cassandra', password=os.environ.get('CASSANDRA_PASSWORD')))
    session = cluster.connect('Cass', wait_for_all_pools=False)
    session.execute('USE Cass')
    result = session.execute('SELECT * FROM paciente')
    rows = {}
    for row in result:
        rows[row.id] = row.name
    app.logger.info(rows)
    return rows
    

@app.route('/create', methods=['GET', 'POST'])
def home():
    cluster = Cluster(fakeLoadBalancer(),port=9042, auth_provider=PlainTextAuthProvider(username='cassandra', password=os.environ.get('CASSANDRA_PASSWORD')))
    session = cluster.connect('Cass', wait_for_all_pools=False)
    session.execute('USE Cass')
    IdsDisponibles = [1, 2, 3, 4, 5]
    RandomID = random.choice(IdsDisponibles)

    session.execute(
    """
    INSERT INTO receta (id, id_paciente, comentario, farmacos, doctor)
    VALUES (%(id)s, %(id_paciente)s, %(comentario)s, %(farmacos)s, %(doctor)s)
    """,
    {'id':1,'id_paciente':RandomID, 'comentario':" uno por dia, tomar despues del desayuno, los efectos duran aproximadamente 8 horas", 'farmacos':"Samexid 50mg", 'doctor': "Yuri Dragcnic" }
    )
    return 

@app.route('/edit', methods=['GET', 'POST'])
def editar():
    cluster = Cluster(fakeLoadBalancer(),port=9042, auth_provider=PlainTextAuthProvider(username='cassandra', password=os.environ.get('CASSANDRA_PASSWORD')))
    session = cluster.connect('Cass', wait_for_all_pools=False)
    session.execute('USE Cass')
    IdsDisponibles = [1, 2, 3, 4, 5]
    RandomID = random.choice(IdsDisponibles)

    session.execute(
    """
    update receta set comentario=%s where id_paciente = %s
    
    """,
    {'se extiende la receta por 7 días más',RandomID}
    
    )

    return

@app.route('/delete', methods=['GET', 'POST'])
def eliminar():
    cluster = Cluster(fakeLoadBalancer(),port=9042, auth_provider=PlainTextAuthProvider(username='cassandra', password=os.environ.get('CASSANDRA_PASSWORD')))
    session = cluster.connect('Cass', wait_for_all_pools=False)
    session.execute('USE Cass')
    IdsDisponibles = [1, 2, 3, 4, 5]
    RandomID = random.choice(IdsDisponibles)

    session.execute(
    """
    DELETE FROM receta WHERE id = %s
    
    """,
    {'se extiende la receta por 7 días más',RandomID}
    
    )
    return 

session = ConectCassandraCluster()
if __name__=='__main__':
      app.run(debug=True,host='0.0.0.0',port=5555)