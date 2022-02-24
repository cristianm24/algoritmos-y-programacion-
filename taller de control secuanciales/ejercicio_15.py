"""
entradas
preciofinalpagado-->pfp-->float
precioventa-->pvp-->float
salidas
descuentoaplicado-->desc-->float
"""

#entradas
pfp=float(input("Ingrese el precio final pagado del producto: "))
pvp=float(input("Ingrese el precio de venta al publico del producto: "))

#caja negra
desc=round(((pvp-pfp)*100)/pvp, 2)

#salidas
print("El descuento aplicado es del ",desc, "%")