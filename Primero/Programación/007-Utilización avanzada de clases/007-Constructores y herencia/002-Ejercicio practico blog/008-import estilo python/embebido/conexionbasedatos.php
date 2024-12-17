<?php
function dameArticulos(){
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(E_ALL);

	$conexion = mysqli_connect(
		"localhost", 
		"blog", 
		"blog", 
		"blog"
	);																						// Me conecto a la base de datos
	$peticion = "SELECT * FROM entradas;";										// Creo una petición
	$resultado = mysqli_query($conexion, $peticion);						// Ejecuto la petición contra el servidor																		// Creo un array vacio
	while($fila = mysqli_fetch_array($resultado, MYSQLI_ASSOC)){		// Para cada uno de los resultados
		echo 	'
			<article>
				<h3>'.$fila['titulo'].'</h3>
				<time>'.$fila['fecha'].'</time>
				<p>'.$fila['contenido'].'</p>
			</article>
		';
	}
}
?>
