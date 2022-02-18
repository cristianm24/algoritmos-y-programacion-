"""
Datos de entrada
precio_contado-->p-->float
precio_cuota-->t-->float
Datos de salida
porcentaje_cobro-->po-->float
"""
#Entrada
p=float(input("Ingrese el precio de contado: "))
t=float(input("Ingrese el precio por cuota: "))
#Caja negra
po=(p/12)-t
#Salida
print(f"El porcentaje que se cobra por el recargo es de {po}%")