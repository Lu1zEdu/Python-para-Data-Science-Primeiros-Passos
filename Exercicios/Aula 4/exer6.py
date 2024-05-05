# Pedir o número
num = int(input('Informe um número inteiro de 1 a 10: '))

# Vamos gerar a tabuada
print(f'Tabuada do {num}:')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
