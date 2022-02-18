""""
entradas
preciocomputador-->P-->float
valorcuotas-->T-->float
salidas
porcentajerecargo-->por-->float
"""

#entradas
P=float(input("Ingrese el precio del computador: "))
T=float(input("Ingrese el valor de las cuotas: "))

#caja negra
tc=T*12
r=tc-P
por=(r*100)/P

#salidas
print("El porcentaje de recargo es del ", por, "%")