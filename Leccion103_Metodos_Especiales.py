"""
Son aquellos que inician y terminan con __ 
ejemplo: __init__
        __mro__
        __bases__
        __subclases__
Funcionalidades que no pueden ser representadas en metodos
"""

class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo =titulo
        self.canciones = canciones

    def __str__(self): #Redefinicion del metodo aplicado para esta clase
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self): #Redefinicion del metodo aplicado para esta clase.
        return self.canciones
    
mi_cd = CD("PinkFloyd","The Wall",24)
print(len(mi_cd))

del mi_cd #Eliminar la instancia de la clase

# Como usar aquellos metodos ya existentes en python para ciertas clases, 
# aplicado ahora a mis clases que he creado



