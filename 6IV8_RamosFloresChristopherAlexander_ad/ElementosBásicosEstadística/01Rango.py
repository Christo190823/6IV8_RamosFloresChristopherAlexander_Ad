import pandas as pd

## Escribir un programa que pregunte al ususario por las ventas y muestre en la pantalla los datos de los vantas indexadas por los años antes y después

inicio = int(input('Introduce el año de ventas inicial: '))
fin = int(input('Introduce elaño final de ventas: '))

ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input('introduce las ventasdel año: ' + str(i) + ': '))
    
ventas = pd.Series(ventas)
print('ventas \n' , ventas )
print('Ventas con descuento\n', ventas*0.9)