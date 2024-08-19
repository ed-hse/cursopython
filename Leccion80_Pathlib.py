from pathlib import Path, PureWindowsPath #Ruta de Windows Path, transforma cualquier ruta en una de windows

carpeta = Path("C:/Users/DELL/Documents/Proyectos Personales/Udemy/PYTHON TOTAL/prueba.txt")
ruta_windows = PureWindowsPath(carpeta)

"""print(carpeta.read_text(encoding="utf-8")) #Permite leer sin necesidad de abrir el archivo
print(carpeta.name) #Extrae el nombre del archivo
print(carpeta.suffix) #La extension del archivo
print(carpeta.stem) #Devuelve el nombre del archivo sin la extension incluida"""

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

print(ruta_windows) #Imprimir la ruta tipo windows