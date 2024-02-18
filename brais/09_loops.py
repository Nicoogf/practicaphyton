""" Lops """

# while

# condicion = 0

# while condicion < 10:
#     print(condicion)
#     condicion += 2

# else:
#     print("Mi condicion es mayo o igual a 10")

# print("La ejecucion continua")


# while condicion < 20:
#     condicion +=1
#     if condicion == 15 :
#         print("Se detiene la aplicacion")
#         break
#     print(f"{condicion} Mi condicion es menor s 20")



my_list = [35,24,62,52,30,30,17]

my_dict = {
        "Nombre" : "Brais" , 
        "Apellido" : "Moure" , 
        "Edad" : 35 , 
        "Lenguajes": {"Python" , "Swift" , "Kotlin"},
        1 : 1.77
    }


for element in my_dict :
    print(element)
    if element == "Edad" :
        break
    print("Se ejecuta")
else :
    print("El bucle for para diccionario finalizo")