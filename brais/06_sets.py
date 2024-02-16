"""Sets"""
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set  = { "brais" , "Moure" , 35 }
print(type(my_other_set))


print(len(my_other_set))

my_other_set.add("MuoreDev")

print(my_other_set)

print("Moure" in my_other_set)
print("Adrian" in my_other_set)


my_other_set.remove("Moure")

print(my_other_set)




print(len(my_other_set))


prueba = my_other_set.copy()

del my_other_set

print(my_other_set)