"""
Existen decoradores para 

metodos de instancia
    Son los que creamos con def(self) #Usan self
    acceden y modifican atributos de instancia y de clase
    acceder a otros metodos 

metodos de clase
    @classmethod
    def mi_metodo(cls): #usan cls
        print("algo")
    No pueden acceder a los atributo de la instancia pero si de la clase

metodos estatico:   "No usan 
    @staticmethod
    No pueden modificar parametros de clase ni de la instancia, solo realizan acciones

"""

class Pajaro:
    alas = True

    #metodos de instancia, por eso tienen al self
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pío")

    def volar(self,metros):
        print(f"EL pajaro vuela {metros} metros")
        self.piar() #Metodo de instancia invoca a otros metodos

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod #Para declarar metodo de clase
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        #print(f"Es de color {self.color}") #No es posible acceder a los atributos de la instancia
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod #Para declarar metodo estatico, no accede a atributos de instancia, de clase, ni a otros metodos
    def mirar():
        print("El pajaro mira")


piolin = Pajaro("amarillo","canario")
piolin.pintar_negro()
piolin.volar(31)
piolin.alas=False #tambien accede a los atributos de la clase
print(piolin.alas)

Pajaro.poner_huevos(3)

