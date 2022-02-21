al=0
gas=0
die=0
while True:
    codigo=int(input())
    if(codigo==1):
        al=al+1
    elif(codigo==2):
        gas=gas+1
    elif(codigo==3):
        die=die+1
    elif(codigo==4):
        break
print(f"MUITO OBRIGADO\nAlcool:{al}\nGasolina: {gas}\nDiesel: {die}")