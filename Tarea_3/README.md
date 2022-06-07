# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', ésta carpeta está dedicada a la tarea 3. La solución está compuesta de ##### partes, 

# ¿Como ejecutar?
Entrar en una consola y ejecutar el comando 'docker-compose up'. Se debería #############

# Preguntas Tarea
1-Explique la arquitectura que Cassandra maneja. Cuando se crea el cluster ¿Cómo los nodos se conectan? ¿Qué ocurre cuando un cliente realiza una petición a uno de los nodos? ¿Qué ocurre cuando uno de los nodos se desconecta? ¿La red generada entre los nodos siempre es eficiente? ¿Existe balanceo de carga?

Cassandra tiene una arquitectura cluster tipo anillo (con los nodos distribuidos lógicamente en un loop), está diseñado sin nodo tipo maestro/esclavo. Con los datos distribuidos automáticamente por todos los nodos para tener redundancia mediante llaves hasheadas. Soporta múltiples anillos (centros de datos) y conexión entre ellos.
Cuando se crea un cluster, los nodos se reconocen mediante una IP local. Se debe configurar el archivo cassandra.yaml en listen_address para lograr esto. #####.
Cuando se realiza una petición desde un cliente, el nodo al que se está conectando se convierte en el coordinador de la transacción con el cliente, luego se hace la query solicitada. El nodo coordinador decide que nodos reciben la query.
En el caso de que un nodo se desconecte, ### https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/architecture/archDataDistributeFailDetect.html


2- Cassandra posee principalmente dos estrategias para mantener redundancia en la replicación de datos. ¿Cuáles son estos? ¿Cuál es la ventaja de uno sobre otro? ¿Cuál utilizaría usted para en el caso actual y por qu ́e? Justifique apropiadamente su respuesta.

##############################

3-Teniendo en cuenta el contexto del problema ¿Usted cree que la soluci ́on propuesta es la correcta? ¿Qué ocurre cuando se quiere escalar en la solución? ¿Qué mejoras implementaría? Oriente su respuesta hacia el Sharding (la replicación/distribución de los datos) y comente una estrategia que podría seguir para ordenar los datos.

###################################