"""Tuplas"""


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,"Brais","Moure","Brais")
my_other_tuple=(35,60,20)
my_sum_tuple = my_tuple + my_other_tuple

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)

print(type(my_tuple))