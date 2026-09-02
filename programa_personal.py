print("=== Inventario SENCILLO ===")

Producto = input("Escribe el nombre del producto:")
Cantidad = int(input("Escribe la cantidad disponible:"))
precio = float(input("Escribe el precio del producto:"))

TOTAL = Cantidad * precio

print("/n--- RESULTADO ---")
print("Producto:", Producto)
print("Cantidad:", Cantidad)
print("Precio: $", precio)
print("Valor total del inventario: $", TOTAL)