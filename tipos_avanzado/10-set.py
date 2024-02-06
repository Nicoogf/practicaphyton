primer = {1, 1, 2, 3, 4, 4}

segundo = [3, 4, 5]

segundo = set(segundo)

print(primer | segundo)
print(primer & segundo)
print(primer - segundo)
print(primer ^ segundo)

if 5 in segundo:
    print("hola mundo")
