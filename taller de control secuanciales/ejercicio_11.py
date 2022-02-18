"""
Datos de entrada
numero_horas-->nh-->float
pago_hora-->ph-->float
horas_extras-->he-->float
numero_hijos-->nj-->int
numero_academicas-->na-->int
Datos de salida
asignaciones-->asg-->float
deducciones-->ded-->float
sueldo_neto-->sn-->float
"""
#Entradas
nh=float(input("Ingrese el número de horas trabajadas: "))
ph=float(input("Ingrese el pago por hora: "))
he=float(input("Ingrese el número de horas extras trabajadas: "))
nj=int(input("Ingrese el número de hijos: "))
na=int(input("Ingrese número de actualizaciones académicas: "))
#Caja negra
nt=nh*ph
hx=(((ph*0.25)*he)+nt)
ded=(hx*0.14)
asg=(na*250000)+(nj*173000)+180000
sn=hx+asg-ded
#Salidas
print("Se le da por asignaciones: ", asg)
print("Se le resta por deducciones: ", ded)
print("El salario total neto es: ", sn)