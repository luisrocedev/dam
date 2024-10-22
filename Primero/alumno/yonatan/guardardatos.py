'''
PROGRAMA AGENDA CON PICKLE
POR YONATAN MORA RUIZ (C)
'''
import pickle
class Libro:
    def __init__(self,nuevo_autor,nuevo_titulo,nuevo_año,nuevo_genero):
        self.autor  = nuevo_autor
        self.titulo = nuevo_titulo
        self.año    = nuevo_año
        self.genero = nuevo_genero

libreria = []
while(True):

    print("*****Bienvenido a tu programa biblioteca de libros*****")
    print("            --Menu de inicio--")

    print("1• Insertar un nuevo LIBRO")
    print("2• guardar los libros")
    print("3• vamos a listar los libros insertados")
    print("4• leer los registro guardados")
    print("5• salir del programa")
    opcion = input("selecciona una de las opciones: ")
    print("has selecionado la opcion",opcion)

    if opcion ==   "1":

        print("vamos a insertar un nuevo libro.")
        autor   = input("Introduce el nombre del Autor :") #INTRODUCE DATOS
        titulo  = input("Introduce el titulo del libro: ")
        año     = input("introduce el año de lanzamiento: ")
        genero  = input("Introduce el genero del libro: ")
        nuevo_libro = Libro(autor,titulo,año,genero) #CREO VARIABLE DE TO DO LO NUEVO QUE ES = A LA CLASE + (DATOS)
        libreria.append(nuevo_libro)#LUEGO ELIJO DONDE SE GUARDAN ESOS DATOS QUE SE GUARDAN EN LA LIBRERIA []+APPEND 

    elif opcion == "3":

        print("vamos a listar los libros insertados.")
        for Libro in libreria:#para clase en libreria
            print("-------------------------------------------")
            print("nombre del autor:",         Libro.autor)
            print("titulo del libro:",         Libro.titulo)
            print("año del libro:",            Libro.año)
            print("el genero del libro es:",   Libro.genero)
            print("------------------------------------------")

    elif opcion == "2":

        print("vamos a GUARDAR los libros en archivo.")
        archivo = open("libreria.bin",'wb')                                       
        pickle.dump(libreria,archivo)                                             
        print("el registro a quedado guardado en un archivo")                      
        archivo.close()                             

                

    elif opcion == "4":
        print("vamos a LEER los libros en pantalla.")
        archivo = open("libreria.bin",'rb')                                       
        libreria = pickle.load(archivo)                                          
        archivo.close()                  

    elif opcion == "5":
        exit()
