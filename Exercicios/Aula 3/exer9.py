# Coletamos os dados
num = float(input('Digite um número: '))

# Verificamos se o número é inteiro ou decimal através do resultado do módulo
if num % 1 == 0:
    print('O número é inteiro.')
else:
    print('O número é decimal.')
