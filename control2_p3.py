palabras = []

while True:
    palabra = input("Ingrese una palabra (deje vacío para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)

if palabras:
    palabra_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    print(f"La palabra con mayor cantidad de caracteres es '{palabra_larga}' con {len(palabra_larga)} caracteres.")
else:
    print("No se ingresaron palabras.")
