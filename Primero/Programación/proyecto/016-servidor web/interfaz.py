from ConectorBD import *
import tkinter as tk

conexion1 = ConectorBD()

ventana = tk.Tk()

tablas = conexion1.dameTablas()

for tabla in tablas:
    tk.Button(ventana,text=tabla['Tables_in_programacion']).pack(padx=10,pady=10)

ventana.mainloop()
