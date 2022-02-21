k=1
n=0
lista=[]
while n<999:
    n=(k**2+1)/k
    lista.append(n)
    print(n)
    k=k+1
print(len(lista))