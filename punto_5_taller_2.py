# 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

def maximo_comun_divisor (a,b)->int:
  while a > b and b != 0: #se establecen los casos bases del algoritmo de Euclides
    r = a % b #Se define el residuo de la división entre los dos números enteros que digita el usuario
    a = b #Se actualiza el valor de la variable a, dado que este pasará a ser el segundo número iterativamente
    b = r #Al hacer las iteraciones, el residuo pasa a ser el segundo numero, es decir, el divisor
  return a #con Euclides, se tiene que el número que quede como dividendo cuando el residuo sea igual a 0, este será el maximo comun divisor.

if __name__ == "__main__":
  texto_inicial_para_usuario = input("Luego de presionar enter, digite dos números, el primero mayor que el segundo ")
  a = int(input("Digite el primer número entero ")) #Valores pedidos al usuario
  b = int(input("Digite el segundo número entero "))
  mcd = maximo_comun_divisor(a,b) #se crea una variable que guarda el retorno de la funcion del maximo comun divisor
  mcm = abs(a*b)//mcd #se calcula el mínimo común múltiplo a partir del máximo común divisor
  print("El mínimo común múltiplo de " +str(a)+ " y " +str(b)+ " es " +str(mcm))