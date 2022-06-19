const cassandra = require('cassandra-driver');
const express = require('express')


//const client1 = new cassandra.Client({
//    contactPoints: ['cassandra-node1', 'cassandra-node2'],
//    localDataCenter: 'datacenter1',
//    keyspace: 'cassandra_keyspace1',
//    authProvider: new cassandra.auth.PlainTextAuthProvider('cassandra', 'cassandra')
//  });

const contactPoints = ['127.0.0.1'];

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