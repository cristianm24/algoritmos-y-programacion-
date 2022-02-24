"""
entradas
lecturaanterior-->lec_an-->float
lecturaactual-->lec_ac-->float
costokilovatio-->ck-->float
salidas
totalapagar-->total-->float
"""

#entradas
lec_an=float(input("Ingrese la lectura anterior: "))
lec_ac=float(input("Ingrese la lectura actual: "))
ck=float(input("Ingrese el costo por kilovatio: "))

#caja negra
total=round((lec_ac-lec_an)*ck, 2)

#salidas
print("El monto total a pagar en un mes de luz eléctrica es de ",total)