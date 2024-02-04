print("Bienvenidos a la Calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma,resta,multi y div")

resultado = ""

while True : 
    if not resultado:
        resultado = input("Ingresar numero : ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("Ingresa operacion : ")
    if operacion.lower() == "salir" :
        break
    n2 = input("ingresar el siguiente numero : ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if operacion.lower() == "suma" :
        resultado += n2 
    elif operacion.lower() == "resta" :
        resultado -= n2 
    elif operacion.lower() == "multi" :
        resultado *= n2 
    elif operacion.lower() == "div" :
        resultado /= n2 
    else:
        print("Operacion no Valida")
        break

    print(f"El resultado es {resultado}")
