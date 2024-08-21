#7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

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