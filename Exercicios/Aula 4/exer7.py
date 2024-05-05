# Solicitamos o número
num = int(input("Digite o número: "))

# Assumimos que o número é primo até que se prove o contrário
eh_primo = True

# Loop para verificar se o número é divisível por algum outro número
# Começa de 2, porque 1 não é um número primo, e vai até um número antes do próprio número
for i in range(2, num):
    # Se o número for divisível por qualquer número dentro deste intervalo,
    # ele não é primo, portanto, mudamos a variável 'eh_primo' para False e saímos do loop.
    if num % i == 0:
        eh_primo = False
        break

# Verifica se 'eh_primo' ainda é True, o que significa que o número passou pelo loop
# sem ser divisível por nenhum número além de 1 e ele mesmo.
if eh_primo == True:
    # Se for o caso, o número é primo.
    print(f'O número {num} é primo')
else:
    # Caso contrário, o número não é primo.
    print(f'O número {num} não é primo')
