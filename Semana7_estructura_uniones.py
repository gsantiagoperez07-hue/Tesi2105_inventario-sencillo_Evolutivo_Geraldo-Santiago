equipo = {
    "nombre": input("Nombre del equipo: "),
    "ram": int(input("RAM en GB: ")),
    "estado": input("Estado: "),
}

dato_alternativo = {
    "tipo": input("Tipo de identificador (serie/activo): "),
    "valor": input("Valor del identificador: "),
}

print("\nREGISTRO DEL EQUIPO")
print("Nombre:", equipo["nombre"])
print("RAM:", equipo["ram"], "GB")
print("Estado:", equipo["estado"])
print("Identificador:", dato_alternativo["tipo"], "=", dato_alternativo["valor"])
