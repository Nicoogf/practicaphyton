""" asd """

my_string = "My String"
my_other_string = 'My otro String'

print(len(my_other_string))
print(len(my_string))

print( my_string + " " + my_other_string)
print(int(len(my_string) + int(len(my_other_string)) ))


my_new_line_string = "Hola \nen salto de linea"
my_tab_string = "Hola \tstring"

print(my_new_line_string)

print(my_tab_string)


my_scape_string = "\\hola es un strins \\n espado"

print(my_scape_string)

#Formateo
nombre = "Brais"
apellido = "Moure"
edad = 32

print("Mi nombre es Brais Moure y tengo 32 años")

print("Mi nombre es {} {} y mi edad  es {}".format(nombre,apellido,edad))
print("Mi nombre es %s %s y mi edad  es %d" %( apellido ,  nombre ,edad ))

print("Mi nombre es %s mi apellido es %s y tengo la edad de %d" %(nombre,apellido,edad))


print(f"mi nombre es {nombre} {apellido}  y tengo {edad}")

#Desempaquetado

language = "Python"
a , b ,c ,d, e ,f= language
print(a ,b ,c,e,f)


#Division

language_slide = language[-2]

print(language_slide)

#reverse 

languaje_reversed = language[::-1]
print(languaje_reversed)

#Funciones



print(language.isnumeric())
print(language.upper().isupper())