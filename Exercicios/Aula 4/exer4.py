# coletamos a temperatura
temperatura = float(input('Insira a temperatura em Celsius: '))

# inicializamos uma contadora e soma para a média
contadora = 0
soma = 0

# nosso código executa sempre até o valor de temperatura for igual a -273
while temperatura != -273:
    # a soma é dada com a adição da temperatura à variavel soma
    soma += temperatura
    # contamos a quantidade de valores coletados através da contadora
    contadora += 1
    # coletamos novamente a temperatura
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A média das temperaturas é: {media}')
