### lambda ###

def sum_two_values(firstvalue, secondvalue): return firstvalue + secondvalue


print(sum_two_values(2, 4))


def nuevalambda(uno, dos): return uno * dos - 3


print(nuevalambda(2, 4))


def prueba_lambda(value):
    return lambda firstvalue, secondvalue: firstvalue + secondvalue + value

print(prueba_lambda(5)(5,5))
