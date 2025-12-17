from flask import Flask                                 #Importamos la librería FLASK

app = Flask(__name__)                                   #Creamos una nueva aplicación

@app.get("/")                                           #Escuchamos en la raiz de la web
def index():                                            #Creamos una entrada
    return "<h1>Hola mundo desde Flask</h1>"            #Devolvemos algo mínimo

if __name__=="__main__":                                #Si nos encontramos en el archivo principal
    app.run(debug=True)                                 #Ejecutamos la aplicacion

#Primero navego a la carpeta indicada (o le dais a play los niños del Visual studio)
#Si estais en linea de comandos, python3 "001-flasksencillo.py"
#Ahora abrimos un navegador web
#Y entramos en la pagina web http://127.0.0.1:5000