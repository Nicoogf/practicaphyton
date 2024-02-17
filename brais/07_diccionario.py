""" Objetos"""
my_dict = dict()

my_other_dict= {}

print(type( my_dict ))
print(type( my_other_dict ))

my_other_dict = {"Nombre" : "Brais" , "Apellido" : "Moure" , "Edad" : 35 , 1 : "Python"}

my_dict = {
        "Nombre" : "Brais" , 
        "Apellido" : "Moure" , 
        "Edad" : 35 , 
        "Lenguajes": {"Python" , "Swift" , "Kotlin"},
        1 : 1.77
    }

print( my_other_dict )
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Adrian"

print(my_dict["Nombre"])

print(my_dict[1])

my_dict["calle"] = "106"


del my_dict["calle"]
del my_dict["Apellido"]

print(my_dict)

print("Nombre" in my_dict)
print("Brais" in my_dict)
#print("Moure" in my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("nombre" , 1 )))

my_list_= ["Nombre" , 1 , "Piso"]

my_new_dict = my_dict.fromkeys((my_list_))

print(my_new_dict)

print(list(my_new_dict.values()))