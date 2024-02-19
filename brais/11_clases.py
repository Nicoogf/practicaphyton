"""Clases"""

class MyEmptyPersona : 
    pass


print(MyEmptyPersona())

class Persona : 
    def __init__(self , nombre , apellido):
        self.nombre  = nombre
        self.apellido = apellido


myPerson = Persona("Brais" , "Moure")

print(myPerson.nombre)