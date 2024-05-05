# Dados de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Variável que vai contar quantas compras foram feitas acima de 3000
contador_acima_3000 = 0
# Usamos o laço para ler a lista de gastos
for gasto in gastos:
  # Verificamos se o elemento está acima de 3000
  if gasto > 3000:
    # Acrescentamos mais um no contador, caso tenha algum valor acima de 3000
    contador_acima_3000 += 1
    
# Quantidade Compras
# Variável que vai ser utilizada para o cálculo da porcentagem
quantidade_compras = len(gastos)	


# Com a contagem conseguimos calcular a porcentagem de valores acima de 3000 entre todas as compras
porcentagem_acima_3000 = 100 * (contador_acima_3000) / (quantidade_compras) 

# Resultado
print(f'{contador_acima_3000} compras foram acima de R$3000,00.')
print(f'{porcentagem_acima_3000}% dos gastos foram acima de R$3000,00.')
