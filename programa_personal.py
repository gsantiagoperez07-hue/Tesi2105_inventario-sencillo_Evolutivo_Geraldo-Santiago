class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def calcular_valor(self):
        return round(self.cantidad * self.precio, 2)


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

print("=== INVENTARIO SENCILLO - PROYECTO FINAL ===")

continuar = "si"

while continuar == "si":
    producto = input("\nEscribe el nombre del producto: ")
    try:
        cantidad = int(input("Escribir la cantidad disponible: "))
        if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                continue
        precio = float(input("Escribe el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            continue
    except ValueError:
        print("Error: Debes escribir uun numero valido.")
        continue
    nuevo_producto = Producto(producto, cantidad, precio)
    TOTAL = nuevo_producto.calcular_valor()

    mostrar_resultado(producto, cantidad, precio, TOTAL)

    verificar_estado(cantidad)
    continuar = input("\n¿Deseas registrar otro producto? (si/no): ").lower()
print("/nPrograma finalizado.")
