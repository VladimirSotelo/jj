def factorial(n):
    if n==0: 
        return 1
    else:
        return n * factorial(n-1)

def sumalista(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+sumalista(lista[1:]) 
        


lista=[10,20,14,25,21,4]

print(sumalista(lista))


