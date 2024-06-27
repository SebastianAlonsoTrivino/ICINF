precios_clp = []
for i in range(10):
    TASA_CAMBIO_USD_CLP = 950.0
    
print("ingrese un monto en CLP por favor")
for i in range(10):
    precio = float(input("ingrese un monto: "))
    precios_clp.append(precio)
    
precios_usd = []
for precio_clp in precios_clp:
    precio_usd = precio_clp / TASA_CAMBIO_USD_CLP
    precios_usd.append(precio_usd)
    
print("la lista de precios transformados a usd es: ")
print(["$" + "%.2f" % precio_usd for precio_usd in precios_usd])