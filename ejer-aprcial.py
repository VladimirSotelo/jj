import matplotlib.pyplot as plt

#ventas={
    #"producto A": 120,"producto B":250,
    #"producto C": 400,"producto D":80,
    #"producto E":150,
    #            }

#productos =list(ventas.keys())
#cantidades= list(ventas.values())

#fig,ax=plt.subplots()

#ax.bar(productos,cantidades)

#ax.set_xlabel('producto')
#ax.set_ylabel('ventas')
#ax.set_title('ventas mensuales')

temperaturas={
    'Entre Rios':[39,38,32,30,20,10,8,16,21,25,12,42],
    'Corrientes':[41,40,32,35,25,14,14,20,28,29,30,32],
    'Miisiones':[42,20,33,34,26,14,15,29,30,30,32,35],
    'Formosa':[45,45,40,36,30,28,25,30,44,42,42,43]           
    }

meses = ['Enero','febrero','Marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

fig,ax=plt.subplots()

for provincias,temperaturas_privincias in temperaturas.items():
    ax.plot(meses,temperaturas_privincias,label=provincias)

ax.set_xlabel('Mes')
ax.set_ylabel('Temperatura')
ax.set_title('Temperaturas promedio durante un año')
ax.legend()
plt.show()
