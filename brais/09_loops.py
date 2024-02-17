""" Lops """

# while

condicion = 0

while condicion < 10:
    print(condicion)
    condicion += 2

else:
    print("Mi condicion es mayo o igual a 10")

print("La ejecucion continua")


while condicion < 20:
    condicion +=1
    if condicion == 15 :
        print("Se detiene la aplicacion")
        break
    print(f"{condicion} Mi condicion es menor s 20")