saludo = "Hola global"

def saludar():
   global saludo
   print(saludo)

def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()