# Crea una función llama dacalcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
# La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
# La función debe devolver el monto del descuento calculado.


def calcular_descuento(monto_total, porcentaje_descuento=20):
    descuento = (monto_total*porcentaje_descuento) /100
    return descuento

compra1 = 100
compra2 = 150
descuto1= calcular_descuento(compra1)
descuento2 = calcular_descuento(compra2)
total1= compra1-descuto1
total2= compra2-descuento2

#imprimir resultados de la primera compra
print("\n PRIMER RESULTADO")

print(f"Total compra 1: ${compra1}")
print(f"El descuento es:{descuto1:.2f}")
print(f"Total de la primera compra= ${total1}")

#Imprimir resultados de la segunda compra
print(f"\n SEGUNDO RESULTADO")

print(f"Total compra 2: ${compra2}")
print(f"El descuento es:{descuento2:.2f}")
print(f"Total de la primera compra= ${total2}")
