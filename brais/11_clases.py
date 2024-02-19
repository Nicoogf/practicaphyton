"""Clases"""

class MyEmptyPersona : 
    pass


print(MyEmptyPersona())

class Persona : 
    def __init__(self , nombre , apellido , alias = "Sin alias"):
        self.fullname = f"{nombre} {apellido}  {alias}"

    def walk(self):
        print(f"{self.fullname}Esta caminando")

myPerson = Persona("Brais" , "Moure")

myPerson.walk()

myOtherPerson =Persona("Nicolas" ,"Falabella" ,"NicoDev")
myOtherPerson.walk()
