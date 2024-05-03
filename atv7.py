numero = 1

while numero in range(0, 100):
    if numero % 3 == 0:
        print(numero)
        numero += 1
        continue
    numero += 1

