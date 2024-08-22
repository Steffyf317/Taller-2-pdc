# Taller 2 Programación de computadores
## Presentado por el grupo: Los 7 pecados de la programación:
### ·Steffy Geraldine Fernández González
### ·Andrés Felipe Sánchez Gómez 
### ·Nilson Daniel Dueñas López

## 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
#### Se desarrolló la función separar_digitos para descomponer un número entero en sus dígitos individuales. Dentro de la función, se iteró sobre el número, obteniendo el último dígito y eliminándolo en cada paso, insertando cada dígito en una lista.
```python
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
```

## 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
####
```python
def separar_digitos(n):
    parte_entera = int(n)  # Obtiene la parte entera del número
    parte_decimal = str(n).split('.')[1] if '.' in str(n) else ''  # Obtiene la parte decimal del número como cadena

    # Separa los dígitos de la parte entera
    digitos_entera = []
    while parte_entera > 0:
        digito = parte_entera % 10
        digitos_entera.insert(0, digito)
        parte_entera = parte_entera // 10

    # Separa los dígitos de la parte decimal
    digitos_decimal = [int(d) for d in parte_decimal] if parte_decimal else [0]

    return digitos_entera, digitos_decimal

n = float(input("Ingrese un número flotante: "))
digitos_entera, digitos_decimal = separar_digitos(n)

print("Los dígitos de la parte entera son:", digitos_entera)
print("Los dígitos de la parte decimal son:", digitos_decimal)
```

## 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
####
```python
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
```

## 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
####
```python
import math

def aproximacion_coseno(x, terminos):
    # Se normalizó el valor de x para que esté dentro del rango [0, 2π).
    x = x % (2 * math.pi)
    cos_x = 0
    
    # Se calculó la serie de Taylor para el coseno hasta el número de términos especificado.
    for i in range(terminos):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        cos_x += term
    
    return cos_x

def n_terminos(x, m_list):
    # Se calculó el valor real del coseno de x utilizando la función incorporada de Python.
    real = math.cos(x)
    results = []

    # Para cada valor de m en la lista, se encontró el número de términos necesario para lograr el error relativo deseado.
    for m in m_list:
        n = 1
        aproximacion = aproximacion_coseno(x, n)
        z = abs((aproximacion - real) / real) * 100

        # Se ajustó el número de términos hasta que el error relativo fue menor que m.
        while z > m:
            n += 1
            aproximacion = aproximacion_coseno(x, n)
            z = abs((aproximacion - real) / real) * 100

        # Se almacenaron los resultados correspondientes a cada valor de m.
        results.append((m, n, aproximacion, z))

    return results

x = float(input("Ingrese el valor de x: "))
m_list = [10, 1, 0.1, 0.001]
real = math.cos(x)
resultados = n_terminos(x, m_list)

# Se imprimieron los resultados para cada valor de m en la lista.
for m, terminos, aproximacion, z in resultados:
    print(f"\nPara un error relativo menor a {m}%:")
    print(f"El aproximado del coseno de x es: {aproximacion}")
    print(f"El valor real del coseno de x es: {real}")
    print(f"Los términos necesarios son: {terminos}")
    print(f"Error relativo (%): {z}")
```
## 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
#### Primero, se crea una función donde se utilizan dos casos bases del algoritmo de Euclides, y es que se establece la división entre dos números (el más grande entre el pequeño), donde el residuo pasa a ser el segundo número iterativamente, con lo que se obtiene finalmente el máximo común divisor y, con este se calcula el mínimo común múltiplo:
```python
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
  ```
 ## 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.
 #### Aquí básicamente se crea una lista auxiliar que guarda elementos únicos, ya que al recorrer la lista digitada por el usuario, se compara el elemento n con el n anterior, si son iguales quiere decir que si tiene elementos repetidos:
 ```python
 def existencia_elementos_repetidos (lista):
  lista_elementos_unicos = [] #lista auxiliar

  for i in lista: #para cada elemento en lista(esta se muestra abajo, fuera de la función)
    if i in lista_elementos_unicos: #si el elemento ya está en la lista auxiliar, hay elementos repetidos
      return True
    lista_elementos_unicos.append(i) #Agregar los elementos a la lista auxiliar

  return False

if __name__ == "__main__":
  n = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo ")) #se ingresa por teclado la cantidad que el usuario quiera
  lista = [] #se crea una lista vacía

  for i in range (n): #para cada elemento dentro del rango de n:
    a = (input("Ingrese el elemento #" +str(i+1)+ " para el arreglo "))  #preguntar qué elementos irán dentro del arreglo
    lista.append(a) #agregar dichos elementos en la lista creada anteriormente
  print(f"La lista tiene elementos repetidos?: {existencia_elementos_repetidos(lista)}")
  ```
## 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
#### Aquí se usa una función que incorpora una lista con los valores ASCII para las vocales y asimismo, un contador de vocales, que retorna la función si el contador es mayor o igual a 2:
```python
def dos_o_mas_vocales(lista):
  vocales:int = 0 #se inicia en 0 un contador de vocales
  valor_ascii_vocales:list = [65,69,73,79,85,97,101,105,111,117] #se establece una lista con los valores ASCII de las vocales minúsculas y mayúsculas

  for i in lista: #para cada elemento de la lista con valores digitados del usuario
    for b in i: #se toma cada valor de la lista como una sublista (ya que se ingresan como strings y estos son arreglos)
      if ord(b) in valor_ascii_vocales:
        vocales +=1 #se compara la lista con valores del usuario y la de valores ASCII
      if vocales >= 2:
        print(lista)
        return  #se retorna la función si se cumple la condición de tener dos o más vocales
  print("No existe")


if __name__ == "__main__":
  n = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo ")) #se ingresa por teclado la cantidad que el usuario quiera
  lista = [] #se crea una lista vacía

  for i in range (n): #para cada elemento dentro del rango de n:
    a = str(input("Ingrese el elemento #" +str(i+1)+ " para el arreglo "))  #preguntar qué elementos irán dentro del arreglo
    lista.append(a) #agregar dichos elementos en la lista creada anteriormente
  dos_o_mas_vocales(lista)
```
## 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
#### Básicamente lo que se hace es comparar elementos entre las dos listas con la palabra reservada 'not':
```python
def elementos_primera_lista_no_en_segunda (lista_1,lista_2):
  for i in lista_1:
    if i not in lista_2: #se comparan elementos entre las dos listas
      print(i)
      return
  print("Todos los elementos de la primera lista están en la segunda ")

if __name__ == "__main__":
  n = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo 1 ")) #se ingresa por teclado la cantidad que el usuario quiera
  m = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo 2 "))
  lista_1 = [] #se crea una lista vacía
  lista_2 = []
  for i in range (n): #para cada elemento dentro del rango de n:
    a = str(input("Ingrese el elemento #" +str(i+1)+ " para el arreglo 1 "))  #preguntar qué elementos irán dentro del arreglo
    lista_1.append(a) #agregar dichos elementos en la lista creada anteriormente
  for j in range (m):
    b = str(input("Ingrese el elemento #" +str(j+1)+ " para el arreglo 2 "))
    lista_2.append(b)
  elementos_primera_lista_no_en_segunda(lista_1,lista_2)
  print(lista_1) #se imprimen las listas para verificar
  print(lista_2)
```
## 9. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

#### Simplemente se siguio el mismo planteamineto de cada problema con las fuinciones de vectortes, acortando las operaciones significativamente al taller 1 
```python
#9. 
listNum = []
numRef = float

# Pedir los 5 numeros a añadir en la lista
for i in range(5):
    listNum.append(float(input(("Ingrese el " + str(i+1) +" número: "))))

#Promedio
print("El promedio es: "+str(sum(listNum)/len(listNum)))

#Mediana
listNum.sort()
print("La Mediana es :"+str(listNum[2]))

#Promedio multiplicativo
mult = 1
for num in listNum:
    mult *= num
print("El Promedio multiplicativo es : "+f"{(mult**(1/len(listNum))):.4f}")

#Orden
print("El Oreden Ascendente es : "+str(listNum))

#Orden reverso
print("El Oreden Descendente : "+str(sorted(listNum,reverse=True)))

#Potencia del mayor al menor
print("Potencia del mayor al menor "+str(listNum[4])+"^"+str(listNum[0])+" es :"+str(listNum[-1]**listNum[0]))

#La raíz cúbica del menor número
print("La raíz cúbica del menor número es : "+str(listNum[0]**(1/3)))
```

## 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser *retornada* por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. 
####  Con comprension de listas se creo una funcion que recorre la matriz dada y escoje solo los multiplos de 3 para retornar una nueva lista con estos multilpos
### *El desafio consistia de hallar la manera de encontrar multiplos de 3 sin usar modulo, en la investigacion previa, la unica otra manera de encontrar estos multiplos es sumando los digitos del numero y si esos digitos sumados son multiplos de 3 el numero ortiginal sera multiplo de 3, con esto en mente no encontramos manera de no usar el modulo, dado que para hallar si la suma de los digitos es multiplo usariamos el modulo.
```python
#Funcion para crear una lista que solo tenga los multipos de 3
def listMod(x):
    listB = [i for i in x if i%3==0] #loop atraves de la matriz y solo añadir si el modulo%3 es 0
    return listB 

if __name__ == "__main__": 
    listNum = []
    #Pedir al cantidad de numeros a valorar
    cantidad=int(input(("Ingrese la cantidad de numeros a valorar : ")))
    # Pedir los numeros a añadir en la lista
    for i in range(cantidad):
        listNum.append(float(input(("Ingrese el " + str(i+1) +" número: "))))
    #print con la funcion de multiplos
    print(listMod(listNum))
```
### Bono
11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
### Se recorren las filas, columnas y diagonales, cada una con un ciclo de comparacion el cual se encarga de marcar si la suma es magica, la cual se evalua al final
```python

c=int(input(("Ingrese el tamaño de la matriz cuadrada a valorar: ")))
# Pedir los numeros a añadir en la lista
magica=[[int(input(f"Ingrese el valor para[{x}][{y}]")) for x in range (c)] for y in range(c)]

print(magica)
comparador=int=0
comparador2=int=0
comparadorHorizontal=int=0
comparadorVertical=int=0
comparadorDiagonal=int=0
 
#recorre la matriz horizontalmente, usando comparadores entre ciclos para guardar informacion
#cada ciclo comparara la suma horizontal y si esta falla se cancela el ciclo 
for i in range(c):
     comparador2=comparador
     comparadorHorizontal=comparador2
     if comparadorHorizontal!=comparador2:
         break
     comparador=0
     for j in range (c):
         comparador+=magica[i][j]
print("Horizontalmente : "+str(comparadorHorizontal))
#recorre la matriz verticalmente, usando comparadores entre ciclos para guardar informacion
#cada ciclo comparara la suma y si esta falla se cancela el ciclo 
for i in range(c):
    comparador2=comparador
    comparadorVertical=comparador2
    if comparadorVertical!=comparador2:
        break
    comparador=0
    for j in range (c):
        comparador+=magica[j][i]
print("Vertical : "+str(comparadorHorizontal))
#recorre la matriz diagonalmente, usando comparadores entre ciclos para guardar informacion
#cada ciclo comparara la suma y si esta falla se cancela el ciclo 
for i in range(c):
    comparador2=comparador
    comparadorDiagonal=comparador2
    if comparadorDiagonal!=comparador2:
        break
    comparador=0
    for j in range (c):
        comparador+=magica[i][i]
print("Diagonal :"+str(comparadorDiagonal))
#comparador de los 3 calores de las sumas, considerando que cada suma ya paso su respectivo comparador
if comparadorDiagonal==comparadorDiagonal==comparadorHorizontal :print("Es Magica, la suma es : "+str(comparadorDiagonal)) 
else: print("No es Magica")
```

  
