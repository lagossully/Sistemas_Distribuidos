# Sistemas_Distribuidos
# Sistemas_Distribuidos

# Acerca del proyecto:
este proyecto trata acera de generar un sistema distribuido para un buscador dentro de una tienda, usando Redis para generar cache y aplicando como politica de remocion el algoritmo de Least Frequently Used(LFU), ademas de un Time To Live(TTL) de 3 horas, reduciendo de esta maner el tiempo de busqueda para las consultas mas frecuentes dado que son respondidas por cache, lo que toma significativamente menos tiempo que hacer consultas a la base de datos, asi mismo tambien reducir la carga del servidor principal en el que se encuentra la base de datos de la tienda, la comunicacion entre el buscador(Cliente) y la base de datos(Servidor) es producida a traves de Google Remote Procedure Call(grpc) y asi llamar desde el cliente a que el servidor utilice su proceso de manera remota.

# inizializando
Para esta aplicación idealmente se debe montar los dockers con el docker compose, pero como no se tuvo el tiempo suficiente se debe instalar python

# Uso 
Para utilizar esta aplicación se debe correr API.py, y modificar todo desde la consola
