onmessage = function(datos){                                 // El worker escucha
    console.log("Hola soy el núcleo",datos.data)
    /*
    let numero = 1.0000000054;
      let iteraciones = 10000000000;
      for(let i = 0;i<iteraciones;i++){
        numero *= 1.000000000076;
      }
    postMessage("ok soy el worker y vuelvo al proceso principal")       // Devuelve un mensaje al hilo principal
    */
}
