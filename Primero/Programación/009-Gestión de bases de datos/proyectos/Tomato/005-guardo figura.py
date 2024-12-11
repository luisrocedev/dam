import matplotlib.pyplot as plt
import psutil

carga = psutil.cpu_percent(interval=1)
print(carga)

archivo = open("carga.txt",'a')
archivo.write(str(carga)+"\n")
archivo.close()

archivo = open("/var/www/html/dam/Primero/Programación/009-Gestión de bases de datos/proyectos/Tomato/carga.txt",'r')
lineas = archivo.readlines()
limpias = []
print(lineas)
for linea in lineas:
    linea = linea.replace("\n","")
    linea = float(linea)
    limpias.append(linea)
print(limpias)
plt.plot(limpias, label='Datos', marker='o')
plt.grid(True)
plt.ylim(0, 100)
plt.savefig("/var/www/html/dam/Primero/Programación/009-Gestión de bases de datos/proyectos/Tomato/cargacpu.jpg")
