consume=int(input("¿Consume licor? Digite 1 para si y 2 para No: "))
agr=0
ron=0
cerv=0
teq=0
whi=0
otro=0
licor=0
listaco=[]
listaco.append(consume)
listalicor=[]
listaaños=[]
listacv=[]
listawhi=[]
listam=[]
listaf=[]
listap=[]
while True:
    if((consume==2)):
        print(f"Aguardiente {agr}\nRon {ron}\nCerveza {cerv}\nTequila {teq}\nwhisky {whi}\nOtro {otro}")
        print(len(listaco))
        print(len(listaf))
        print(sum(listam))
        print(sum(listap)/sum(listacv))
        print(len(listawhi)/len(listaco))
        break
    elif(consume==1):
        años=int(input("Ingrese su edad: "))
        listaaños.append(años)
        sexo=str(input("Ingrese su sexo. 1 para femenino y 2 para masculino: "))
        licor=int(input("1.Aguardiente, 2.Ron, 3.Cerveza, 4.Tequila, 5.Whisky, 6.Otro: "))
        listalicor.append(licor)
        print("Encuesta nueva")
        consume=int(input("Continuar la encuesta, 1 para sí, 2 para no: "))
        if(licor==1):
            agr=agr+1
        elif(licor==2):
            ron=ron+1 
        if(licor==3):
            cerv=cerv+1
            listacv.append(cerv)
            if(licor==3 and años>0):
                p=años
                listap.append(p)
                continue
        if(licor==4):
            teq=teq+1
        if(licor==5):
            whi=whi+1
            listawhi.append(whi)
        if(licor==6):
            otro=otro+1  
        elif(años>=0):
            listaaños.append(años)
            continue
        elif(años<=18)and(sexo==1):
            f=años+sexo
            listaf.append(f)
            continue
        elif(20>=años<=25)and(sexo==2) and (licor!=5):
            m=años+sexo
            if(licor!=5):
                listam.append(m)
            continue