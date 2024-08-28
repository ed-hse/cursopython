"""
try, exception, finally
Intenta ejecutar
exception: Si sale mal has esto
finally: Sea como sea, ejecuta esto

"""

def suma():
    n1 = int(input("numero 1:"))
    n2 = int(input("numero 2:"))
    print(n1+n2)
    print("Gracias por sumar")



try:
    #Codigo que queremos probar
    suma()
except:
    print("Algo no funciono")
else:
    #Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    #Codigo a ejecutar de todos modos
    print("Eso fue todo")

