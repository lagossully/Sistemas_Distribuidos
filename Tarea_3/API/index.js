const cassandra = require('cassandra-driver');
const express = require('express')
const app = express();


var port = process.env.PORT || 3000;
var host = process.env.PORT || '0.0.0.0';
const contactPoints = ['127.0.0.1'];

const {
    v4: uuidv4
  } = require('uuid');

const client = new cassandra.Client({
    contactPoints: contactPoints,
    localDataCenter: 'datacenter1',
    keyspace: 'user_keyspace',
    authProvider: new cassandra.auth.PlainTextAuthProvider('cassandra', 'cassandra')
});

client.connect(function (err) {
    if (err) {
        console.log('Error in connnection: ', err); return;
    }
    console.log('Cassandra connected');
});