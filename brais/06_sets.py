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

my_set = { "brais" , "Moure" , 35 }

my_list = list(my_set)
print(my_list)


my_other_set = { "kotlin" , "Swift" , "Python" }

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set).union({"Javascript" , "C#"}))

print(my_new_set.difference(my_set))