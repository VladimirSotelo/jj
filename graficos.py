import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

x= np.arange(1,20,3.1)
y= np.sin(x)

sns.set_style("darkgrid")

plt.plot(x,y)
plt.title("Grafico de ejemplo")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.show()