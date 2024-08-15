#Herencia
# Es un proceso mediante el cual una clase hereda atributos y metodos de otra clase
# Principio DRY, cuanto menos codigo mejor. Dont Repeat Yourself
# Se buscan metodos y atributos que compartan todo un grupo de clases, para formar una clase 


class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha ncaido")


class Pajaro(Animal):
    pass

print(Pajaro.__bases__) #Ve quien es la clase padre
print(Animal.__subclasses__) #Ve quien es la clases hijas

piolin =Pajaro(2,"amarillo")
piolin.nacer() #Ha heredado el metodo de nacer de la clase Animal.

print(piolin.color)

"""
Ejercicios:

Crea una clase llamada Persona, 
que tenga los siguientes atributos de instancia: nombre, edad. 
Crea otra clase, Alumno, que herede de la primera estos atributos.
"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Alumno(Persona):
    pass

"""
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.
"""
class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad=edad
        self.nombre=nombre
        self.cantidad_patas=cantidad_patas
        
class Perro(Mascota):
    pass

"""
Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() 
(puedes dejar el código de los métodos en blanco con pass). 
Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
"""
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

    