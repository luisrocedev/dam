window.onload = function(){													// Cuando la ventana haya cargado
	console.log("Javascript está preparado para la acción")
	fetch("http://localhost:5000/damearticulos")							// Me conecto al servidor
	.then(function(response){													// Cuando el servidor responda
		return response.json()													// Lo que me responda lo interpreto como json
	})
	.then(function(datos){														// Cuando la interpretación haya sido realizada
		console.log(datos)														// En la consola ponme los datos
		let contenedor = document.querySelector("#blog .articulos")
		datos.forEach(function(dato){											// Para cada uno de los datos
			contenedor.innerHTML += `
				<article>
					<img src="imagenes/portfolio.jpg">
					<h5>`+dato.titulo+`</h5>
					<time>`+dato.fecha+`</time>
					<p>`+dato.texto+`</p>
				</article>
			`;																			// Devuelvo el resultado al contenedor
		})
	})
}
