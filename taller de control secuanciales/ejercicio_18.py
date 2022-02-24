"""
entradas
capitalparaprestamo-->c-->float
tasadeinteres-->t-->float
salidas
porcentajeanualdecobro-->i-->float
"""

#entradas
c=float(input("Ingrese el capital "))
t=float(input("Ingrese la tasa de interes "))

#caja negra
i=(t*100)/(c*4)

#salidas
print("El porcentaje anual de cobro por el prestamo de ",c, " sera de ",i, "%")