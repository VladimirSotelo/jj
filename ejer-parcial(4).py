import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lee el archivo CSV y crea un DataFrame de Pandas con los datos:
df = pd.read_csv("ventas.csv")
print (df)

# Convierte la columna de fechas a un vector de fechas de Pandas:
df['fecha'] = pd.to_datetime(df['fecha'],format='%d/%m/%Y')

#Calcula la cantidad total vendida de cada producto:
ventas_por_producto = df.groupby('producto')['cantidad'].sum()

# Ordena los productos de forma descendente por la cantidad vendida:
ventas_por_producto = ventas_por_producto.sort_values(ascending=False)

# Crea un gráfico de barras horizontales que muestre la cantidad total vendida de cada producto:
plt.barh(ventas_por_producto.index, ventas_por_producto.values)
plt.title('Ventas por producto')
plt.xlabel('Cantidad vendida')
plt.ylabel('Producto')
plt.show()
#El resultado será un gráfico de barras horizontales que muestra la cantidad total vendida de cada producto:

# Calcula la cantidad total vendida por día:
ventas_por_dia = df.groupby('fecha')['cantidad'].sum()

# Crea un gráfico de línea que muestre la evolución de las ventas diarias:
plt.plot(ventas_por_dia.index, ventas_por_dia.values)
plt.title('Evolución de las ventas diarias')
plt.xlabel('Fecha')
plt.ylabel('Cantidad vendida')
plt.show()
