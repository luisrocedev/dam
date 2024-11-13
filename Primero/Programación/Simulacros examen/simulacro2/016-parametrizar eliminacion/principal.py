from funciones import *

while True:
    print("Escoge una opcion")
    print("1.-Listar los registros")
    print("2.-Insertar un registro")
    print("3.-Eliminar un registro")
    print("4.-Actualizar un registro")
    print("5.-Cerrar el programa")
    opcion = input("Escoge una opcion:")

    if opcion == "1":
        print(seleccionaCapitulo())
    elif opcion == "2":
        Titulo = input("Introduce el Titulo del capítulo:")         # Le pido un nuevo Titulo al usuario
        Subtitulo = input("Introduce el Subtitulo del capítulo:")   # Le pido un nuevo Subtitulo al usuario
        Imagen = input("Introduce el Imagen del capítulo:")         # Le pido un nuevo Imagen al usuario
        Video = input("Introduce el Video del capítulo:")           # Le pido un nuevo Video al usuario
        Texto = input("Introduce el Texto del capítulo:")           # Le pido un nuevo Texto al usuario
        print(insertaCapitulo(Titulo,Subtitulo,Imagen,Video,Texto))
    elif opcion == "3":
        Identificador = input("Introduce el Identificador del capítulo a eliminar:")         # Le pido un nuevo Titulo al usuario
        print(eliminaCapitulo(Identificador))
    elif opcion == "4":
        print(actualizaCapitulo())
    elif opcion == "5":
        conexion.close()
        break

print("El programa ha finalizado")

        
