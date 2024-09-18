SELECT 
    nombre,
    apellidos,
    TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) AS edad
FROM 
    miempresa.clientes;
