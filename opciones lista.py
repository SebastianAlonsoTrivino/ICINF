lista = []

while True:
    print("\n1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        lista.append(input("Ingresa el elemento: "))
    elif opcion == "2":
        i = int(input("Índice a modificar: "))
        if 0 <= i < len(lista):
            lista[i] = input("Nuevo elemento: ")
        else:
            print("Índice no válido.")
    elif opcion == "3":
        i = int(input("Índice a eliminar: "))
        if 0 <= i < len(lista):
            del lista[i]
        else:
            print("Índice no válido.")
    elif opcion == "4":
        if lista:
            lista.pop()
        else:
            print("La lista está vacía.")
    elif opcion == "5":
        e = input("Elemento a buscar: ")
        if e in lista:
            print(f"'{e}' está en el índice {lista.index(e)}.")
        else:
            print("Elemento no encontrado.")
    elif opcion == "6":
        print("Lista:", lista)
    elif opcion == "7":
        break
    else:
        print("Opción no válida.")