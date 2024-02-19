### Funciones ###

def my_function () :
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values ( first_value:int , second_value:int) :
    print(first_value + second_value)

sum_two_values( 5, 7 )
sum_two_values( 6 , 4.2 )


def sum_two_values_with_return ( first_value:int , second_value:int) :
    return first_value + second_value

resultado = sum_two_values_with_return(10 , 5 )

print(resultado)
