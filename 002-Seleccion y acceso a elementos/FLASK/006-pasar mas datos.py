from flask import Flask,render_template                 #Importamos la librería FLASK y la template

app = Flask(__name__)                                   #Creamos una nueva aplicación

datos = {'nombre':'Héctor',
        'apellido':'Quirós Pérez',
        }                

@app.get("/")                                           #Escuchamos en la raiz de la web
def inicio():                                            #Creamos una función
    return render_template("masdatos.html", misdatos=datos)               #Buscará en la carpeta "templates" el html


if __name__=="__main__":                                #Si nos encontramos en el archivo principal
    app.run(debug=True)                                 #Ejecutamos la aplicacion

#Primero navego a la carpeta indicada (o le dais a play los niños del Visual studio)
#Si estais en linea de comandos, python3 "001-flasksencillo.py"
#Ahora abrimos un navegador web
#Y entramos en la pagina web http://127.0.0.1:5000