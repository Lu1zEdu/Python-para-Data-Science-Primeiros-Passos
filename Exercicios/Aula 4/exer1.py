# Coletamos os valores de início e fim
inicio = int(input('Insira o primeiro número inteiro: '))
fim = int(input('Insira o segundo número inteiro: '))

# Verificamos se o valor de início é maior que o fim
if inicio < fim:
  # podemos imprimir os inteiros entre o menor e o maior valor
  for i in range(inicio + 1, fim): 
    print(i)
elif inicio > fim:
  for i in range(fim + 1, inicio):
    print(i)
else: #caso os números sejam iguais, não conseguimos imprimir sequência alguma
  print('Os números são iguais.')
