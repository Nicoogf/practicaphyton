"""Ficheros"""

import os

txt_file = open("./my_file.txt", "w+")

txt_file.write("Creacion del archivo base")

print(txt_file.readline())

txt_file.write("\nNueva Linea de comando")

txt_file.close()

# os.remove("./my_file.txt")