import json
from flask import Flask,render_template

app = Flask(__name__)

@app.get("/")	
def inicio():
  archivo = open("005-curriculum.json",'r', encoding="utf-8")
  contenido = json.load(archivo)

  return render_template("no tan sencillo.html",contenido=contenido)

  archivo.close()

if __name__ == "__main__":								#I Si estoy en el archivo principal		
	app.run(debug=True)	