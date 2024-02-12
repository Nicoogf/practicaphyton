""" Variables """

my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

print(my_bool_variable)
print(my_variable, my_int_to_str_variable, my_bool_variable)

print(type(print("hola")))

# Len
print(len(my_int_to_str_variable))
print("El valor de la variables es : ", my_bool_variable)

name, surname, alias, age = "Brais", "Moure", "Moure dev" , 43

print( age , name , surname , "y mi alias es : " , alias )
 """
name = input("Ingresar nombre")
edad = input("Ingresar edad")
print(name , age)

name = 35
age = "Brais"
print(name , age)
 """



#Forzamos el tipo
address: str = "Mi Direccion"
address = 32 

print(type(address))