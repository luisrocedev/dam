from flask import Flask
from flask_cors import CORS


aplicacion = Flask(__name__)
CORS(aplicacion)

@aplicacion.route('/')
def inicio():
    entradas = []
    entradas.append({
        "titulo":"Mi primera entrada",
        "fecha":"2024-09-26",
        "contenido":"Este es el contenido de mi primera entrada"
    })
    entradas.append({
        "titulo":"Segunda entrada desde Python",
        "fecha":"2024-09-26",
        "contenido":"Si estas viendo este contenido, que sepas que es porque te lo está dando Python, porque si no es por eso, no lo verías"
    })
    return entradas

if __name__ == '__main__':
    aplicacion.run()
