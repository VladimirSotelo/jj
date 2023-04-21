Nombre=[]
Edad=[]
i=0
n=input("ingrese el Nombre del Alumno: ")
e=input("ingrese la Edad del mismo: ")
while (n != "*" and e!="*"):
    Nombre.append(n)
    Edad.append(e)
    Nombre.sort()
    Edad.sort()
    n=input("ingrese el Nombre del Alumno: ")
    e=input("ingrese la Edad del mismo: ")
    
for i in zip(Nombre,Edad):
    print(i)


