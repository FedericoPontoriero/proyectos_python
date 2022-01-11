
nombre1 = input('Cuál es tu nombre? ')
edad1 = int(input('Cuál es tu edad? '))
saludo = f'Hola {nombre1}, tienes {edad1} años.'
print(saludo + ' Sabías que este texto tiene ', len(saludo), 'caracteres?')

nombre2 = input('Dame el nombre de alguien conocido ')
edad2 = int(input('Qué edad tiene? '))

if edad1 > edad2:
    compedades = edad1 - edad2
    print(f'Sabías que eres mayor que {nombre2} por {compedades} años?')
elif edad1 < edad2:
    compedades = edad2 - edad1
    print(f'Sabías que eres menor que {nombre2} por {compedades} años?')
else:
    print(f'{nombre2} y tú tienen la misma edad!')






hora = 0
minuto = 0
segundo = 0  

while hora < 24:
    while minuto < 60:
        while segundo < 60:
            print(hora, minuto, segundo)
            segundo += 1
        minuto += 1
        segundo = 0
    hora += 1
    minuto = 0





from time import time
def raiz():
  tiempo_total = 0
  objetivo =int(input('Escoge un numero'))
  tiempo_inicial = time() 
  epsilon = 0.01
  paso = epsilon**2
  respuesta = 1.0
  while abs(respuesta**2 - objetivo )>= epsilon and respuesta <= objetivo:
    respuesta += paso 
  if abs(respuesta**2 - objetivo ) >= epsilon:
    print(f'No se encontro la raiz cuadrada  {objetivo}')

  else:
      print(f'La Raiz cuadrada de  {objetivo} es {respuesta}')
  tiempo_final = time() 
  tiempo_total = tiempo_final -tiempo_inicial 
  print(f'el tiempo fue de : {tiempo_total}')

raiz()





import time

objetivo = float(input('Escoge un numero: '))
if objetivo < 0:
    print('Los números negativos no están soportados')
    exit()
epsilon = 0.000001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo)/2
num = 0 #numero para contar iteraciones

start = time.time()

while abs(respuesta**2 - objetivo) >= epsilon:

    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo)/2

    num += 1

end = time.time()

print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')

print(f'La raiz cuadrada de {objetivo} es {respuesta}') 




def opciones():
  print(f'Opciones para hallar raiz cuadrada \n (1) Enumeracion exhaustiva \n (2) Aproximacion de soluciones \n (3) Busqueda binaria') 
  opcion = int(input('Elija una opcion: '))
  numero = int(input('Elija un numero: '))
  if opcion==1:
    Enumeracion(numero)
  elif opcion==2:
    Aproximacion(numero)
  elif opcion==3:
    BusquedaBinaria(numero)
  else:
    print('Elija 1, 2 o 3')

def Enumeracion(objetivo):
  respuesta = 0

  while respuesta**2 < objetivo:
      print(respuesta)
      respuesta += 1

  if respuesta**2 == objetivo:
      print(f'La raiz cuadrada de {objetivo} es {respuesta}')
  else:
      print(f'{objetivo} no tiene una raiz cuadrada exacta')

def Aproximacion(objetivo):
  epsilon = 0.001
  paso = epsilon**2 
  respuesta = 0.0

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
      print(abs(respuesta**2 - objetivo), respuesta)
      respuesta += paso

  if abs(respuesta**2 - objetivo) >= epsilon:
      print(f'No se encontro la raiz cuadrada {objetivo}')
  else:
      print(f'La raiz cudrada de {objetivo} es {respuesta}')


def  BusquedaBinaria(objetivo):
  epsilon = 0.001
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2

  while abs(respuesta**2 - objetivo) >= epsilon:
      print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
      if respuesta**2 < objetivo:
          bajo = respuesta
      else:
          alto = respuesta

      respuesta = (alto + bajo) / 2
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')

opciones()

def factorial(n):
    """
    Calcula el factorial de n
    n int > 0
    return !n
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)
n = int(input('Escribe un entero'))
print(factorial(n))

my_tuple = (1, 2, 3)
print(my_tuple)

impar = range (1,100,2)

for i in impar:
    print (i)

def nones():
    for i in range(1, 100):
        if i % 2 != 0:
            print(i)

nones()

"""
Listas:
lista.append #agrega un elemento
lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
lista.pop(i) #Elimina valor en la posición i de la lista.
lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
lista.clear() #Borra elementos en la lista.
lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
lista.sort() #Ordena los elementos de mayor a menor.
lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
lista.reverse() #Invierte los elementos
lista.copy() #Genera una copia de la lista. También útil para clonar listas.
Crear una lista:
mylist = ['one', 20, 5.5, [10, 15], 'five']

listas mutables:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[2] = "New item"
Si el índice es negativo, cuenta desde el último elemento.
elem = mylist[-1]

Recorrer una lista:
for elem in mylist:
print(elem)

Actualizar elementos:
mylist = [1, 2, 3, 4, 5]
for i in range(len(mylist)):
    mylist[i]+=5
print(mylist)

mylist = ['one', 20, 5.5, [10, 15], 'five']
print(len(mylist))

Cortar una lista:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[1:3] = ['Hello', 'Seven']
print(mylist)

Insertar en una lista:
mylist = [1, 2, 3, 4, 5]
mylist.insert(1, 'Hello')
print(mylist)

Agregar a una lista al final:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist.append("new one")

mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ["Hello", "new one"]
mylist.extend(list2)
print(mylist)

Ordenar una Lista:
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
list = [3, 5, 2, 4, 1]
mylist.sort()
list.sort()
print(mylist)
print(list)

Invertir una lista:
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)

Indice de un elemento:
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist.index('two'))

Eliminar un elemento:
mylist = ['one', 'two', 'three', 'four', 'five']
removed = mylist.pop(2)
print(mylist)
print(removed)

mylist.remove('two')
del mylist[2]

mylist = ['one', 'two', 'three', 'four', 'five']
del mylist[1:3]
print(mylist)

Funciones agregadas:
mylist = [5, 3, 2, 4, 1]
print(len(mylist))
print(min(mylist))
print(max(mylist))
print(sum(mylist))

Comparar listas:
mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ['four', 'one', 'two', 'five', 'three']
if (mylist == list2):
     print("match")
else:
     print("No match")

Operaciones matematicas en las listas:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
print(list1 * 2)

Listas y cadenas:
mystr = "LikeGeeks"
mylist = list(mystr)
print(mylist)

mystr = "LikeGeeks"
mystr = "Welcome to likegeeks website"
mylist = mystr.split()
print(mylist)

Unir una lista:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
delimiter = ' '
output = delimiter.join(mylist)
print(output)

Aliasing:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
list2 = mylist
list2[3] = "page"
print(mylist)
"""


