# Coletamos os preços dos três produtos
p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

# Verificamos qual produto é o mais barato usando o operador lógico 'and'
if p1 < p2 and p1 < p3:
    print('O primeiro produto é o mais barato.')
elif p2 < p1 and p2 < p3:
    print('O segundo produto é o mais barato.')
elif p3 < p1 and p3 < p2:
    print('O terceiro produto é o mais barato.')
elif p1 == p2 == p3:
    print('Os produtos possuem o mesmo preço.')
else:
    # Identificamos quais produtos possuem o mesmo preço, se for o caso
    if p1 == p2:
        print('O primeiro e o segundo produtos são os mais baratos.')
    elif p2 == p3:
        print('O segundo e terceiro produtos são os mais baratos.')
    elif p1 == p3:
        print('O primeiro e o terceiro produtos são os mais baratos.')
