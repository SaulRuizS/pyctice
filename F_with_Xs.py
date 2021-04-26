numbers = [5,2,5,2,2]

for number in numbers:              #Iteracion de numero en numero dentro de la lista "numbers"
    line = ""                       #Por cada iteracion se vuelve a inicializar la linea
    for unit in range(number):      #Iteracion por cada unidad dentro del rango del numero actual
        line = line + "X"           #Por cada iteracion se concatena el caracter 'X'
    print(line)                     #Se imprime el resultado de cada linea