def main():
    alturas = []
    
    while True:
        try:
            altura = float(input("Ingrese una altura en metros (o 0 para finalizar): "))
            if altura == 0:
                break
            elif altura < 0:
                print("Por favor, ingrese una altura válida (mayor o igual a 0).")
            else:
                alturas.append(altura)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    if alturas:
        promedio = sum(alturas) / len(alturas)
        print(f"La altura promedio es: {promedio:.2f} metros")
    else:
        print("No se ingresaron alturas.")

if __name__ == "__main__":
    main()
