<?php
	include "jocarsa | navy.php";
	$markdownFile = "muestra.md";
	$markdownContent = file_get_contents($markdownFile);
	$htmlContent = markdownToHtml($markdownContent);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Conversión Markdown a HTML</title>
</head>
<body>
<?php
echo $htmlContent;
?>
</body>
</html>
