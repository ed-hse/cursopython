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