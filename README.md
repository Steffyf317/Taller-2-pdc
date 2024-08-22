# Taller 2 Programación de computadores
## Presentado por el grupo: Los 7 pecados de la programación:
### ·Steffy Geraldine Fernández González
### ·Andrés Felipe Sánchez Gómez 
### ·Nilson Daniel Dueñas López

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


  
