import numpy as np
print("OPERACION CON MATRICES")

a =np.array([[3,5],[21,65]])
print(" a\n",a,"\n") 

b =np.array([[2,7],[5,6]])
c= a+b
print(" a+b\n",c,"\n")

c=a.dot(b)
print(" a*b\n",c,"\n")

print("TRANSPUESTAS")

Ta=(a.transpose())
print(" transpuestade a\n",Ta,"\n")

j = np.array([[12,3,4],[32,43,6],[12,32,5]])


print("SUMA DE DIAGONAL Y DIAGONAL")

trace= np.trace(j)
print("\n",j,"\n")
print("\n",trace,"\n")

di=np.diagonal(j)
print("\n",di,"\n")

print("NUMEROS COMPLEJOS \n")
x=np.array([8+7j,5+6j])
print("\n",x,"\n")
y=np.array([2+3j,4+5j])
print("\n",y,"\n")
z=np.vdot(x, y) 
print("\n",z,"\n")

