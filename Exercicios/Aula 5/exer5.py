# Coletamos o números
numero = int(input('Digite um número inteiro: '))
# Lista para receber os números primos
lista_primos = []
# Laço que vai rodar por todos os números abaixo do número digitado
for num in range(2, numero):
  # Primo é uma bandeira, ela permite sabermos se o valor analisado é ou não primo
  primo = True 
  # Testamos se todos os números abaixo do especificado no primeiro laço podem
  # gerar uma divisão exata
  for teste_divisiveis in range(2, num):
    if num % teste_divisiveis == 0:
      # Caso seja divisivel por algum número entendemos que 
      # o num não é primo e finalizamos o laço interno com break
      primo = False
      break
  # A condição se torna o resultado booleno de primo: False, ignoramos o condicional
  # True, executamos o bloco do if
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')
