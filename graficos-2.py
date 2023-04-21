import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd

Esperaclientes= [random.randint (1,40)for i in range(100)]
sns.displot(Esperaclientes)
#plt.plot(Esperaclientes)

sns.set_style("dark")
plt.title("Grafico")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.show()