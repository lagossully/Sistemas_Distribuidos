use Cass;
create table paciente (id int, rut int, nombre text, apellido text, email text, fecha_nacimiento text, PRIMARY KEY (rut));
create table receta (id int,id_paciente int, comentario text, farmacos text, doctor text, PRIMARY KEY (id_paciente));