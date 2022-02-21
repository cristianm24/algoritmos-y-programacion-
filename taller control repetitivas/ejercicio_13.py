listao=[]
listan=[]
listaf=[]
estudiantes=int(input("Ingrese la cantidad de estudiantes: "))
estu=int(input("Ingrese 1 para agregar nombres y puntajes: "))
for i in range(0, estudiantes):
    est=input()
    if(estu==1):
        s=(nombre, puntaje)=est.split(" ")
        nombre=str(nombre)
        puntaje=int(puntaje)
        listan.append(nombre)
        listao.append(puntaje)
        listaf.append(s)
        promedio=sum(listao)/len(listao)
        n = [i for i in listao if i>promedio]       
        inf=(len(n)*100)/len(listao)
        s = [i for i in listao if i<promedio]
        sup=(len(s)*100)/len(listao)
    elif(estu==2):
        break
print("El estudiante con el puntaje más alto es: ", (listaf[listao.index(max(listao))]))
print("El estudiante con el puntaje más bajo es: ", (listaf[listao.index(min(listao))]))
print("El puntaje maximo es: ", max(listao))
print("El puntaje maximo es: ", min(listao))
print("Promedio de puntajes: ", promedio)
print(f"Porcentaje de estudiantes que estan bajo el promedio: {inf}%")
print(f"Porcentaje de estudiantes que estan sobre el promedio: {sup}%")