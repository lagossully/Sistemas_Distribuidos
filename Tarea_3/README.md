# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', ésta carpeta está dedicada a la tarea 3. La solución está compuesta de 4 partes (contenedores):
- El primero es un contenedor llamado backendpython el cual es una API que se monta gracias al script Python API.py (ver para referencia del funcionamiento), este se mantiene en espera gracias a Flask, espera los métodos POST y GET, tiene 3 métodos: 1- el método /create crea una receta aleatoria. 2- el método /edit edita una receta y cambia el comentario por "se extiende la receta por 7 días más". 3- el método /delete elimina la receta del último ID. Finalmente este contenedor se conecta al primer nodo de Apache Cassandra.
- Los otros contenedores son nodos de Apache Cassandra que se comunican entre si. Estos se encargan de guardar los datos ingresados por el cliente. El nodo 1 crea el keyspace, las tablas y rellena estas con unos cuantos datos.

# ¿Como ejecutar?
Entrar en una consola y ejecutar el comando 'docker-compose up'. Se deberían crear los 4 nodos anteriormente mencionados.
Abrir un navegador y acceder a las siguientes direcciones para hacer sus funciones:
- `localhost:5555/create` crea una receta para un paciente aleatorio
- `localhost:5555/edit` cambia el valor específico 'comentario' de una receta de un paciente aleatorio
- `localhost:5555/delete` borra una receta con un id aleatorio

# Preguntas Tarea
1-Explique la arquitectura que Cassandra maneja. Cuando se crea el cluster ¿Cómo los nodos se conectan? ¿Qué ocurre cuando un cliente realiza una petición a uno de los nodos? ¿Qué ocurre cuando uno de los nodos se desconecta? ¿La red generada entre los nodos siempre es eficiente? ¿Existe balanceo de carga?

- Cassandra tiene una arquitectura cluster tipo anillo (con los nodos distribuidos lógicamente en un loop), está diseñado con nodos que no tienen tipo maestro/esclavo, si no que están conectados como peer-to-peer. Con los datos distribuidos automáticamente por todos los nodos para tener redundancia mediante llaves hasheadas. Soporta múltiples anillos (centros de datos) o racks (grupos de nodos dentro del anillo) y conexión entre ellos. Cuando se crea un cluster, los nodos se reconocen mediante una IP local. Se debe configurar el archivo cassandra.yaml en listen_address para lograr esto.
- Cuando se realiza una petición desde un cliente, el nodo al que se está conectando se convierte en el coordinador de la transacción con el cliente, luego se hace la query. Para buscar los datos, el nodo coordinador decide que nodos reciben la query.
- En el caso de que un nodo se desconecte, si existe un factor de réplica mayor a 1, el nodo con la información replicada sustituye en funciones al desconectado.
- La red generada en los nodos no siempre es eficiente por que el anillo no asegura que los datos sean encontrados inmediatamente, dependiendo de la query se puede buscar los datos por un tiempo.
- No existe balanceo de carga en su estado base, para esto se utilizan otras técnicas como las particiones. La partición aleatoria si tiene un balanceo de carga, en cambio la partición con preservación de orden puede ser cargada muy hacia unas claves específicas y no termina siendo con carga balanceada.

2- Cassandra posee principalmente dos estrategias para mantener redundancia en la replicación de datos. ¿Cuáles son estos? ¿Cuál es la ventaja de uno sobre otro? ¿Cuál utilizaría usted para en el caso actual y por qué? Justifique apropiadamente su respuesta.

- Cassandra tiene 2 estratégias de replicación, Simple Strategy y NetworkTopology Strategy. Simple Strategy coloca réplicas de datos en un nodo seleccionado y luego en los nodos adyacentes a este en el anillo, se usa para un solo datacenter o rack. NetworkTopology Strategy se utiliza cuando los datos tienen que estar en múltiples centros de datos, específicando cuantas réplicas se requiere en cada datacenter, intenta guardar réplicas en racks distintos por si falla un rack entero.

- Para el caso actual, se recomienda utilizar la estrategia Simple Strategy ya que se utiliza solo un contenedor con 3 nodos y no se necesita más complejidad de replicación que simple strategy.

3-Teniendo en cuenta el contexto del problema ¿Usted cree que la soluci ́on propuesta es la correcta? ¿Qué ocurre cuando se quiere escalar en la solución? ¿Qué mejoras implementaría? Oriente su respuesta hacia el Sharding (la replicación/distribución de los datos) y comente una estrategia que podría seguir para ordenar los datos.

- Se cree que la solución es bastante acertada para la tarea, ya que son pocas tablas y nodos.
- Si se quiere escalar se va a encontrar con problemas de rendimiento, en este caso la solución podría ser mejor.
- Los cambios propuestos son 1-distribuir los datos de mejor forma, en varios racks y con replicación en varios racks (de forma NetworkTopology Strategy) para evitar la carga y peligro de pérdida del centro. 2-Si los datos son muy complejos se aconseja utilizar sharding del tipo aleatoria, ya que genera un balanceo de carga natural.


# Detalles No solucinados

- El nodo 1 de cassandra corre bien entre 30 segundos y un minuto y se cae. 

- La Coneccion entre Cluster y script esta incompleta, hubo errores que no se pudieron solucionar, pero los comandos segun la documentacion de la libreria cassandra-driver esta bien.
