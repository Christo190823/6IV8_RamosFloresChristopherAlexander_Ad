import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBásicosEstadística/housing.csv')

##Mostrar las primeras 5 filas
print(df.head())

##Mostrar las ultimas 5 filas
print(df.tail())

##Mostrar fila en especifico
print(df.iloc[7])

##Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

##Obtener la media de la columna total_rooms
mediadecuartos = df["total_rooms"].mean()
print('La media de total rooms es', mediadecuartos)

##Mediana
medianacuarto = df['median_house_value'].median()
print('La mediana de lacolumna valor mediana de la casa: ',  mediadecuartos)

##La suma de popular 
salariototal = df['population'].sum()
print('El salario total es de: ', salariototal)

##Para vpoder filtara
vamoshacerunfiltro = df[df['ocean_proximity']=='ISLAND']
print(vamoshacerunfiltro)

##vamos a hacer un gráfico de disperción
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
##Nombramos los ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("Gráfico de disperción deproximidad al Oceano vs precio")
plt.show()