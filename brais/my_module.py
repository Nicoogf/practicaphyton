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
    my_sum =first_value + second_value
    return my_sum

resultado = sum_two_values_with_return(10 , 5 )

print(resultado)



def print_name (nombre , apellido ) :
    print(f"Se creo el nombre {nombre} {apellido}")
    
print_name(apellido="Falabella" , nombre="Nicolas" )


def print_name_with_default ( nombre , apellido , alias="Sin Alias Registrado" ):
    print(f"Se cargo el nombre {nombre} {apellido} {alias}")

print_name_with_default("Nicolas" ,"Falabella" )


def print_upper_texts(*texts) :
    for text in texts:
        print(text.upper())

print_upper_texts("hola","mundo")