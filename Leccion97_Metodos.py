class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color=color
        self.especie=especie
    def piar(self):
        print("pio, mi color es {}".format(self.color))
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = Pajaro("amarillo","canario")

piolin.piar()
piolin.volar(30)

#Ejercicios
"""
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. 
Cada vez que ladre, debe mostrarse en pantalla "Guau!".
"""

class Perro:
    def ladrar(self):
        print("Guau!")

husky = Perro()
husky.ladrar()

"""
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() 
(deberá imprimir "¡Abracadabra!").
Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
"""
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

"""
Crea una instancia de la clase Alarma, que tenga un método llamado 
postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""

class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

correr = Alarma()
correr.postergar(30)