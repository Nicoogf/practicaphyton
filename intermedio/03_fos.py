"""Funciones orden superior"""

def sum_one( valor ):
    return valor + 1

def sum_five (valor) :
    return valor + 5

def sum_two_values_and_one ( first_value , second_value) :
    return sum_one(first_value + second_value)

def sum_two_funcion (valor_uno , valor_dos , funcion ) :
    return funcion(valor_uno + valor_dos)


print(sum_two_values_and_one(5,5))
print(sum_two_funcion(5,2,sum_five))