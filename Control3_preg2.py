def es_binario(var):
    for i in range(len(var)):
        
        if var[i] != '0' and var[i] != '1':
            return False
    return True

cadena_ingresada = input("Ingrese una cadena: ")

if es_binario(cadena_ingresada):
    print("La cadena ingresada es una expresión binaria.")
else:
    print("La cadena ingresada NO es una expresión binaria.")
