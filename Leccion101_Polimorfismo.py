"""
Permite que diferentes objetos con un metodo que se llama igual
comportarse de forma diferente, por eso el POLI-MORFISMO
"""


class Vaca:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + " dice bee")

vaca1=Vaca("Aurora")
oveja1=Oveja("Nube")



animales = [vaca1,oveja1] 

# Veremos la utilidad en la siguientes lineas: 
for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)


