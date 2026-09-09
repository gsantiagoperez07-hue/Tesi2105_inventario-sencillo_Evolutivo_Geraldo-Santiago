def calcular_total(cantidad, precio):
    total = round (cantidad * precio, 2)
    return total

def mostrar_resultado(producto, cantidad, precio, total):
    print("/n--- RESULTADO---")
    print("Producto:", producto)
    print("Cantidad:", cantidad)
    print("Valor total del inventario:  $", total)

def verificar_estado(cantidad):
    if cantidad == 0:
        print("Estado: Producto agotado.")
    elif cantidad <= 5:
        print("Estado: Quedan pocas unidades.")
    else:print("Estado: Inventario disponible.")

print("=== INVENTARIO SENCILLO - VERSION 3.0 ===")

continuar = "si"

while continuar == "si":
    producto = input("/nEscribe el nombre del producto: ")
    cantidad = int(input("Escribir la cantidad disponible: "))
    precio = float(input("Escribe el precio del producto: "))

    TOTAL = calcular_total (cantidad, precio)

    mostrar_resultado(producto, cantidad, precio, TOTAL)

    verificar_estado(cantidad)
    continuar = input("/n¿Deseas registrar otro producto? (si/no): ").lower()
print("/nPrograma finalizado.")