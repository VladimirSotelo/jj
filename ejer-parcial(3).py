import pandas as pd

import matplotlib.pyplot as plt

datos_ventas = pd.read_csv('ventas.csv')
print("datos venta \n",datos_ventas)

ventas_por_mes = datos_ventas.sum(axis=1)

ventas_por_mes.plot(kind ="line",figsize=(10,5))
plt.title('ventas mensuales totales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()

ventas_promedio_por_categoria = datos_ventas.mean(axis=0)

ventas_promedio_por_categoria.plot(kind = 'bar',figsize=(10,5))
plt.title('ventas promedio por categoria de productos')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()