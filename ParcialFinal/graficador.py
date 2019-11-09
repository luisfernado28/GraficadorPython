import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Lectura del archivo csv para almacenarlo como un set de datos
weather = pd.read_csv('https://coded2.herokuapp.com/datavizpandas/london2018.csv')
##imprimir para ver contenido de set de datos
#print(weather)


##Crea un grafico en referencia con el eje X y Y en base a dos columnas del set de datos
weather.plot(y='Tmax', x='Month')
#weather.plot.bar(y='Tmax', x='Month')
##Capacidad de graficar mas de dos columnas del documento al mismo tiempo
#weather.plot.bar(y=['Tmax','Tmin'], x='Month')

##graficar multiples recuadros para diferentes columnas, Layouts permite definir los recuadros
#weather.plot.bar(y=['Tmax','Tmin','Rain','Sun'], x='Month', subplots=True, layout=(2,2))



##  graficar puntados con valores en relacion entre dos variables 
#weather.plot.scatter(x='Sun', y='Rain')

################################################siguiente segmento#####
##formas alternativas para graficar graficos de "torta"
meals = pd.read_csv("https://coded2.herokuapp.com/datavizpandas/meals2.csv", index_col = 0)
print(meals)

meals.plot.pie(subplots=True)
plt.savefig("pie.png")


#etiqueta para desplegar cuadros
#plt.legend()

## muestra los datos graficados en una imagen
plt.show()

