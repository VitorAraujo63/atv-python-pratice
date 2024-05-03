'''
frutas = ['maça', 'banana', 'uva', 'melancia']
precos = [5.99, 6.99, 7.99, 8.99]
for idx, fruta in enumerate(frutas):
  print(f"Fruta: {fruta} | R$: {precos[idx]}")
'''

numeros = [2, 5, 8, 11, 14]
impar = []

for idx, numero in enumerate(numeros):
  if numeros[0] %2 != 0:
      impar.append(numeros[0])
      numeros.remove(numeros[0])
      print(idx, numeros)
      continue
  else:
      numeros.remove(numeros[0])
      
      continue
      
print(impar)

