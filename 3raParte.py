#Argumentos indefinidos *args Leccion 66
#La expresion args podemos definir funciones genericas, que se adapten al numero de argumentos que el usuario quiera pasar.
#en realidad es una practica comun llamarle args, pero puede ser otra palabra, con que tenga un asterisco
'''
#Por ejemplo una suma de elementos
def suma(*args): #Es una convencion usar la palabra "args", es recomendable
    total = 0

    for arg in args: #Iterable
        total += arg
    return total

print(suma(4,5,3,5,2,4,55,55553))

#Devuelve la suma de los cuadrados
def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total = total + arg**2
    return total

#Devuelve la suma de los valores absolutos
def suma_absolutos(*args):
    total =0
    for arg in args:
        total = total + abs(arg)
    return total
    
"""
Crea una función llamada numeros_persona que reciba, como primer argumento,
 un nombre, y a continuación, una cantidad indefinida de números.
La función debe devolver el siguiente mensaje:
"{nombre}, la suma de tus números es {suma_numeros}"
"""
def numeros_persona(nombre, *numeros): ### Se combinan
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

# Ejemplos de uso
mensaje1 = numeros_persona("Ana", 1, 2, 3, 4)
print(mensaje1)  # Salida: Ana, la suma de tus números es 10

mensaje2 = numeros_persona("Carlos", 5, 10, 15)
print(mensaje2)  # Salida: Carlos, la suma de tus números es 30

mensaje3 = numeros_persona("Laura", 7, -2, 8.5)
print(mensaje3)  # Salida: Laura, la suma de tus números es 13.5

'''

#Argumentos Indefinidos **kwargs Leccion 67
#Keyword Arguments - Para diccionarios
#Le podemos dar un valor a los argumentos
'''
def suma(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))

"""
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de 
parémetros que se entregan, y devuelva esa cantidad como resultado.
"""
def cantidad_atributos(**kwargs):
    return len(kwargs)

# Ejemplos de uso
resultado1 = cantidad_atributos(a=1, b=2, c=3, d=4)
print(resultado1)  # Salida: 4

resultado2 = cantidad_atributos(nombre="Ana", edad=30, ciudad="Madrid")
print(resultado2)  # Salida: 3

resultado3 = cantidad_atributos()
print(resultado3)  # Salida: 0

"""
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""
def lista_atributos(**kwargs):
    return list(kwargs.values())

# Ejemplos de uso
atributos1 = lista_atributos(nombre="Ana", edad=30, ciudad="Madrid")
print(atributos1)  # Salida: ['Ana', 30, 'Madrid']

atributos2 = lista_atributos(a=1, b=2, c=3, d=4)
print(atributos2)  # Salida: [1, 2, 3, 4]

atributos3 = lista_atributos()
print(atributos3)  # Salida: []

"""
Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
"""

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

# Ejemplos de uso
describir_persona("María", color_ojos="azules", color_pelo="rubio")
# Salida:
# Características de María:
# color_ojos: azules
# color_pelo: rubio

describir_persona("Juan", altura="1.80m", peso="75kg", edad="30 años")
# Salida:
# Características de Juan:
# altura: 1.80m
# peso: 75kg
# edad: 30 años

describir_persona("Laura")
# Salida:
# Características de Laura:

'''

#Ejercicios practicos
"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""
"""
def devolver_distintos(a, b, c):
    # Calcular la suma de los tres números
    suma = a + b + c
    
    # Encontrar el número mayor, menor e intermedio
    mayor = max(a, b, c)
    menor = min(a, b, c)
    intermedio = a + b + c - mayor - menor

    # Devolver el número según la suma
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:  # suma está entre 10 y 15, inclusive
        return intermedio

# Ejemplos de uso
print(devolver_distintos(5, 7, 3))   # Salida: 7 (suma=15, número mayor)
print(devolver_distintos(1, 2, 3))   # Salida: 1 (suma=6, número menor)
print(devolver_distintos(4, 6, 5))   # Salida: 5 (suma=15, número intermedio)

"""
"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']
"""
"""
def letras_unicas_ordenadas(palabra):
    # Convertir la palabra a un conjunto para obtener letras únicas
    letras_unicas = set(palabra)
    # Convertir el conjunto a una lista y ordenarla
    letras_ordenadas = sorted(letras_unicas)
    return letras_ordenadas

# Ejemplos de uso
resultado1 = letras_unicas_ordenadas("entretenido")
print(resultado1)  # Salida: ['d', 'e', 'i', 'n', 'o', 'r', 't']

resultado2 = letras_unicas_ordenadas("programacion")
print(resultado2)  # Salida: ['a', 'c', 'g', 'i', 'm', 'n', 'o', 'p', 'r']

resultado3 = letras_unicas_ordenadas("python")
print(resultado3)  # Salida: ['h', 'n', 'o', 'p', 't', 'y']"""

"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""
"""
def cero_repetido_consecutivo(*args):
    # Iterar a través de los argumentos
    for i in range(len(args) - 1):
        # Verificar si el número cero aparece dos veces consecutivas
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Ejemplos de uso
print(cero_repetido_consecutivo(5, 6, 1, 0, 0, 9, 3, 5))  # Salida: True
print(cero_repetido_consecutivo(6, 0, 5, 1, 0, 3, 0, 1))  # Salida: False
print(cero_repetido_consecutivo(1, 2, 3, 4, 5))            # Salida: False
print(cero_repetido_consecutivo(0, 0, 0, 0))               # Salida: True

"""

"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
"""

# DIA 6 - PROGRAMA UN RECETARIO
# Abrir y manipular archivos - Leccion 77 Solo se modifica en esta leccion las variables que clonan al archivo
# open, read, write, close - Abrir archivos y alojarlos en varibales para aplicar metodos.
"""
mi_archivo = open("prueba.txt") #Al estar alojado en la misma carpeta, no es necesario decirle que ruta
print(mi_archivo) #
print(mi_archivo.read()) #

una_linea = mi_archivo.readline()
print(una_linea.upper()) #Se pueden usar metodos de los string
una_linea = mi_archivo.readline() #Lee a partir de donde se quedó #De esta forma no se procesa el salto de linea 
print(una_linea.rstrip)
una_linea = mi_archivo.readline()
print(una_linea) 

#Iterar:

for l in mi_archivo:
    print("Aqui dice: "+l)

#Metodo readlines para convertirlos en listas

todas = mi_archivo.readlines() #Devuelve una lista con cada linea #Es mejor usar readlines para archivos pequeños.
todas = todas.pop() 
'''El método pop() elimina y retorna un elemento de una lista.
#Hay un parámetro opcional, el índice a ser eliminado de la lista, 
# si no se especifica ningún índice, a.pop() elimina y retorna el último elemento de la lista.'''
print(todas)
mi_archivo.close() #Es recomendable cerrarlo para no ocupar memoria
"""
# Crear y escribir archivos Leccion 78
# El metodo open open("archivo.txt","x") x {modo apertura} = r {solo lectura}, = w {solo escritura, se crea si no existe, y si existe se re
# reseta, osea borra(sobreescribe) todas las lineas y posiciona cursor al inicio}, a = {solo escritura, se crea si no existe, y si existe posiciona el cursor 
# hasta el final del archivo para escribir apartir de ahi, mantiene el contenido}

archivo = open("prueba1.txt","w") #Solo lectura, al no encontrarlo va a crear uno
archivo.write("Soy el nuevo texto\n") #Metodo para escribir, no permitira si se abrio modo lectura "r"
archivo.write('''Soy la segunda linea
yo la tercera con salto de linea usando diferente metodo al caracter de escape \\n''')
archivo.write("\n") #Salto de linea simple
archivo.writelines(["Una","lista","escrita","con","metodo","writelines\n"]) #Escribe los elementos juntos de corrido sin salto
lista = ["Una","lista","escrita","con","metodo","writelines"]
for p in lista: #Otra forma de escribir una lista con un for y metodo write
    archivo.write(p + "\n") 
archivo.close()

archivo = open("prueba1.txt","a")
archivo.write("Bienvenido")
archivo.close()


