#Para la leccion se usa PyCharm, pero intentare trasladar la funcionalidad en VSCode
import os
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


nombre =input("DIme tu nombre: ")
edad = input("DIme tu edad: ")

#clear_terminal()
print("\033c", end="")

print(f"tu nombre es {nombre} y tienes {edad} años")