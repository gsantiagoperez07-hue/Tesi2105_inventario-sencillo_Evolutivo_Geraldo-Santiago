# Laboratorio5 - Arreglos y Cadenas

#Parte 2 - Arreglo Unidimensional

precios = [10.50, 20.00, 15.75, 8.50, 30.00]

print("Cpntenido completo:")
print(precios)

print("/nAcceso mediante indices:")
print("Primer elemento:", precios [0])
print("Tercer elemento:", precios [2])

# Modificar un elemento
precios [1] = 25.00

print("/nArreglo despues de modificar un elemento:")
print(precios)

print("/nRecrrido del arreglo:")
for precio in precios:
    print(precio)
    
    
    
# Parte 3 - Arreglo Multidimensional

notas = [ [90, 85, 88,], [78, 92, 80] ]

print("/nArreglo multimensional:")

for fila in notas:
    for nota in fila:
        print(nota, end=" ") 
        print()
        
print("/nDato especifico:", notas[0][1])


# Parte 4 - Cadenas de Caracteres

texto = "Programacion"

print("/nTexto:", texto)

#Mostrar la longitud
print("Longitud de las cadena:", len (texto))

#Acceder a un caracter mediante indice
print("Caracter en el indice 3:", texto[3])

#Recorrer los caracteres
print("Recrrido de caracteres:")
for caracter in texto:
    print(caracter)

#Buscar dentro del texto
if "grama" in texto:
    print("La palabra 'grama' fue encontrada.")
    
#Transformar el texto
texto_mayuscula = texto.upper()
print("Texto en mayusculas:", texto_mayuscula)
