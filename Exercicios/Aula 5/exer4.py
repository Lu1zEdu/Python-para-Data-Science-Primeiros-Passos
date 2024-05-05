# Lista que irá armazenar os 5 números inteiros
lista_numeros = []

# Criamos um laço que vai iterar 5 vezes para receber os 5 números
for i in range(0, 5):
  # Coletamos o valor e inserimos na lista por 5 vezes
  numero = int(input('Digite um número inteiro: '))
  lista_numeros.append(numero)
# Usamos da lógica de partição para imprimir o resultado
print(f'Lista de números invertida: {lista_numeros[::-1]}')
