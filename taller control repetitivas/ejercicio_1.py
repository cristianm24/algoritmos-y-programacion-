n=int(input("Ingrese el numero N: "))
k=int(input("Ingrese el numero K: "))
sum=0
while True:
    if(k<n):
        n=n-1 
        print(n) 
    elif(k==n): 
        break
print(k) 