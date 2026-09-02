print("=== INVENTARIO SENCILLO - VERSION 2.0 ===")

continuar = "si"

while continuar == "si":
    producto = input("/nEscribe el nombre del producto: ")
    cantidad = int(input("Escribir la cantidad disponible: "))
    precio = float(input("Escribe el precio del producto: "))

    TOTAL = cantidad * precio

    print("/n--- RESULTADO---")
    print("Producto:",producto)
    print("Cantidad:",cantidad)
    print("precio: $", precio)
    print("Valor total del inventario: $", TOTAL)

    if cantidad == 0:
        print("Estado: Producto agotado.")
    elif cantidad <= 5:
        print("Estado: Quedan pocas unidades.")
    else:
        print("Estado Inventrio disponible.")
    continuar = input("/n¿Deseas registrar otro producto? (si/no): ").lower()
print("/nPrograma finalizado.")