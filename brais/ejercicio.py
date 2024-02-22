""" asd """


# def ejercicio_uno():
#     for numer in range(1, 101):
#         if numer % 3 == 0 and numer % 5 == 0:
#             print(f"FizzBuzz {numer}")
#         if  numer % 3 == 0 :
#             print(f"Fizz {numer}")
#         if  numer % 5 == 0 :
#             print(f"Buzz {numer}")
#         else :
#             print(numer)


# ejercicio_uno()


# def es_anagrama ( palabrauno , palabrados) :
#     if palabrauno == palabrados:
#         return False
#     return sorted(palabrauno.lower()) == sorted(palabrados.lower())

# print(es_anagrama("casa" ,"asac"))


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]

# print(sorted(student_tuples, key=lambda x:x[2] , reverse=True))


# def fibonacci () :

#     prev = 0
#     next = 1

#     for index in range(1,51):
#         print(f"Posicion {index} : {prev}")
#         fib = prev + next
#         prev =  next
#         next = fib


# fibonacci()


# def is_primo ( number ) :
#     if number < 2 :
#         return False
#     for index in range(2,number):
#         if number % index == 0:
#             return False

#     return True

# print(is_primo(4))


# def FizzBuzz () :
#     for index in range(0, 101) :
#         if index % 3 == 0 and index % 5 == 0 :
#             print(f"El numero {index} es FizzBuzz")
#         elif index % 3 == 0 :
#             print(f"El numero {index} es Fizz")
#         elif index % 5 == 0 :
#             print(f"El numero {index} es Buzz")
#         else:
#             print(f"El numero {index}")

# FizzBuzz()


# def es_anagrama( palabraUno, palabraDos ) :
#     if palabraUno == palabraDos :
#         return False
#     return sorted(palabraUno.lower()) == sorted(palabraDos.lower())

# print(es_anagrama("culo" ,"olu"))


# def fibonacci() :
#     prev = 0
#     next = 1
#     for index in range(0 , 50):
#         print( prev )
#         fib = prev + next
#         prev = next
#         next = fib

# fibonacci()


def es_primo():
    for numero in range(1,101):
        if numero < 2:
            return False
        for index in range(2, numero):
            if numero % index == 0:
                return False
        return True


print(es_primo())
