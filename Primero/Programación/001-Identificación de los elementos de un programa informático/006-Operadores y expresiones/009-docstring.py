'''
    Programa calculadora de primer tema de clase
    (c) 2024 Jose Vicente Carratalá
    Este programa está hecho en Python
'''

NOMBRE_DEL_PROGRAMA = "Programa calculadora"
VERSION = "0.1"
AUTOR = "Jose Vicente Carratalá"
print(NOMBRE_DEL_PROGRAMA,VERSION,AUTOR)

operando1 = input("Introduce el primer operando: ")
operando2 = input("Introduce el segundo operando: ")
operador = input("Introduce el operador (+,-,*,/): ")

operando1 = int(operando1)
operando2 = int(operando2)

if operador == "+":
    resultado = operando1 + operando2
elif operador == "-":
    resultado = operando1 - operando2
elif operador == "*":
    resultado = operando1 * operando2
elif operador == "/":
    resultado = operando1 / operando2

print("El resultado de la operación es: ",resultado)
