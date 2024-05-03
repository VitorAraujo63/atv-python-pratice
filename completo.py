escolher_exercicio = int(input("Escolha o numero do exercicio (1 - 10): "))

# Exercicio 1

if escolher_exercicio == 1:
    numero = 1
    
    while numero <=10:
        if numero == 5:
            numero += 1
            continue
        print(numero)
        numero += 1

# Exercicio 2

elif escolher_exercicio == 2:
    numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)

# Exercicio 3

elif escolher_exercicio == 3:
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

# Exercicio 4

elif escolher_exercicio == 4:
    numeros = [1,2,3,4,5,6,7,8,9,10]

    while numeros:
        print(numeros[-1])
        numeros.remove(numeros[-1])

# Exercicio 5

elif escolher_exercicio == 5:
    numeros = 0

    while numeros <= 20:
        if numeros % 2 != 0:
            print(numeros)
        numeros += 1

# Exercicio 6

elif escolher_exercicio == 6:
    print("Em desenvolvimento")

# Exercicio 7

elif escolher_exercicio == 7:
    numero = 1

    while numero in range(0, 100):
        if numero % 3 == 0:
            print(numero)
            numero += 1
            continue
        numero += 1

# Exercicio 8

elif escolher_exercicio == 8:
    nomes = []


    print("Digite pelo menos 10 nomes, quando quiser parar digite 'SAIR'")
    while True:
        nome = input("\nDigite um nome: ")

        if nome == 'SAIR':
            if len(nomes) < 10:
                print(f"Ainda falta {10 - len(nomes)} nomes")
                continue
            break
        nomes.append(nome)

    for idx, nome in enumerate(nomes):
        print(f"{idx}. {nome}")

# Exercicio 9

elif escolher_exercicio == 9:
    lista = []

    print("Hora das compras. caso não for colocar mais nada na lista basta digitar 'sair'")
    lista.append("Lista de produtos")
    try:
        while True:
            produto = input("O que você irá comprar: ").lower()
            

            if produto == 'sair':
                if len(lista) < 11:
                    print(f"Você precisa ter pelo menos 10 itens na sua lista, faltam {11 - len(lista)} itens")
                    continue
                break
            lista.append(produto)

        while lista:
            print(20*'===')
            
            if len(lista) == 1:
                break

            for idx, produtos in enumerate(lista):
                print(f"\n{idx}: {produtos}")

            comprado = int(input("\nQual item você esta comprando(informe o numero na lista): "))

            if comprado == 0:
                print("\nVocê não pode remover o numero '0' da lista... !!")
                continue
            elif comprado <= (len(lista) - 1):
                lista.remove(lista[comprado])
            else:
                print("\nNumero não identificado na lista, por favor tente outro numero")
                continue

        print("\nVocê terminou a sua compra !!")
    except Exception as erro:
        print(f"houve um problema, '{erro}'")

# Exercicio 10

elif escolher_exercicio == 10:
    print("Em desenvolvimento")