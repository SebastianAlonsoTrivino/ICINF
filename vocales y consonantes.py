lista_palabras = []

while True:
    palabra = input("Ingresa una palabra (deja en blanco para terminar): ")
    if palabra == "":
        break
    lista_palabras.append(palabra)

def contar_vocales_consonantes(palabra):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0
    
    for letra in palabra:
        if letra in vocales:
            num_vocales += 1
        elif letra.isalpha():
            num_consonantes += 1
                
    return num_vocales, num_consonantes

for palabra in lista_palabras:
    vocales, consonantes = contar_vocales_consonantes(palabra)
    print(f"La palabra '{palabra}' tiene {vocales} vocales y {consonantes} consonantes.")