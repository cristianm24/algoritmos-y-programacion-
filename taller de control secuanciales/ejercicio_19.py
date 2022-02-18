"""
entradas
numerodenaranjas-->lote-->int
docenasnaranjas-->docena-->float
cantidadtotalporventas-->t_c-->float
salidas
porcentajeganancia-->p_g-->float
"""

#entradas
lote=int(input("Lote de naranjas: "))
docena=float(input("Docena: "))
t_v=float(input("Cantidad de las ventas: "))

#caja negra
t_g=(lote/12)*docena
p_g=round(((t_v-t_g)*100)/t_g, 2)

#salidas
print("El porcentaje de ganancia fue de ",p_g, "%")