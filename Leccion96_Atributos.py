#Dos clases de atributos en la POO en Python
#Atributos de clase
#Atributos de la instancia

class Pajaro:
    alas =True #Atributo de clase, todos comparten el mismo valor de atributo
    def __init__(self,color): #Metodo constructor que asigna atributo, afuerzas en la instancia pedira un atributo a asignar
        self.color=color #Al atributo color le asignamos el valor de la variable color

mi_pajaro=Pajaro("negro")

class Auto:
    def __init__(self,color,marca):
        self.color = color
        self.marca = marca

mi_auto = Auto("negro","Toyota")
print(f"Mi auto es un {mi_auto.marca} de color {mi_auto.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)
