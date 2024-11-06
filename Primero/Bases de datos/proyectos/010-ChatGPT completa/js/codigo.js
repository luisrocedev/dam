window.onload = function() {
  console.log("La web está preparada...");

  fetch("./json/web.json")
    .then(function(response) {
      return response.json();
    })
    .then(function(datos) {
      console.log(datos);

      // Cabecera
      document.querySelector("header h1").textContent = datos.cabecera.titulo;
      document.querySelector("header h2").textContent = datos.cabecera.subtitulo;
      datos.cabecera.menu.forEach((item, index) => {
        document.querySelector(`header nav a:nth-child(${index + 1})`).textContent = item;
      });
      document.querySelector("header button").textContent = datos.cabecera.boton;

      // Heroe
      document.querySelector("#heroe h4").textContent = datos.heroe.titulo;
      document.querySelector("#heroe h3").textContent = datos.heroe.subtitulo;
      document.querySelector("#heroe p").textContent = datos.heroe.texto;
      document.querySelector("#heroe button").textContent = datos.heroe.boton1;
      document.querySelector("#heroe .secundario").textContent = datos.heroe.boton2;

      // Sobre mi
      document.querySelector("#sobremi h4").textContent = datos.sobremi.subtitulo;
      document.querySelector("#sobremi h3").textContent = datos.sobremi.titulo;
      document.querySelector("#sobremi p").textContent = datos.sobremi.texto;
      document.querySelector("#sobremi .firma").textContent = datos.sobremi.firma;
      document.querySelector("#sobremi button").textContent = datos.sobremi.boton;

      // Calificaciones
      document.querySelector("#calificaciones h4").textContent = datos.calificaciones.subtitulo;
      document.querySelector("#calificaciones h3").textContent = datos.calificaciones.titulo;

      // Columna 1 (Educación)
      document.querySelector("#col1 h6").textContent = datos.calificaciones.columna1.titulo;
      datos.calificaciones.columna1.elementos.forEach((elemento, index) => {
        const article = document.querySelector(`#col1 article:nth-child(${index + 1})`);
        article.querySelector("h5").textContent = elemento.titulo;
        article.querySelector("a").textContent = elemento.enlace;
        article.querySelector("p").textContent = elemento.tiempo;
      });

      // Columna 2 (Experiencia)
      document.querySelector("#col2 h6").textContent = datos.calificaciones.columna2.titulo;
      datos.calificaciones.columna2.elementos.forEach((elemento, index) => {
        const article = document.querySelector(`#col2 article:nth-child(${index + 1})`);
        article.querySelector("h5").textContent = elemento.titulo;
        article.querySelector("a").textContent = elemento.enlace;
        article.querySelector("p").textContent = elemento.tiempo;
      });

      // Columna 3 (Habilidades)
      document.querySelector("#col3 h6").textContent = datos.calificaciones.columna3.titulo;
      const habilidadesList = document.querySelector("#col3 ul");
      habilidadesList.innerHTML = ""; // Clear existing items
      datos.calificaciones.columna3.habilidades.forEach(habilidad => {
        const li = document.createElement("li");
        li.textContent = habilidad;
        habilidadesList.appendChild(li);
      });

      // Servicios
      document.querySelector("#servicios h4").textContent = datos.servicios.subtitulo;
      document.querySelector("#servicios h3").textContent = datos.servicios.titulo;
      datos.servicios.items.forEach((servicio, index) => {
        const article = document.querySelector(`#servicios article:nth-child(${index + 1})`);
        article.querySelector("h5").textContent = servicio.titulo;
        article.querySelector("p").textContent = servicio.descripcion;
        article.querySelector("a").textContent = servicio.enlace;
      });

      // Proyectos
      document.querySelector("#proyectos h4").textContent = datos.proyectos.subtitulo;
      document.querySelector("#proyectos h3").textContent = datos.proyectos.titulo;
      document.querySelector("#proyectos p").textContent = datos.proyectos.descripcion;
      datos.proyectos.botones.forEach((boton, index) => {
        document.querySelector(`#proyectos .botones button:nth-child(${index + 1})`).textContent = boton;
      });
      datos.proyectos.items.forEach((proyecto, index) => {
        const article = document.querySelector(`#proyectos .articulos article:nth-child(${index + 1})`);
        article.querySelector("img").src = `imagenes/${proyecto.imagen}`;
        article.querySelector("h5").textContent = proyecto.titulo;
        article.querySelector("p").textContent = proyecto.descripcion;
      });
      document.querySelector("#proyectos button").textContent = datos.proyectos.boton;

      // Testimonios
      document.querySelector("#testimonios .imagen img").src = `imagenes/${datos.testimonios.imagen}`;
      document.querySelector("#testimonios h4").textContent = datos.testimonios.titulo;
      document.querySelector("#testimonios h3").textContent = datos.testimonios.subtitulo;
      document.querySelector("#testimonios p").textContent = datos.testimonios.texto;
      document.querySelector("#testimonios .firma").textContent = datos.testimonios.firma;
      document.querySelector("#testimonios button").textContent = datos.testimonios.boton;

      // Blog
      document.querySelector("#blog h4").textContent = datos.blog.titulo;
      document.querySelector("#blog h3").textContent = datos.blog.subtitulo;
      datos.blog.items.forEach((articulo, index) => {
        const article = document.querySelector(`#blog .articulos article:nth-child(${index + 1})`);
        article.querySelector("img").src = `imagenes/${articulo.imagen}`;
        article.querySelector("h5").textContent = articulo.titulo;
        article.querySelector("p").textContent = articulo.descripcion;
      });
      document.querySelector("#blog button").textContent = datos.blog.boton;

      // Contacto
      document.querySelector("#contacto h4").textContent = datos.contacto.titulo;
      document.querySelector("#contacto h3").textContent = datos.contacto.subtitulo;
      document.querySelector("#contacto form input[placeholder='Tu nombre']").placeholder = datos.contacto.formulario.nombre;
      document.querySelector("#contacto form input[placeholder='Tu email']").placeholder = datos.contacto.formulario.email;
      document.querySelector("#contacto form input[placeholder='Asunto']").placeholder = datos.contacto.formulario.asunto;
      document.querySelector("#contacto form textarea").placeholder = datos.contacto.formulario.mensaje;
      document.querySelector("#contacto form button").textContent = datos.contacto.formulario.boton;
      document.querySelector("#contacto iframe").src = datos.contacto.mapa.url;
      document.querySelector("#contacto iframe").width = datos.contacto.mapa.ancho;
      document.querySelector("#contacto iframe").height = datos.contacto.mapa.alto;

      // Footer
      document.querySelector("footer h3").textContent = datos.footer.titulo;
      document.querySelector("footer p:nth-of-type(1)").textContent = datos.footer.email;
      document.querySelector("footer p:nth-of-type(2)").textContent = datos.footer.telefono;
      datos.footer.redes.forEach((red, index) => {
        const img = document.querySelector(`footer img:nth-child(${index + 1})`);
        img.src = `imagenes/${red.icono}`;
        img.parentElement.href = red.url;
      });
      document.querySelector("footer p:last-of-type").textContent = datos.footer.copyright;
    });
};

