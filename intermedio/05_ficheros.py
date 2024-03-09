"""Ficheros"""

import json
import os

txt_file = open("./my_file.txt", "w+")

txt_file.write("Creacion del archivo base")

print(txt_file.readline())

txt_file.write("\nNueva Linea de comando")

txt_file.close()

# os.remove("./my_file.txt")

json_file = open("./mi_practica.json", "w+")

json_text = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": ["Python", "Swift", "Kotlin"],
    "web": "https://google.com"
}

json.dump(json_text, json_file)

json_file.close()

with open("./mi_practica.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./mi_practica.json"))

print(json_dict)

print(type(json_dict))