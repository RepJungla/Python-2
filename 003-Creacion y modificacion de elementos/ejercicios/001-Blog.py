from flask import Flask,render_template		
from datetime import datetime                                                                             #Importa libreria de horas

ahora = datetime.now()                                                                                    #Crea la variable "ahora"

anio   = ahora.year
mes = ahora.month                                                                                         #Creamos todas las variables restantes 
dia  = ahora.day
hora  = ahora.hour
minuto = ahora.minute
segundo = ahora.second

app = Flask(__name__)					

blog = {
  'fecha':{
    'anio':anio,
    'mes':mes,
    'dia':dia,
    'hora':hora,
    'minuto':minuto,
    'segundo':segundo
	},
  'articulos':[
    {'titulo':'Esto es el titulo 1','texto':'Esto es el texto 1','fecha':'2025-12-01'},
    {'titulo':'Esto es el titulo 2','texto':'Esto es el texto 2','fecha':'2025-12-02'},
    {'titulo':'Esto es el titulo 3','texto':'Esto es el texto 3','fecha':'2025-12-03'}
  ]
}
 # {Esto es para hacer diccionarios}
 # [Esto es para hacer listas de diccionarios]
 
@app.get("/")										
def inicio():										
    return render_template("blog.html",datos=blog)

if __name__ == "__main__":				
    app.run(debug=True)