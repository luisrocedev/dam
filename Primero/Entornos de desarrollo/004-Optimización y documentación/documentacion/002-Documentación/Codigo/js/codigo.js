window.onload = function () {
  console.log("La web está preparada...");

  fetch("./json/web.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (datos) {
      console.log(datos);

      // Cabecera
      if (document.querySelector("header h1")) {
        document.querySelector("header h1").textContent = datos.cabecera.titulo;
      }
      if (document.querySelector("header h2")) {
        document.querySelector("header h2").textContent = datos.cabecera.subtitulo;
      }
      datos.cabecera.menu.forEach((item, index) => {
        const menuItem = document.querySelector(`header nav a:nth-child(${index + 1})`);
        if (menuItem) {
          menuItem.textContent = item;
        }
      });
      if (document.querySelector("header button")) {
        document.querySelector("header button").textContent = datos.cabecera.boton;
      }

      // Heroe
      if (document.querySelector("#heroe h4")) {
        document.querySelector("#heroe h4").textContent = datos.heroe.titulo;
      }
      if (document.querySelector("#heroe h3")) {
        document.querySelector("#heroe h3").textContent = datos.heroe.subtitulo;
      }
      if (document.querySelector("#heroe p")) {
        document.querySelector("#heroe p").textContent = datos.heroe.texto;
      }
      if (document.querySelector("#heroe button")) {
        document.querySelector("#heroe button").textContent = datos.heroe.boton1;
      }
      if (document.querySelector("#heroe .secundario")) {
        document.querySelector("#heroe .secundario").textContent = datos.heroe.boton2;
      }

      // Sobre mi
      if (document.querySelector("#sobremi h4")) {
        document.querySelector("#sobremi h4").textContent = datos.sobremi.subtitulo;
      }
      if (document.querySelector("#sobremi h3")) {
        document.querySelector("#sobremi h3").textContent = datos.sobremi.titulo;
      }
      if (document.querySelector("#sobremi p")) {
        document.querySelector("#sobremi p").textContent = datos.sobremi.texto;
      }
      if (document.querySelector("#sobremi .firma")) {
        document.querySelector("#sobremi .firma").textContent = datos.sobremi.firma;
      }
      if (document.querySelector("#sobremi button")) {
        document.querySelector("#sobremi button").textContent = datos.sobremi.boton;
      }

      // Calificaciones
      if (document.querySelector("#calificaciones h4")) {
        document.querySelector("#calificaciones h4").textContent = datos.calificaciones.subtitulo;
      }
      if (document.querySelector("#calificaciones h3")) {
        document.querySelector("#calificaciones h3").textContent = datos.calificaciones.titulo;
      }

      // Columna 1 (Educación)
      if (document.querySelector("#col1 h6")) {
        document.querySelector("#col1 h6").textContent = datos.calificaciones.columna1.titulo;
      }
      datos.calificaciones.columna1.elementos.forEach((elemento, index) => {
        const article = document.querySelector(`#col1 article:nth-of-type(${index + 1})`);
        if (article) {
          article.querySelector("h5").textContent = elemento.titulo;
          article.querySelector("a").textContent = elemento.enlace;
          article.querySelector("p").textContent = elemento.tiempo;
        }
      });

      // Columna 2 (Experiencia)
      if (document.querySelector("#col2 h6")) {
        document.querySelector("#col2 h6").textContent = datos.calificaciones.columna2.titulo;
      }
      datos.calificaciones.columna2.elementos.forEach((elemento, index) => {
        const article = document.querySelector(`#col2 article:nth-of-type(${index + 1})`);
        if (article) {
          article.querySelector("h5").textContent = elemento.titulo;
          article.querySelector("a").textContent = elemento.enlace;
          article.querySelector("p").textContent = elemento.tiempo;
        }
      });

      // Columna 3 (Habilidades)
      if (document.querySelector("#col3 h6")) {
        document.querySelector("#col3 h6").textContent = datos.calificaciones.columna3.titulo;
      }
      const habilidadesList = document.querySelector("#col3 ul");
      if (habilidadesList) {
        habilidadesList.innerHTML = ""; // Clear existing items
        datos.calificaciones.columna3.habilidades.forEach((habilidad) => {
          const li = document.createElement("li");
          li.textContent = habilidad;
          habilidadesList.appendChild(li);
        });
      }

      // Servicios
      if (document.querySelector("#servicios h4")) {
        document.querySelector("#servicios h4").textContent = datos.servicios.subtitulo;
      }
      if (document.querySelector("#servicios h3")) {
        document.querySelector("#servicios h3").textContent = datos.servicios.titulo;
      }
      datos.servicios.items.forEach((servicio, index) => {
        const article = document.querySelector(`#servicios article:nth-of-type(${index + 1})`);
        if (article) {
          article.querySelector("h5").textContent = servicio.titulo;
          article.querySelector("p").textContent = servicio.descripcion;
          article.querySelector("a").textContent = servicio.enlace;
        }
      });

      // Proyectos
      if (document.querySelector("#proyectos h4")) {
        document.querySelector("#proyectos h4").textContent = datos.proyectos.subtitulo;
      }
      if (document.querySelector("#proyectos h3")) {
        document.querySelector("#proyectos h3").textContent = datos.proyectos.titulo;
      }
      if (document.querySelector("#proyectos p")) {
        document.querySelector("#proyectos p").textContent = datos.proyectos.descripcion;
      }
      datos.proyectos.botones.forEach((boton, index) => {
        const buttonElement = document.querySelector(`#proyectos .botones button:nth-of-type(${index + 1})`);
        if (buttonElement) {
          buttonElement.textContent = boton;
        }
      });
      datos.proyectos.items.forEach((proyecto, index) => {
        const article = document.querySelector(`#proyectos .articulos article:nth-of-type(${index + 1})`);
        if (article) {
          article.querySelector("img").src = `imagenes/${proyecto.imagen}`;
          article.querySelector("h5").textContent = proyecto.titulo;
          article.querySelector("p").textContent = proyecto.descripcion;
        }
      });
      if (document.querySelector("#proyectos button")) {
        document.querySelector("#proyectos button").textContent = datos.proyectos.boton;
      }

      // Testimonios
      if (document.querySelector("#testimonios .imagen img")) {
        document.querySelector("#testimonios .imagen img").src = `imagenes/${datos.testimonios.imagen}`;
      }
      if (document.querySelector("#testimonios h4")) {
        document.querySelector("#testimonios h4").textContent = datos.testimonios.titulo;
      }
      if (document.querySelector("#testimonios h3")) {
        document.querySelector("#testimonios h3").textContent = datos.testimonios.subtitulo;
      }
      if (document.querySelector("#testimonios p")) {
        document.querySelector("#testimonios p").textContent = datos.testimonios.texto;
      }
      if (document.querySelector("#testimonios .firma")) {
        document.querySelector("#testimonios .firma").textContent = datos.testimonios.firma;
      }
      if (document.querySelector("#testimonios button")) {
        document.querySelector("#testimonios button").textContent = datos.testimonios.boton;
      }

      // Blog
      if (document.querySelector("#blog h4")) {
        document.querySelector("#blog h4").textContent = datos.blog.titulo;
      }
      if (document.querySelector("#blog h3")) {
        document.querySelector("#blog h3").textContent = datos.blog.subtitulo;
      }
      datos.blog.items.forEach((articulo, index) => {
        const article = document.querySelector(`#blog .articulos article:nth-of-type(${index + 1})`);
        if (article) {
          article.querySelector("img").src = `imagenes/${articulo.imagen}`;
          article.querySelector("h5").textContent = articulo.titulo;
          article.querySelector("p").textContent = articulo.descripcion;
        }
      });
      if (document.querySelector("#blog button")) {
        document.querySelector("#blog button").textContent = datos.blog.boton;
      }

      // Contacto
      if (document.querySelector("#contacto h4")) {
        document.querySelector("#contacto h4").textContent = datos.contacto.titulo;
      }
      if (document.querySelector("#contacto h3")) {
        document.querySelector("#contacto h3").textContent = datos.contacto.subtitulo;
      }
      if (document.querySelector("#contacto form input[placeholder='Tu nombre']")) {
        document.querySelector("#contacto form input[placeholder='Tu nombre']").placeholder = datos.contacto.formulario.nombre;
      }
      if (document.querySelector("#contacto form input[placeholder='Tu email']")) {
        document.querySelector("#contacto form input[placeholder='Tu email']").placeholder = datos.contacto.formulario.email;
      }
      if (document.querySelector("#contacto form input[placeholder='Asunto']")) {
        document.querySelector("#contacto form input[placeholder='Asunto']").placeholder = datos.contacto.formulario.asunto;
      }
      if (document.querySelector("#contacto form textarea")) {
        document.querySelector("#contacto form textarea").placeholder = datos.contacto.formulario.mensaje;
      }
      if (document.querySelector("#contacto form button")) {
        document.querySelector("#contacto form button").textContent = datos.contacto.formulario.boton;
      }
      if (document.querySelector("#contacto iframe")) {
        document.querySelector("#contacto iframe").src = datos.contacto.mapa.url;
        document.querySelector("#contacto iframe").width = datos.contacto.mapa.ancho;
        document.querySelector("#contacto iframe").height = datos.contacto.mapa.alto;
      }

      // Footer
      if (document.querySelector("footer h3")) {
        document.querySelector("footer h3").textContent = datos.footer.titulo;
      }
      if (document.querySelector("footer p:nth-of-type(1)")) {
        document.querySelector("footer p:nth-of-type(1)").textContent = datos.footer.email;
      }
      if (document.querySelector("footer p:nth-of-type(2)")) {
        document.querySelector("footer p:nth-of-type(2)").textContent = datos.footer.telefono;
      }
      datos.footer.redes.forEach((red, index) => {
        const img = document.querySelector(`footer img:nth-of-type(${index + 1})`);
        if (img) {
          img.src = `imagenes/${red.icono}`;
          img.parentElement.href = red.url;
        }
      });
      if (document.querySelector("footer p:last-of-type")) {
        document.querySelector("footer p:last-of-type").textContent = datos.footer.copyright;
      }
    });
};

