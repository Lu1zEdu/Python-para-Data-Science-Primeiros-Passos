# Pedir o número
num = int(input('Informe um número inteiro: '))

# Inicializar o cálculo
fatorial = 1

# nosso contador inicializa com o número máximo
# e será feita uma contagem decrescente com o operador -=
i = num
while i > 0:
    # queremos multiplicar agora o valor do fatorial pelo num
    # e todos os números abaixo dele até 1
    fatorial *= i
    i -= 1

# Imprimir o cálculo do fatorial
print(f'Fatorial de {num} é {fatorial}')
