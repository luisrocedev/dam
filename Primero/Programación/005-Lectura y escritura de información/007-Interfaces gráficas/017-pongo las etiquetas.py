import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Calculadora v0.1")

tk.Label(
    ventana,
    text="Introduce el operando 1"
    ).pack(
        padx=10,
        pady=10
        )

ventana.mainloop()
