
c=int(input(("Ingrese el tamaño de la matriz cuadrada a valorar: ")))
# Pedir los numeros a añadir en la lista
magica=[[int(input(f"Ingrese el valor para[{x}][{y}]")) for x in range (c)] for y in range(c)]
#for i in range(c):
#    for j in range (c):
#        magica.append(int(input(("Ingrese el " + str(i+1) +" número: "))))
print(magica)
comparador=int=0
comparador2=int=0
comparadorHorizontal=int=0
comparadorVertical=int=0
comparadorDiagonal=int=0
 
 
for i in range(c):
     comparador2=comparador
     comparadorHorizontal=comparador2
     if comparadorHorizontal!=comparador2:
         break
     comparador=0
     for j in range (c):
         comparador+=magica[i][j]
print("Horizontalmente : "+str(comparadorHorizontal))
for i in range(c):
    comparador2=comparador
    comparadorVertical=comparador2
    if comparadorVertical!=comparador2:
        break
    comparador=0
    for j in range (c):
        comparador+=magica[j][i]
print("Vertical : "+str(comparadorHorizontal))
for i in range(c):
    comparador2=comparador
    comparadorDiagonal=comparador2
    if comparadorDiagonal!=comparador2:
        break
    comparador=0
    for j in range (c):
        comparador+=magica[i][i]
print("Diagonal :"+str(comparadorDiagonal))

if comparadorDiagonal==comparadorDiagonal==comparadorHorizontal :print("Es Magica, la suma es : "+str(comparadorDiagonal)) 
else: print("No es Magica")