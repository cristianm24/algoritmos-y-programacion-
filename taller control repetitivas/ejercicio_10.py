lista=[]
datos=int(input("Ingrese numero de datos: "))
for i in range(0,datos):
    alt=float(input("Ingrese las alturas: "))
    lista.append(alt)
print("La altura maxima es: ", max(lista))