import random
i=0
a=[]

for i in range(1,11):
    a.append(random.randint(1,10))
    a.sort()


for n in a:
    print(n,"",n**2,"",n**3)
    


