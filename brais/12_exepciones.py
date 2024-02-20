"""Exepciones"""

numeroUno = 5
numeroDos = 4
numeroDos = "4"

try:
    print(numeroUno + numeroDos)
    print("No se produjo error")

except ValueError:
    print("Se ha producido un error ValueError")
except TypeError as error :
    print(f"Se ha producido un error TypeError {error}")

