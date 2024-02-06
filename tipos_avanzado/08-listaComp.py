usuarios = [
    ["Adrian", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


# nombres = []

# for usuario in usuarios :
#     nombres.append(usuario[0])

# print(nombres)


# nombres = [usuario[0] for usuario in usuarios]

# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

nombres = list(map(lambda usuario: usuario[0], usuarios))
menosNombres = list(filter(lambda usuario: usuario[1] > 2, usuarios))
menosNombresNuevo= list(map(lambda usuario: usuario[0] , menosNombres))
print(menosNombresNuevo)
