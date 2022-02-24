"""
entradas
presupuestoanual-->pre_a-->float
salidas
presupestoparaginecologia-->pre_g-->float
presupestoparatraumatologia-->pre_t-->float
presupestoparapediatria-->pre_p-->float
"""
#entradas
pre_a=float(input("Ingrese el presupuesto anual: "))

#caja negra
pre_g=round(pre_a*0.40, 2)
pre_t=round(pre_a*0.30, 2)
pre_p=round(pre_a*0.30, 2)

#salidas
print("Ginecologia recibira ",pre_g)
print("Traumatologia recibira ",pre_t)
print("Pediatria recibira", pre_p)
