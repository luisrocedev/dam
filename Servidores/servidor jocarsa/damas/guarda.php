<?php
	$myfile = fopen("tablero.html", "w") or die("Unable to open file!");
	$txt = $_GET['datos'];
	fwrite($myfile, $txt);
	fclose($myfile);
	echo "ok";
?>
