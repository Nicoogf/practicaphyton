numeros = [2, 14, 1, 45, 75, 22]
# numeros.sort( reverse=True)

numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["Adrian", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena , reverse=True)
print(usuarios)
