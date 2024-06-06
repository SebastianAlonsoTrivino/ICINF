nombres = []


for _ in range(7):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombres_terminan_a = []
for nombre in nombres:
    if nombre.lower()[-1] == 'a':
        nombres_terminan_a.append(nombre)

print("Lista resultante después de eliminar nombres que no terminan en 'a':")
print(nombres_terminan_a)
