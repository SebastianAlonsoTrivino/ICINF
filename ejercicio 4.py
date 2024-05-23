def leer_sueldos():
    sueldos = []
    print("Ingrese los sueldos de los empleados uno por uno. Ingrese -1 para finalizar.")

    while True:
        sueldo = int(input("Ingrese el sueldo del empleado: "))
        if sueldo == -1:
            break
        if 500000 <= sueldo <= 1500000:
            sueldos.append(sueldo)
        else:
            print("El sueldo debe estar entre $500.000 y $1.500.000. Intente nuevamente.")

    return sueldos

def clasificar_sueldos(sueldos):
    sueldos_500_900 = [sueldo for sueldo in sueldos if 500000 <= sueldo <= 900000]
    sueldos_mas_900 = [sueldo for sueldo in sueldos if sueldo > 900000]

    return sueldos_500_900, sueldos_mas_900

def calcular_gasto_total(sueldos):
    return sum(sueldos)

def main():
    sueldos = leer_sueldos()
    sueldos_500_900, sueldos_mas_900 = clasificar_sueldos(sueldos)
    gasto_total = calcular_gasto_total(sueldos)

    print(f"Cantidad de empleados que cobran entre $500.000 y $900.000: {len(sueldos_500_900)}")
    print(f"Cantidad de empleados que cobran más de $900.000: {len(sueldos_mas_900)}")
    print(f"El gasto total de la empresa en sueldos es: ${gasto_total:,}")

if __name__ == "__main__":
    main()
