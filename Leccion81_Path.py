#Crear o mover archivos // Enumerar // 

from pathlib import Path

base=Path.home() #Crea una ruta principal
guia = Path(base,"Barcelona","Sagrada_Familia",Path("Calle_Fea.txt")) #Acepta variable path, cadenas y objetos Path para construir paths, Gestiona de forma inteligente
guia2 = guia.with_name("La_Mas_Bonita.txt") #Sustituye el ultimo elemento de la ruta 
print(base) 
print(guia) #Construye objetos que pueden ser como tipo de directorio, esto sirve para tener 
print(guia2) #Podemos crear otra ruta con diferente archivo desino
print(guia.parent) #Devuelve la ruta 
print(guia.parent.parent) #Podemos aplicarlo cuantas veces se pueda segun la longitud de la ruta

#Enumerar archivos dentro de un directorio usando Path
guia = Path(Path.home(),"Documents","Proyectos Personales","Udemy","PYTHON TOTAL")
print(guia)

for txt in Path(guia).glob("*.txt"): #Busca todos los txt dentro de la carpeta PYTHON TOTAL
    print(txt)

for txt in Path(guia).glob("**/*.txt"): #Busca todos los txt dentro de la carpeta PYTHON TOTAL y ADEMAS DENTRO DE LOS SUBDIRECTORIOS INTERNOS
    print(txt)

guia = Path("Proyectos Personales","Udemy","PYTHON TOTAL")
en_proyectos = guia.relative_to(Path("Proyectos Personales")) #Devuelve objeto Path a partir de cierta carpeta en un ruta
en_udemy = guia.relative_to(Path("Proyectos Personales","Udemy")) #Tiene que aparecer a partir de ahi, A fuerza tiene que aparecer el primer elemento de la izquiera en adelante

print(en_proyectos)
print(en_udemy)