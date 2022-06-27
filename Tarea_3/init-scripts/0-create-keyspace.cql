-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS Cass WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '2' };
