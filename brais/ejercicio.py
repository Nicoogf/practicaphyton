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


def fibonacci () :

    prev = 0
    next = 1
    
    for index in range(1,51):
        print(f"Posicion {index} : {prev}")
        fib = prev + next
        prev =  next
        next = fib
        

fibonacci()