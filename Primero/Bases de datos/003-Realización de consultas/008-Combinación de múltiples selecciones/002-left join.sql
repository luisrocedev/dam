SELECT * FROM empleados
LEFT JOIN direcciones
ON empleados.Identificador = direcciones.empleados_nombre;


