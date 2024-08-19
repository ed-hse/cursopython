"""
Para una clase hija
metodos heredados
metodos modificados
metodos nuevos

Lo mismo para los atributos

Herencia multiple: Puede heredar de mas de una clase.

Se amplia, si hay una tercer hijo, que metodo va heredar?? lo veremos en la clase
"""


class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha ncaido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    def __init__(self, edad, color,altura_vuelo): #Una forma de 
        self.edad=edad
        self.color=color
        self.altura_vuelo=altura_vuelo

    def hablar(self):
        print("pio") #Metodo heredado modificado
    def volar(self,metros): #Metodo nuevo en hijo
        print(f"el pajaro vuela {metros} metros")

piolin = Pajaro(3,"amarillo",60)
piolin.hablar() #Se efectua la modificacion del metodo
piolin.volar(20)

mi_animal=Animal(5,"negro")

class Perro(Animal):
    def __init__(self, edad, color,velocidad):  #OTRA FORMA DE HEREDAR ATRIBUTOS DE FORMA MAS COMPACTA SIN NECESIDAD DE ESCRIBIR MUCHO
        super().__init__(edad, color)
        self.velocidad=velocidad

#Herencia extendida

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja-ja")
    def hablar(self):
        print("Que tal")


#Hereda de Padre y Madre, si se repiten los metodos en las clases Padres, se ejecuta el que primero se hereda, en este caso Padre
# Si la clase Hijo fuer Hijo(Madre,Padre), la Clase Nieto elejiria el metodo de Madre por ser primero.
class Hijo(Padre,Madre): 
    pass

class Nieto(Hijo):
    pass

mi_nieto =Nieto()
mi_nieto.hablar() #Hereda del Padre por medio de Hijo, aunque 
mi_nieto.reir() # Hereda de Madre por medio de hijo

print(Nieto.__mro__) #Orden en que se busca el metodo a ejecutar

#Ejercicio de codificacion

"""
Si la clase Hija ha heredado de su padre la forma de reir, 
y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, 
crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.
Completa el código suministrado a continuación para lograrlo
"""
#Como la clase Madre no tiene metodo reir, no habra problema con que herede primero a madre y despues a padre, funcionara bien

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre,Padre):
    pass

"""
"El ornitorrinco es una de las criaturas más raras del mundo: 
aunque es un mamífero, pone huevos; y amamanta a sus crías 
pero no tienen mamas." (National Geographic)
Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, 
Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:
- poner_huevos()
- tiene_pico = True
- vertebrado = True
- venenoso = True
- nadar()
- caminar()
- amamantar()
"""

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass


