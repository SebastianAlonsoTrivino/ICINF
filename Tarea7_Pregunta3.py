supermercado = {}

print("Ingrese productos. Para finalizar, presione Enter sin ingresar un producto.")

while True:
    nombre_producto = input("Ingrese el nombre del producto: ")
    if nombre_producto == "":
        break
    cantidad = int(input("Ingrese la cantidad de " + nombre_producto + ": "))
    supermercado[nombre_producto] = cantidad

X = int(input("Ingrese un valor numérico para multiplicar las cantidades: "))

print("Productos con sus cantidades multiplicadas por " + str(X) + ":")
for producto, cantidad in supermercado.items():
    nueva_cantidad = cantidad * X
    print(producto + ": " + str(nueva_cantidad))