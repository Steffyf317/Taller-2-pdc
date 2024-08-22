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

