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