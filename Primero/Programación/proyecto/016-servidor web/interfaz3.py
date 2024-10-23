from ConectorBD import *
import tkinter as tk

conexion1 = ConectorBD()

def damedatos(tabla):
    print("Te voy a dar los datos de la tabla: "+tabla)

ventana = tk.Tk()

tablas = conexion1.dameTablas()

for tabla in tablas:
    tk.Button(
        ventana,
        text=tabla['Tables_in_programacion'],
        command=lambda t=tabla['Tables_in_programacion']: damedatos(t)
        ).pack(padx=10,pady=10)

texto = tk.Text(ventana)
texto.pack(padx=10,pady=10)

ventana.mainloop()
