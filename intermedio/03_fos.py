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


def sum_ten(original_value):
    def add(value):
        return value +10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))


numbers = [ 2 , 5, 10, 21 ,3 ,30]

def mutiply_two(number):
    return number * 2

print(list(map( mutiply_two , numbers  )))
print(list(map( lambda number: number * 2 , numbers  )))


#filter

def filter_greater_ten( number ) :
    if number > 10 :
        return True
    return False

print(list(filter( filter_greater_ten , numbers)))