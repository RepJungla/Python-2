print ("Clasificaremos el rendimiento de un jugador según sus puntos anotados:")

#creamos la variable
puntaje=int(input("Anota los puntos marcados: "))

#hacemos los condicionales
if puntaje <=10 :
    print ("Rendimiento bajo")
elif puntaje >=11 and puntaje <=19 :
    print ("Rendimiento medio")
elif puntaje >=20 and puntaje <=29 :
    print ("Rendimiento alto")
else :
    print ("Rendimiento estrella")