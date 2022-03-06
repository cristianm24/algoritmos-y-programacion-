archivo = open("C:\Users\CRISTIAN\Desktop\TallerEstructurasFor\paises.txt", "r")
## Ejemplos
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""

##Taller para realizar:
#1: Cuente e imprima cuantas ciudades inician con la letra M"""
"""
lista=[]
ciudades=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="M"):
    contador=contador+1
    print(i,contador)
"""  
#2: Imprima todos los paises y capitales, cuyo inicio sea con la letra U
# Paises
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
"""   
# Ciudades:
"""""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="U"):
    print(i)
"""
#3: Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
for i in archivo:
    lista.append(i)
print(len(lista))
"""
#4: Busque e imprima la ciudad de Singapur"""
"""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i=="Singapur"):
    print(i)
"""
#5: Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
pais=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  for r in lista:
    pais.append(r)
for i in pais:
  if i=="Venezuela: Caracas\n":
    print(i)
    break
  lista=[]   
"""
#6: Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudades=[]
ciudad=[]
for i in archivo:
  lista.append(i)
for i in lista:  
  if(i[0]=="E"):
    ciudades.append(i)
  c="".join(ciudades)  
for i in ciudades:
  a=i.index(":")     
  for r in range(a+2,len(i)-1):
    ciudad.append(i[r])
  b = "".join(ciudad)  
  for e in ciudad:
    e="".join(ciudad)
  ciudad=[]
  print(e)
"""
#7: Buesque e imprima la Capiltal de Colombia
"""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i=="Bogotá"):
    print(i)
"""
#8: imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#9: imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
"""
#10: El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien 
#es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
for i in archivo:
  lista.append(i)
  lista.remove=("Madagascar: rey julien")
  lista.insert=(149,"Madagascar: Antananarivo")
  print(lista)
"""
#11: Agregue un país que no esté en la lista 
"""
nuevo="Reino de Lothric: Anor Londo"
archivo= open('paises.txt', 'a')
archivo.write(nuevo)
"""
#archivo.close()