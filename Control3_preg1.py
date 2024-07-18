def digitos(num):
    num_str = str(num)
    cantidad_digitos = len(num_str)
    return cantidad_digitos

numero_ingresado = input("Ingrese un número: ")

print(f"La cantidad de dígitos en el número ingresado es: {digitos(numero_ingresado)}")
