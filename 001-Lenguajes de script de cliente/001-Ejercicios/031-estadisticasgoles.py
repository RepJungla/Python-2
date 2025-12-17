'''Enunciado

Queremos calcular las estadísticas de goles de un jugador en una serie de 5 partidos.

Usa un bucle for que vaya de 1 a 5.

En cada iteración, pide por teclado los goles anotados en ese partido y conviértelos a int.

Ve acumulando los goles en una variable total.

Al final, muestra:

El total de goles.

La media de goles por partido (total dividido entre 5).'''

print ("Queremos calcular las estadísticas de goles de un jugador en una serie de 5 partidos.:")

goles_total=0

for days in range (1,6):
    goles= int(input ( "Introduce los goles anotados en ese partido: "))

    goles_total = goles_total + goles


print (goles_total)



