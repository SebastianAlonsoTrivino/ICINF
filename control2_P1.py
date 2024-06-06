puntajes=[]

for dia in range(1,15):
    puntaje= int(input(f"ingrese el puntaje para el dia {dia}: "))
    puntajes.append(puntaje)

print("dias con puntajes mayor o igual a 60:")
for dia in range(len(puntajes)):
    if puntajes [dia] >= 60:
        print(f"Dia{dia+1}")

print ("Dias con puntaje menor a 60:")
for dia in range(len(puntajes)):
    if puntajes[dia] < 60:
        print(f"Dia{dia+1}")
