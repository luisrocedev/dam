print("Mi querido diario, v 0.1")

fecha = input("Introduce la fecha de la entrada:")
mensaje = input("Introduce lo que quieres guardar en tu diario:")

archivo = open("miqueridodiario.txt",'a')

archivo.write(fecha+"|"+mensaje+"\n")

archivo.close()
