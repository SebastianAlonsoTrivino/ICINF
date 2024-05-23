def main():
    nombre1 = input("Ingrese el primer nombre: ")
    nombre2 = input("Ingrese el segundo nombre: ")

    
    nombres = [nombre1, nombre2]

   
    nombres_ordenados = sorted(nombres)

    
    print("Nombres ordenados alfabéticamente:")
    for nombre in nombres_ordenados:
        print(nombre)


if __name__ == "__main__":
    main()