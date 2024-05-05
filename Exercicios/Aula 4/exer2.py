# número inicial de bactérias
colonia_a = 4
colonia_b = 10

# taxas de crescimento das colônias
taxa_a = 0.03
taxa_b = 0.015

# contador de dias
dias = 0

# A condição que finaliza o laço é o caso em que
# a colônia A ultrapasse a colônia B
while colonia_a <= colonia_b:
  # usamos um operador de atribuição com multiplicação
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  # contamos o dia para cada iteração
  dias += 1

# resultado final
print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')
