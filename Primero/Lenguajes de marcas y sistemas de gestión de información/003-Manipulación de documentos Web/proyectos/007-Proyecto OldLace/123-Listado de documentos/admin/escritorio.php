<?php 
//include "error.php"
?>
<!doctype html>
<html>
	<head>
		<link rel="Stylesheet" href="estilo/escritorio.css">
	</head>
	<body>
		<header><h1>jocarsa | DarkSlateBlue</h1></header>
		<main>
			<nav>
				<ul>
					<li class="destacado">Tablas:</li>
					<?php include "inc/menu.php"?>
					<li class="destacado">Documentos:</li>
					<?php include "inc/listadodocumentos.php"?>
				</ul>
			</nav>
			<section>
				<?php include "inc/tabla.php"?>
				<?php include "inc/documentos.php"?>
				<?php include "inc/formulario.php"?>
			</section>
		</main>
		<script src="js/codigo.js"></script>
	</body>
</html>

