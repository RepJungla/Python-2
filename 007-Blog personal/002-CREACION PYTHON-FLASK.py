import sqlite3                                  # Uso SQLite3
from flask import Flask, render_template        # Uso Flask

app = Flask(__name__)                           # Creo la app web

@app.get("/")                                   # Ruta principal
def inicio():
    conexion = sqlite3.connect("blog.db")      # Conexión a la BD
    conexion.row_factory = sqlite3.Row          # Filas como diccionarios
    cursor = conexion.cursor()                  # Cursor

    cursor.execute("SELECT * FROM entradas")    # Recupero entradas del blog
    filas = cursor.fetchall()                   # Ejecuto la consulta

    entradas = []                               # Lista de entradas
    for fila in filas:
        entradas.append(dict(fila))             # Paso a diccionario

    return render_template("blog.html", datos=entradas)

if __name__ == "__main__":
    app.run(debug=True)
