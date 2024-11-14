<!doctype html>
<html>
	<head>
		<style>
			body,html{
				background:grey;
			}
			header,main,footer{
				width:800px;
				padding:20px;
				margin:auto;
				background:white;
			}
		</style>
	</head>
	<body>
		<header>
			<h1>Blog</h1>
			<h2>El blog de Jose Vicente</h2>
		</header>
		<main>
			<?php
				include "conexionbasedatos.php";
			?>
		</main>
		<footer>
			<h6>(c) 2024 Jose Vicente Carratala</h6>
		</footer>
	</body>
</html>
