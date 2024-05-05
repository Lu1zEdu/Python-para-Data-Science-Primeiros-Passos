# Coleta do percentual
variacao = float(input('Digite o percentual de crescimento: '))

# Verifica se o valor é positivo ou negativo com uma verificação se o número
# é maior ou menor que 0
if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve um decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento.')
