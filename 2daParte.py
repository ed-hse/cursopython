#Tuplas Leccion 33
#Coleccion de elementos que son inmutables, llevar parentesis
#Ocupan menos espacio de memoria
#A prueba de daños dado que no pueden ser modificadas
'''
mi_tuple=(1,2,3,4)
print(type(mi_tuple))

t=(5,5.6,"string") #Puede contener diccionarios, tuplas y listas
#mi_tuple[0]=5

#Si se pueden anidar
mi_tuple=(1,2,(10,20),4)
print(mi_tuple[2][0]) #Imprime 10
mi_tuple = list(mi_tuple)
print(type(mi_tuple)) #Se ha cambiado una lista
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))# se cambia a tuple

t=(1,2,3,1)
x,y,z,q=t #Si se puede al ser el mismo numero de elementos, tambien se puede con listas y diccionarios
print(x,y,z,q) #Solo si es el mismo numero de elementos
print(len(t))
print(t.count(1)) #Va a contar 2 veces el 1
print(t.index(2)) #regresa la posicion del 2 es decir el 1

"""
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
"""
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

"""
Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
"""
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista=list(mi_tupla)

"""
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
"""
mi_tupla = (1, 2, 3, 4)
a,b,c,d=mi_tupla

'''
#Sets Leccion 34
"""#No pueden contener listas ni diccionarios, por que los set son inmutables

mi_set=set([1,2,3,4,5]) #Funciona con parentesis, corchetes, o llaves set({}),set(())
print(type(mi_set))
print(mi_set)

otro_set={1,2,3}
print(type(otro_set))
print(otro_set)

#Los set solo tienen elementos unicos, cuando ponemos elementos repetidos se descartan
#No pueden contener listas ni tampoco diccionarios porque esos si aceptan elementos repetidos, pero si admite tuples por ser inmutables

print(len(otro_set))
print(2 in otro_set)

s1 ={1,2,3}
s2 ={3,4,5}
s3 = s1.union(s2)
s1.add(4) #Agrega elementos al set
s1.remove(3) #Si funciona, pero si eliminamos uno que no esta marcara error
s1.discard(2) #Si funcion aun si eliminamos uno que no esta dentro del set
#s1.pop() #Elimina al azar sin argumentos
elemento_eliminado= s1.pop()
#s1.clear() #Borra todos los elementos del set, queda un set vacio
print(s3)
"""

#Booleanos Leccion 35
#Se puede agregar tambien de forma indirecta
#mayor que, menor que, igual que, != desigual
'''
var1=True
var2=False
#Modos expresos

print(type(var1))
print(var1)

numero= 5>2+3
print(type(numero))

numero = bool(4>4) #Es explicitamente, tambien es posible encontrarlo en variedad de codigo
numero =bool() #Falso por default

lista = [1,2,3,4]
control = 5 in lista #Otra forma de construir booleanos
print(type(control)) #Booleano
'''
#Operadores de comparacion Leccion 41
#Se obtendra Falso o Verdadero
'''
mi_bool= 5+5 == 18-8
print(mi_bool) #Verdadero

mi_bool = "Blanco" == "blanco" #Falso
mi_bool = "Blanco".lower() == "blanco" #Verdadero
mi_bool = 100.0 == 100 #Aun si son diferentes tipos de datos para este cas, pero string "100" == 100 ahi si da falso

#Operadores
mi_bool = "blanco"=="blanc" and 5>1
print(mi_bool) 
mi_bool = not ("blanco"=="blanc") and 5 > 1 or 5==5-5+5
print(mi_bool)
'''
#Control de flujo Leccion 43
'''
if 10>9:
    print("Es correcto")

mascota ="perro"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("No se que animal tienes")
'''
#Introduccion a los loops 44
#Loop For
#Bloque de codigo a repetir su ejecución
#Algunos objetos son iterables
#for y while
'''
nombres = ["Juan","Ana","Carlos","Belen","Fran"]
# por cada elemento en nombre imprimir Hola.
#for elemento in nombre:
#   print("Hola") #elemento es una variable interna

lista  = ["a","b","c"]

for letra in lista: #el nombre de la variable letra es solo por temas de legibilidad, pero no es necesario.
    numero_letra=lista.index(letra)+1
    print(f"Letra: {letra}, en la posicion {numero_letra}")

lista = ["pablo","laura","fede","luis","julia"]
for nombre in lista:
    if nombre.startswith("l"):
        print(f"{nombre} comienza con l")
    else:
        print(f"{nombre} no comienza con l")

'''

#Loop While Leccion 46
#Es esencial que se cumpla mientras se cumple una condicion
#mientras que: 
#   Ejecucion
#else: si la condicion no se cumple, break continue y pass palabras clave para este loop
"""
monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    #monedas=monedas-1
    monedas-=1 #forma compacte
else:
    print("No tengo mas dinero")


respuesta ="s"

while respuesta=="s":
    respuesta=input("Quieres seguir (s/N))").lower()
else:
    print("Gracias")

respuesta = "s"
while respuesta == "s":
    pass #Un espacio para no hacer nada #Como un ticket que ayuda al programador a reservar el lugar

nombre=input("Tu nombre: ")
for letra in nombre:
    if letra=="r":
        break #Con eso interrumpe el loop completo
    print(letra)


nombre=input("Tu nombre: ")
for letra in nombre:
    if letra=="r":
        continue #Con eso interrumpe el loop completo
    print(letra)

"""

#Rango Leccion 47
#Sirve para crear un rango de numeros para iterar sobre ellos sin necesidad de crear una lista o algun otro contenedor iterable
"""
for number in range(10): #rango comienza por defecto desde el 0, en este caso llega hasta el 9 incluyendolo
    print(number)

for number in range(20,30): #rango comienza 20 y llega al 29
    print(number)

for number in range(10,100,2): #de 10 a 99 en pasos de 2
    print(number)

lista=list(range(1,21)) #Tambien sirve para crear listas de forma rapida
print(lista)
"""
#Enumerador Leccion 48
#Es una herramienta para acceder a los indices de un arreglo
"""
lista = ["a","b","c"]
indice =0
for item in lista:
    print(indice, item)
    indice +=1
#Esta no es la mejor manera de encontrar los indices"""

#Es mejor usando enumerate
"""
lista = ["a","b","c"]

for item in enumerate(lista): #el enumerador devuele una serie de tuples #Es un objeto iterador
    print(item)

for indice,item in enumerate(lista): #el enumerador devuele una serie de tuples 
    print(indice,item)

#Tambien para convertir una lista en una lista de tuples que tienen indice-valor
mis_tuples=list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])
"""

#Zip Leccion 49 
#Se tienen varias listas, y se combinan en una lista de tuplas, crea un objeto iterador formado por los elementos agrupados del mismo indice provenientes de dos o mas iterables.
"""nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]
ciudades = ["Lima","Madrid","Mexico"]

combinados = list(zip(nombres,edades,ciudades)) #Zip llega hasta el largo de la lista mas corta 
#Formo una lista compuesta de tuplas
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre}, tiene {edad} años y vive en {ciudad}")


#Min y Max 50
menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)

nombres =["juan","pablo","alicia","carlos"]
print(min(nombres))

nombre="carlos"
print(min(nombre))
nombre="Carlos"
print(min(nombre)) #Busca primero en mayusculas

dic={"C1":45,"C2":11}
print(min(dic)) #Imprime la clave mas pequeña

print(min(dic.values())) #Imprime el valor mas pequeño"""

#Random Leccion 51
#from random import randint #Es importante que el nombre del archivo no tenga el mismo nombre que la libreria
"""
from random import * # Es una forma de importar todos los metodos desde la libreria
# 
aleatorio = randint(1,50) #Valor aleatorio de tipo entero
print(aleatorio)

aleatorio = uniform(1,5) #Valor aleatorio de tipo decimal/flotante
print(aleatorio)

aleatorio = random() #Elije un decimal entre 0 a 1
print(aleatorio)

colores = ["azul","rojo","verde","amarillo"]
aleatorio = choice(colores) #Elije un elemento de la lista

numeros=list(range(5,50,5)) 
shuffle(numeros) #Ordena de forma aleatoria #Es in situ
print(numeros)

"""



#Comprension de listas Leccion 52
#Mas eficiente menos legible
"""
palabra ="python"
lista=[]
for letra in palabra:
    lista.append(letra)
print(lista)

#Hay una forma mas compacta
palabra2 = "paraguas"
lista=[letra for letra in palabra2]

pies=[10,20,30,40,50]
metros=[p/3.281 for p in pies]
print(metros)

lista =[n for n in range(0,21,2) if n*2>10] #Manera de incluir el condicional

lista =[n if n*2>10 else "no" for n in range(0,21,2)] #Manera de incluir condicional con else

#Ejemplos
#Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado =[n**2 for n in valores]

#Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n%2 == 0]

#Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. 
temperatura_fahrenheit = [32, 212, 275]
grados_celsius =[(t-32)*(5/9) for t in temperatura_fahrenheit]
"""
#Match Leccion 54
#A partir de la actualizacion de python 3.10
# Su utilidad ademas del uso como switch case, tambien sirve para cuando una estructura tiene determinada forma.
"""
#Uso como switch
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe este producto {serie}") 
   

#Uso para compara estructura

cliente ={"nombre": "Federico",
          "edad":45,
          "ocupacion":"instructor"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica":{"protagonista":"Keanu Reeves",
                             "director":"Lana y Lilly Wachoski"}}

elementos = [cliente, pelicula,"libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad":edad,
              "ocupacion": ocupacion}: #Si se coincide con esta estructura
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo":titulo,
              "ficha_tecnica":{"protagonista":protagonista,
                               "director":director}}: #Si se coincide con esta estructura
            print("Es una pelicula")
            print(titulo, protagonista,director)
        case _: #Por Default
            print("No se que es esto")
            
"""

#Proyecto del Dia 4
"""
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir 
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos 
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un 
número y el programa puede responder cuatro cosas distintas: 
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido 
un número que no está permitido. 
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a 
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto. 
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la 
misma manera. 
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos 
intentos le ha tomado. 
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro 
número. Y así hasta que gane o hasta que se agoten los ocho intentos. 
"""

""" #Intento de codigo.
from random import *
nombre_usuario = input("Hola bienvenido al juego, cual es tu nombre")
print(f"Bueno, {nombre_usuario}, he pensado un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cual crees que sea el numero")
numero_ganador = randint(1,100)
left_try = 8

for i in range(1,9):
    guess = int(input(f"cual crees que sea? te quedan {left_try} intentos: \n"))
    if guess == numero_ganador:
        print(f"Felicidades, acertaste en {i} intentos, te restaban {left_try-i} intentos")
        break
    if guess < 1 or guess > 100:
        print(f"Has elegido un numero que no esta permitido, te restan {left_try-i} intentos")
    if guess > numero_ganador:
        print(f"Has elegido un numero mayor que el numero secreto, sigue intentando, te quedan {left_try-i} intentos")
    if guess <numero_ganador:
        print(f"Has elegido un numero menor que el numero secreto, sigue intentando, te quedan {left_try-i} intentos")
    left_try=left_try-1
    if i == 8:
        print("Se te han agotado todos los intentos! :( que pena")
"""

#Metodos, Ayuda y Documentacion
"""
Es necesario consultar la ayuda contextual como por ejemplo en pycharm, las ayudas de visual studio code, tambien podemos
ver la documentacion oficial de python. Todos los objetos tienen muchos metodos. Es importante buscar e interpretar el significado de los diferentes metodos.

"""

#Funciones Leccion 60
#Crear funciones 61
'''
def mi_funcion(nombre):
    """
    Esta es una funcion que se encarga
    de imprimir un saludo en pantalla #ES USUAL ESCRIBIR UNA DESCRIPCION DE LA FUNCION COMO FORMA DE DOCUMENTAR
    """
    print(f"Esta es mi primera funcion, Hola {nombre}")
    
mi_funcion("Luis")

def saludar_persona():
    """
    Esta funcion sirve para saludar
    a las personas y etceteda
    """
    print("Hola")

saludar_persona()
saludar_persona()
'''


#Return Leccion 62
#Podemos retornar un valor para imprimir o bien almacenar en una variable
"""
def multiplicar(numero1, numero2):
    return numero1*numero2

print(multiplicar(3,4))
resultado = multiplicar(5,10) #La funcion esta contemplada que tome valores integers y floats,
#en un caso general: espera que el usuario introduzca el tipo de datos correcto


print("Prueba 05/08/2024 - 11 p.m.")

"""
#Funciones dinamica Leccion 63
"""
def chequear_3_cifras(numero):
    return numero in range(100,1000) #Verifique que esta dentro del rango, devuelve True o False

resultado = chequear_3_cifras(658)
print(resultado)


def chequear_3_cifras_listas(lista): #Devuelve True o None
    for n in lista:
        if n in range(100,1000):
            return True #Esta en el medio, termina la funcion con solo esta sentencia de "escape"
        else:
            pass
    #return False #Si se quisiera que en lugar de None, devolviera false cuando no hay ningun elemento, se pone este return
def chequear_3_cifras_listas_each(lista): #Devuelve todos los elementos de la lista que cumplen
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
"""

#Ejemplo de funcion Leccion 64
"""
precios_cafe=[("capuchino",1.5),("Expreso",1.2),("Moka",1.9)]
for elemento in precios_cafe:
    print(f"imprimimos la tupla: {elemento}")

def cafe_mas_caro(lista_precios): #Devuelve el cafe mas caro
    precio_mayor = 0
    cafe_mas_caro =""
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass

    return(cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")
"""

#Interaccion entre Funciones Leccion 65
#Muchas funciones interactuando entre si.


#Eliges 1 palito, si te toca el mas corto lavas trastes.
"""
from random import shuffle

#Lista inicial
palitos = ["-","--","---","----"]
#Funcion mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


#print(mezclar(palitos))
#Pedirle intento 
def probar_suerte():
    intento=""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4:")
    return int(intento)


#Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados=mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
"""

#Ejercico de codificacion 
"""
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. 
El orden de los elementos puede modificarse.
Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
"""
'''
def reducir_lista(lista):
    # Eliminar duplicados convirtiendo la lista a un conjunto
    lista_unica = list(set(lista))
    # Encontrar el valor máximo
    max_valor = max(lista_unica)
    # Eliminar el valor máximo de la lista
    lista_reducida = [x for x in lista_unica if x != max_valor]
    return lista_reducida

def promedio(lista):
    if not lista:  # Evitar división por cero si la lista está vacía
        return 0
    return sum(lista) / len(lista)

# Variable de ejemplo
lista_numeros = [1, 2, 15, 7, 2]

# Usar las funciones
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

print("Lista original:", lista_numeros)
print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", resultado_promedio)'''

#Ejercicio de codificacion
"""
Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. 
El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
"""

"""
from random import choice
def lanzar_moneda():
    return choice(["Cara","Cruz"])

def probar_suerte(resultado_moneda,lista_numeros):
    if resultado_moneda=="Cara":
        print("La lista se autodestruirá.")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
    
lista_numeros = [1,42,123,13,45,4]
"""

