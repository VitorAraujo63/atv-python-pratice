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

