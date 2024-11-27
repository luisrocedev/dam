console.log("Soy el JS de la cabecera")
let secciones = [
	'Store',
	'iMac',
	'iPad',
	'iPhone',
	'xxx',
	'yyy',
	'zzz'
	]
let cabecera = document.querySelector("header nav ul")
let plantilla = document.querySelector("#elementomenu")
secciones.forEach(function(seccion){
	let instancia = plantilla.content.cloneNode(true);
	instancia.querySelector("a").textContent = seccion
	cabecera.appendChild(instancia)
})
