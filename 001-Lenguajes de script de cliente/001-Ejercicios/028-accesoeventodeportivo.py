print ("Crearemos un constraint de edad para dependiendo de la mayoría de edad se pueda acceder a una zona:")

#Pedimos la entrada de edad a la persona
edad= int (input("Introduce tu edad:"))

#Creamos la restriccion

if edad >= 18 :
    print ("Puedes acceder a la zona especial")
else :
    print ("No puedes acceder a la zona especial")
