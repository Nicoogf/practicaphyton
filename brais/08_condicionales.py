""" Condicional"""
condicion = False

if condicion:
    print("Se ejecuta la condicion del if")

condicion = 5 * 2

if condicion == 10:
    print("Se ejecuta la condicion del segundo if")

if condicion > 10:
    print("La condicion es mayor que 10")
else:
    print("Es menor o igual que 10")

print("La ejecucion continua")


my_string = "mi cadena de texto"

if not my_string:
    print("Mi cadena de texto no es vacia")
