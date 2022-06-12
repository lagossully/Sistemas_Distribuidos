# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', ésta carpeta está dedicada a la tarea 3. La solución está compuesta de ##### partes, 

# ¿Como ejecutar?
Entrar en una consola y ejecutar el comando 'docker-compose up'. Se debería #############

# Preguntas Tarea
1-Explique la arquitectura que Cassandra maneja. Cuando se crea el cluster ¿Cómo los nodos se conectan? ¿Qué ocurre cuando un cliente realiza una petición a uno de los nodos? ¿Qué ocurre cuando uno de los nodos se desconecta? ¿La red generada entre los nodos siempre es eficiente? ¿Existe balanceo de carga?

Cassandra tiene una arquitectura cluster tipo anillo (con los nodos distribuidos lógicamente en un loop), está diseñado sin nodo tipo maestro/esclavo. Con los datos distribuidos automáticamente por todos los nodos para tener redundancia mediante llaves hasheadas. Soporta múltiples anillos (centros de datos) o racks (grupos de nodos dentro del anillo) y conexión entre ellos.
Cuando se crea un cluster, los nodos se reconocen mediante una IP local. Se debe configurar el archivo cassandra.yaml en listen_address para lograr esto. #####.
Cuando se realiza una petición desde un cliente, el nodo al que se está conectando se convierte en el coordinador de la transacción con el cliente, luego se hace la query solicitada. El nodo coordinador decide que nodos reciben la query.
En el caso de que un nodo se desconecte, ### https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/architecture/archDataDistributeFailDetect.html
La red generada en los nodos no siempre es eficiente por que ####
No existe balanceo de carga en su estado base, para esto se utilizan otros implementos externos en la red.

2- Cassandra posee principalmente dos estrategias para mantener redundancia en la replicación de datos. ¿Cuáles son estos? ¿Cuál es la ventaja de uno sobre otro? ¿Cuál utilizaría usted para en el caso actual y por qu ́e? Justifique apropiadamente su respuesta.

Cassandra tiene 2 estratégias de replicación, Simple Strategy y NetworkTopology Strategy.
Simple Strategy coloca réplicas de datos en un nodo seleccionado y luego en los nodos adyacentes a este en el anillo, se usa para un solo datacenter o rack.
NetworkTopology Strategy se utiliza cuando los datos tienen que estar en múltiples centros de datos, específicando cuantas réplicas se requiere en cada datacenter, intenta guardas réplicas en racks distintos por si falla un rack entero, las réplicas. ###<- arreglar lo anterior de networktopology###
Para el caso actual, se recomienda utilizar la estrategia Simple Strategy ya que se utiliza solo un contenedor con 3 nodos y no se necesita más complejidad de replicación que simple strategy.

3-Teniendo en cuenta el contexto del problema ¿Usted cree que la soluci ́on propuesta es la correcta? ¿Qué ocurre cuando se quiere escalar en la solución? ¿Qué mejoras implementaría? Oriente su respuesta hacia el Sharding (la replicación/distribución de los datos) y comente una estrategia que podría seguir para ordenar los datos.

Se cree que la solución podría ser mejor, distribuyendo los datos de mejor forma, en varios racks y con replicación en varios racks (de forma NetworkTopology Strategy).
Para ordenar los datos ###################################