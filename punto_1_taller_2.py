#1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

def separar_digitos(n):
    digitos = []  # Lista para almacenar los dígitos
    while n > 0:
        digito = n % 10  # Obtiene el último dígito del número
        digitos.insert(0, digito)  # Inserta el dígito al inicio de la lista
        n = n // 10  # Elimina el último dígito del número
    return digitos  # Retorna la lista de dígitos

n = int(input("Ingrese un número entero: "))  # Solicita al usuario que ingrese un número entero
resultado = separar_digitos(n)  # Llama a la función para separar los dígitos del número
print("Los dígitos que componen el número son:", resultado)  # Muestra los dígitos que componen el número