#Impresion simples y con comillas
"""
print("Hola mundo") #Impresion simple
print('Otra forma de imprimir')
print("Asi podemos imprimir 'con comillas simples'")
print('Asi podemos imprimir "con comillas dobles"') #Comentario de una sola linea
"""
#Strings - Cadena de caracteres
"""
nombre = "Edgar" #forma correcta de asignar un string a una variable
nombre_2 = 'Juan' #otra forma de asignar un string a una variabla
print(nombre+" Conoce a "+nombre_2)
print("Me llamo \"Federico\"") #Es una forma de usar comillas dobles con comillas dobles fuera
print("\t Esta es una tabulacion") #Tabulacion
print('This isn\'t a number')
print('Este signo \\ es una barra invertida') #como imprimir barra invertida
print("Linea 1\nLinea 2") #Salto a la siguiente linea
print("A\tB\tC\nD\tE\tF\nG\tH\tI")
print("Barra Normal: /")
print("Barra Invertida: \\")
"""

#input
"""
input("Dime tu nombre")
input("Dime tu apellido")
print(input("Dame un dato para imprimir"))
print("Tu nombre es "+ input("Dime tu nombre")+" "+input("Dime tu apellido"))
print(input("¿Qué estás estudiando?"))
print(input("¿En qué país vives?"))
print(input("Escribe tu nombre:")+input("Escribe tu apellido:"))
"""


#Tipos de datos
""" 
Comentario multilinea
string
integer
floating
listas (coleccion ordenada de objetos) van entre corchetes
diccionario dic conjunto de pares, clave y valor, no tienen un orden con un indice, van entre llaves
tuplas van entre parentesis, ordenado pero inmutable, tienen la limitacion de no quitar ni reordenar
sets conjunto de valores unicos, van entre llaves
booleanos solo verdadero o falso


"""

#Variables
"""
edad = 30
edad2 = 15
print(edad)
print(edad+edad2)

edad3=input("Dime tu edad")
nombre1=input("Dime tu nombre")
"""

#Los nombres de las variables
"""
Una buena practica es que debe ser 
legible, tiene que tener sentido el nombre
unidad, no usar espacios, puede ser nombre_de_estudiante de forma correcta
hay que omitir la ñ y los acentos, tambien se pueden usar numeros, pero al final no al inicio
No se pueden usar signos como \ $ " y todo eso
Hay palabras reservadas que no se pueden usar como nombres de variables

"""

#Integers y floats
"""
Integers son para valores enteros
floats es para decimales

mi_numero=1
mi_numero2=5.5
mi_numero3=1.5
mi_numero4=mi_numero2+mi_numero3
print(mi_numero)
print(type(mi_numero)) #Imprime el tipo de dato contenido en la variable
print(type(mi_numero2))
print(type(mi_numero4))
#print("Vas a cumplir"+mi_numero2) # La concatenacion de caracteres, por lo tanto debe cambiarse el tipo de dato
edad=input("Dime tu edad: ") #Devuelve tipo de dato string
print(mi_numero2+mi_numero2) #Imprime suma
print(edad+edad)
"""

#Conversion de tipos de datos
#Puede haber ocasiones en los que es necesario cambiar un tipo de conversion
#Conversion implicita, python lo hace automaticamente
#Conversion explicita, el usuario lo expresa
"""
edad_integer = 15
typedata = str(type(edad_integer))
print("edad_integer es de tipo: "+typedata)
edad_integer = str(edad_integer) # de integer a string
typedata = str(type(edad_integer))
print("edad_integer es de tipo: "+typedata)
edad_integer = edad_integer+edad_integer
print(edad_integer)

#Tambien es aplicable para float a string
#Cuando se cambio de float a integer lo que hace es recortar la parte decimal, como una funcion piso


"""

#Formateo de cadenas Leccion 18
#Imprimir como string sin tener que cambiar el tipo de datos
"""
colorauto = "rojo"
matricula = 15443

#Hay dos formas de hacerlo, 1 con formato y otra con cadenas literales, es mas legible con cadenas literales.

print("Mi auto es {} y de matricula {}".format(colorauto,matricula)) #Es bueno saber este metodo por la variedad de codigo que se puede presentar
print(f"Mi auto es {colorauto} y de matricula {matricula}") #Mas usado y mas legible
"""
#Operadores matematicos Leecion 19
"""
x=6
y=2
z=7
print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido al piso de {y} es igual a {z//y}") #Division al piso
print(f"{z} modulo de {y} es igual {z%y}") #Modulo
print(f"{x} elevado a la {y} es igual a {x**y}") #Potencia x^y
print(f"la raiz cuadrada de {x} es {x**0.5}") #Raiz cuadrada

"""
#Redondeo

"""
cantidad_redondeada = round(5.211435,3) #Redondea a 3 decimales, si se omite el segundo parametro se redondea a entero de tipo entero
print(cantidad_redondeada)
"""

#Metodo Index() Leccion 27
"""
Una cadena tiene un indice que da conocer un determinado caracter 
"""
"""
mi_texto ="holoa"
print(mi_texto.index("o")) #Solo la primera vez que sale, es decir devuelve la primera posicion encontrada
print(mi_texto[4]) #h>0,o>1,l>2,o>3,a>4 Encuentra el caracter en la posicion referida
mi_texto = "Esto es una prueba"
resultado = mi_texto.index("prueba") #Busca dentro del string la posicion en la comienza el substring buscado
resultado = mi_texto.index("a",5,11) #Empieza a buscar desde la posicion 5, hasta antes de 11
resultado = mi_texto.rindex("a") #busca de derecha a izquierda
"""
#Extraer substring Leccion 28 (slicing)
"""
texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)
fragmento = texto[2:6:2] #Se obtiene desde la C hasta la posicion 6 sin incluirla y de 2 en 2, es decir tiene C
print(fragmento)
fragmento = texto[::-1] #de principio a fin, pero invertido
"""

#Metodos de string Leccion 29
"""
upper
lower
split
join
find
replace
"""
"""
texto ="Este es el texto de Federico"
resultado = texto.upper() #ESTE ES EL TEXTO DE FEDERICO
#resultado = texto.lower() #este es el texto de federico
#resultado = texto.split() #['Este', 'es', 'el', 'texto', 'de', 'Federico']
resultado = texto.split("e") #['Est', ' ', 's ', 'l t', 'xto d', ' F', 'd', 'rico']
a="Aprender"
b="Python"
c="es"
d="genial"
e="- *".join([a,b,c,d]) #Lista con cuatro elementos: Aprender- *Python- *es- *genial
resultado = texto.find("s") #la unica diferencia con index, es que cuando no encuentra el string o cadena, no devuelve error sino -1
resultado=texto.replace("Federico","todos") #Este es el texto de todos

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil","fácil").replace("mala","buena")) #Se pueden reemplazar dos cosas ala vez, reaplicando el metodo a la cadena modificada

print(e)
print(resultado)
"""

#Propiedades de los strings Leccion 30
'''#Los strings son inmutables, son concatenables, multiplicable (concatenacion varias veces), verificar si algun sub esta contenido, tambien ver la cantidad de cara con len
nombre ="Carina"
#nombre[0] = "K" Marcara error por su inmutabilidad #No permite cambiarse el string, la variable 
print(nombre) 
#La variable si se puede cambiar
nombre = """Karina
se pueden hacer saltos con los triples
""" #Saltos de linea sin necesidad de poner \n tambien funciona con comillas simples. 
print(nombre)

n1="Kari"
n2="na"
print(n1*10) #Autoconcatenacion 10 veces

#Si en un string existe algun substring

poema = """ Mil pequeños peces blancos
como si hirviera
el color del agua"""

print("sol" not in poema) #Devuelve verdadero si no lo encuentra
print("mil" in poema) #Devuelve verdadero si lo encuentra
print(len(poema)) #Devuelve numero de caracteres del string poema

'''
#Listas Leccion 31

"""
mi_lista =['a','b','c'] #Lista por extension
otra_lista=['hola',55,6.1] #Pueden contener diferentes tipos de datos
mi_lista2=['d','e','f']
print(type(mi_lista)) #tipo de dato
print(len(mi_lista)) #numero de elementos
print(mi_lista[0])
print(mi_lista[0:2]) #Imprime el elemento 0 hasta el 2 sin incluirlo, "a" y "b"
print(mi_lista+mi_lista2) #Una lista compuesta de listas, tal como la concatenacion
mi_lista3=mi_lista+mi_lista2
mi_lista3[0]='alfa'
print(mi_lista3)

#DEFINICION DE LISTAS POR COMPRENSION
#NO EN UDEMY https://www.youtube.com/watch?v=dkAjT3sDt4I"
#Listas en python por comprension
numeros = [n*2 for n in range(1,6)] #Expresion - for element - in iterable #Para todos 
#Ejemplo
"Crear lista con el numero siguiente a los numeros del 1 al 30 que sean multiplos de 7 o de 11
contiguos=[n+1 for n in range(1,31) if n%7==0 or n%11==0] #Si llevara un bloque else, va antes del for todo el condicional
print(contiguos)

#Ejemplo 2
"Crear lista con el tipo de dato, cadena, float, entero 
datos = [7,"h",2.5,"m",8.2,24,"p"]
tipos = ["cadena" if isinstance(dato,str) else
        "entero" if isinstance(dato,int) else
        "float" for dato in datos]
#No podemos usar elif, solo else 
"""
#Ejemplo3
#"Crear lista por comprension que contenga listas con todos los nombres de la lista personas y la condicion de la edad: "Mayor" si es > 30 y "Menor" si es <= 30
personas=[["Jorge",36],["Silvia",24],["Tomás",47],
            ["Irene",19],["Ignacio",24],["Julia",43],
            ["Sara",38],["Miguel",25]]
personas_2 = [[p[0],"Mayor"] if p[1] > 30 else
              [p[0],"Menor"] for p in personas]
print(personas_2)

personas_3 =[[p[0],"Mayor" if p[1]>30 else "Menor"] for p in personas]
print(personas_3)


#Ejemplo4 Listas por comprension apartir de diccionarios
inventario = {"Puntas": 30,
              "Tornillos":140,
              "Tuercas":250,
              "Arandelas":70}

pedido = [articulo for articulo in inventario if inventario[articulo]<100]
"""
#Metodos para list
mi_lista3.append("g") #Agrega un espacio y asigna un valor
print(mi_lista3)

mi_lista3.pop(0) #Si lo dejaramos sin valor interno, elimina el ultimo elemento, en este caso eliminara el primer elemento
#Tambien es posible guardar el elemento eliminado
eliminado=mi_lista3.pop(2) #Si devuelve un valor a comparacion del metodo .sort
lista=['g','o','b','m','c']
lista.sort()
print(lista)

lista.reverse() #Tampoco devuelve un valor solo ejecuta la accion.
"""


#Diccionarios Leccion 32
#Pares de datos, es una clave y un valor asociado, no pueden repetirse las claves, no hay un orden, es irrelevante
"""
mi_dic={'clave1':'Valor1','clave2':'Valor2'}
diccionario={"c1":"valor1","c2":"valor12"} #Las claves no pueden repetirse, los valores si
print(type(diccionario))
print(diccionario)
resultado = diccionario["c1"] 
print(resultado) #Despliega valor asociado a la clave c1
cliente={"nombre":"Juan","apellido":"Fuentes","peso":88}
consulta=cliente["peso"]
print(consulta)
"""
#Diccionarios y listas dentro de diccionarios
dic_1 = {"C1":55,2:[10,20,30],"C3":{"s1":100,"s2":214}}
print(dic_1[2][0]) #Busqueda tupla dentro de diccionario
print(dic_1["C3"]["s2"]) #Busqueda diccionario dentro de diccionario

#Agregando elementos
dic_1[3]=342 #Agrega clave y asigna valor
dic_1["C3"]["s1"]=101

#Obteniendo items, claves, valores
print(dic_1.items()) #Devuelve tuplas
print(dic_1.keys()) 
print(dic_1.values())

#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

'''#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y
agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
nombre: Karen
apellido: Jurgens
edad: 36
ocupacion: Editora
pais: Colombia'''

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["nombre"]="Karen"
mi_dic["apellido"]="Jurgens"
mi_dic["edad"]=36
mi_dic["ocupacion"]="Editora"
mi_dic["pais"]="Colombia"