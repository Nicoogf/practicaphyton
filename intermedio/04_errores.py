"""Errores"""

# SyntaxError
# print "Hola Comunidad"
import math
print("Hola Comunidad")

# NameErrors
languaje = "spanish"
print(languaje)


# indexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
# print(my_list[5])


# ModulenotFound Errors

# import maths


# AtributteError

# print(math.PI)
print(math.pi)

# keyError

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: "Python"
}

print(my_dict["Edad"])






#TypeError
# print(my_list["Nombre"])


#ImportError
# from math import PI
from math import pi as PI

#valueError
# my_int = int("10 años")
# print(type(my_int))


#ZerodivisionError
print(1 /0 )