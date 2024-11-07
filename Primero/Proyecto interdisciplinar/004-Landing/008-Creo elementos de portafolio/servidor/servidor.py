from flask import Flask, jsonify                        # Importo librería Flask
from flask_cors import CORS                     # Permito entrar a todo el mundo
import mysql.connector                          # Uso el conector de MySQL

app = Flask(__name__)                           # Creo un servidor
CORS(app)                                       # Utilizo CORS

@app.route('/damearticulos')
def home():
    conexion = mysql.connector.connect(
        host="localhost",
        user="landing",
        password="landing",
        database="landing"
    )
    cursor = conexion.cursor(dictionary=True)
    peticion = "SELECT * FROM blog"
    cursor.execute(peticion)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()  # Cierra la conexión
    return jsonify(resultados), 200

@app.route('/dameportafolio')
def portafolio():
    conexion = mysql.connector.connect(
        host="localhost",
        user="landing",
        password="landing",
        database="landing"
    )
    cursor = conexion.cursor(dictionary=True)
    peticion = "SELECT * FROM portafolio"
    cursor.execute(peticion)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()  # Cierra la conexión
    return jsonify(resultados), 200

if __name__ == '__main__':                      # Si estoy en el archivo principal
    app.run(debug=True)                         # Corro el servidor
