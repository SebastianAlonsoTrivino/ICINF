def calcular_nivel(total_preguntas, preguntas_correctas):
    porcentaje = (preguntas_correctas / total_preguntas) * 100

    if porcentaje >= 95:
        nivel = "Nivel máximo"
    elif porcentaje >= 70:
        nivel = "Nivel medio"
    elif porcentaje >= 40:
        nivel = "Nivel regular"
    else:
        nivel = "Fuera de nivel"
    
    return porcentaje, nivel
total_preguntas = int(input("Ingrese el total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
porcentaje, nivel = calcular_nivel(total_preguntas, preguntas_correctas)

print(f"El porcentaje de respuestas correctas es: {porcentaje:.2f}%")
print(f"El nivel del postulante es: {nivel}")
