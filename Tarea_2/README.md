# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', esta carpeta está dedicada a la tarea 2. La solución está compuesta de 3 partes, primero que todo está el lado del usuario, que está compuesto por la API(API.py), ésta llama al productor (Producer.py) el cual obtiene una dupla de login aleatoria desde un par de archivos (credencialesRandomID.json, credencialesRandomPass.json) mediante el archivo login.py. Una vez introducida la dupla aleatoria se consulta en un archivo (blocked.json) si la cuenta está bloqueada, si está bloqueada se le notifica al usuario, en el caso de que no lo esté pueden ocurrir dos cosas: 1- que las credenciales estén correctas, en este caso se le notifica al usuario el login. 2- que las credenciales estén incorrectas, en este caso se registran la hora de la consulta y el ID de la cuenta, si es el 5to intento que se produce en el mismo minuto la cuenta será bloqueada.

# ¿Como ejecutar?


# Preguntas Tarea
1- ¿Por qué Kafka funciona bien en este escenario?

Primero por que tiene un mecanismo de organización y orden de mensajes integrado, el cual permite analizar más facilmente los accesos y determinar si una cuenta debe ser bloqueada. Otra razón es que tiene integrada una función de retención temporal de la información (parecida al comportamiento de un caché) junto con politicas de remonición personalizables, lo cual para esta tarea permite asegurar que los accesos se mantenga por el minuto requerido.

2- Basado en tecnologías que usted tiene a su disposición (Kafka, backend) ¿Que haría usted para manejar una gran cantidad de usuarios al mismo tiempo?

Gracias a que los brokers de Kafka están compuestos de una red de intermediarios, se puede aumentar esta red y así escalar horizontalmente sin problema. Además cada categoría Topic en Kafka están particionados, permitiendo escalar mediante réplicas en varios servidores.