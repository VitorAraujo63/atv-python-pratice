numeros = 0
numero = []
soma = 0

for numeros in range(100):
    numeros += 1
    
    numero.append(numeros)

while numero:
    soma += numero[0] + numero [-1]
    print(soma)
    numero.remove(numero[0])
    numero.remove(numero[-1])

