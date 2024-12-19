<?php

	$servidor = "localhost";				// Defino el servidor
	$usuario = "oldlace";			// Defino el usuario con permiso
	$contrasena = "oldlace";		// Defino la contraseña de ese usuario
	$base = "oldlace";				// Defino la base de datos

	$conexion = new mysqli(
		$servidor, 
		$usuario, 
		$contrasena, 
		$base
	);												// Creo una conexión de tipo MySQL

?>
