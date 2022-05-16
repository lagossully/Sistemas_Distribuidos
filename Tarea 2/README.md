# Sistemas_Distribuidos

# Acerca del proyecto:
Este proyecto es hecho por Diego Lagos y Lucas Peñailillo para el ramo 'Sistemas Distribuidos', esta carpeta está dedicada a la tarea 2.

# Preguntas Tarea
1- ¿Por qué Kafka funciona bien en este escenario?

Primero por que tiene un mecanismo de organización y orden de mensajes integrado, el cual permite analizar más facilmente los accesos y determinar si una cuenta debe ser bloqueada. Otra razón es que tiene integrada una función de retención temporal de la información (parecida al comportamiento de un caché) junto con politicas de remonición personalizables, lo cual para esta tarea permite asegurar que los accesos se mantenga por el minuto requerido.

2- Basado en tecnologías que usted tiene a su disposición (Kafka, backend) ¿Que haría usted para manejar una gran cantidad de usuarios al mismo tiempo?

Gracias a que los brokers de Kafka están compuestos de una red de intermediarios, se puede aumentar esta red y así escalar horizontalmente sin problema. Además cada categoría Topic en Kafka están particionados, permitiendo escalar mediante réplicas en varios servidores.