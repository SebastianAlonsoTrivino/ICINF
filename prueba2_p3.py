capitales_paises = {}

print("Ingrese 5 capitales y sus países:")
for x in range(5):
    capital = input(f"Ingrese la capital {x + 1}: ")
    pais = input(f"Ingrese el país de la capital {capital}: ")
    capitales_paises[capital] = pais

print("Capitales y países ingresados:")
print(capitales_paises)

nombre_turista = input("Ingrese el nombre del turista: ")
capital_turista = input("Ingrese la capital de procedencia del turista: ")

if capital_turista in capitales_paises:
    pais_turista = capitales_paises[capital_turista]
else:
    pais_turista = "desconocido"

print("El turista con el nombre {nombre_turista} viene de la capital {capital_turista} y su país es {pais_turista}.")
