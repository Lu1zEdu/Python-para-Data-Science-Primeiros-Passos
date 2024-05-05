# Coletamos as idades dos clientes
idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Inicializamos as variáveis de contadores
contador_0_25 = 0 # contador de idades entre 0 e 25
contador_26_50 = 0 # contador de idades entre 26 e 50
contador_51_75 = 0 # contador de idades entre 51 e 75
contador_76_100 = 0 # contador de idades entre 76 e 100

# nosso código executa sempre até o valor de idade for negativa
while idade >= 0:
    # contamos cada caso
    if idade >= 0 and idade <= 25:
        contador_0_25 += 1
    elif idade >= 26 and idade <= 50:
        contador_26_50 += 1
    elif idade >= 51 and idade <= 75:
        contador_51_75 += 1
    elif idade >= 76 and idade <= 100:
        contador_76_100 += 1
    
    # Repetir o processo de entrada de dados até que seja digitado um número negativo    
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

# Mostramos os resultados
print('Distribuição de idades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)
