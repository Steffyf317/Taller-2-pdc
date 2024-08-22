#3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

def son_espejos(a, b):
    # Convierte los números a cadenas
    a_str = str(a)
    b_str = str(b)

    # Compara la cadena de a con la cadena de b invertida
    return a_str == b_str[::-1]

# Solicitar al usuario que ingrese dos números enteros
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

# Verificacion si los números son espejos
if son_espejos(a, b):
    print(f"{a} y {b} son números espejos.")
else:
    print(f"{a} y {b} no son números espejos.")