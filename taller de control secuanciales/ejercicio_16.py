"""
entradas
galonesasurtir-->ng-->float
salidas
valortotalcobro-->total-->float
"""
#entradas
ng=float(input("Numero de galones que se surtiran: "))

#caja negra
total=round((ng*3.785)*50000, 2)

#salidas
print("El valor a cobrar sera de ",total, "COP")