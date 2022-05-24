# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', ésta carpeta está dedicada a la tarea 2. La solución está compuesta de 2 partes, primero que todo está el lado del usuario o productor, que está compuesto principalmente por la API(APIproducer.py), ésta llama al productor (Producer.py) el cual obtiene una dupla de login aleatoria desde un par de archivos (credencialesRandomID.json, credencialesRandomPass.json) mediante el llamado del archivo login.py, una vez introducida la dupla aleatoria se envía mediante Kafka. Desde el otro lado está la parte del consumidor esperando desde la aplicación APIbasededatos.py, una vez acá llama a la función consumermain del archivo consumer.py la cual se mantiene en espera a recibir los logins, cuando se recibe un login esta llama al archivo verificador.py el cual revisa si un ID está bloqueado mediante la consulta del json blocked.json, si está bloqueado se notifica al usuario. en paralelo está corriendo la función seguridad() la cual guarda cada dato enviado en un log llamado BDD_logs.json, si hay 5 intentos de la misma ID dentro del mismo minuto, este se bloquea.

# ¿Como ejecutar?
Entrar en una consola y ejecutar el comando 'docker-compose up'. Se deberían crear dos contenedores 'Consumer' y 'Producer', ejecutar primero el contenedor 'Consumer' y luego 'Producer' enviará logins aleatorios.

# Preguntas Tarea
1- ¿Por qué Kafka funciona bien en este escenario?

Primero por que tiene un mecanismo de organización y orden de mensajes integrado, el cual permite analizar más facilmente los accesos y determinar si una cuenta debe ser bloqueada. Otra razón es que tiene integrada una función de retención temporal de la información (parecida al comportamiento de un caché) junto con politicas de remonición personalizables, lo cual para esta tarea permite asegurar que los accesos se mantenga por el minuto requerido.

2- Basado en tecnologías que usted tiene a su disposición (Kafka, backend) ¿Que haría usted para manejar una gran cantidad de usuarios al mismo tiempo?

Gracias a que los brokers de Kafka están compuestos de una red de intermediarios, se puede aumentar esta red y así escalar horizontalmente sin problema. Además cada categoría Topic en Kafka están particionados, permitiendo escalar mediante réplicas en varios servidores.