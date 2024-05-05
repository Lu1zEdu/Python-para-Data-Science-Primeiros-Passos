# laço para pegar as 15 notas
for i in range(15):
  nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

  # verifica se a nota está entre 0 e 5
  # se estiver, o laço rodará ininterruptamente até ser obtido um valor válido
  while (nota < 0) or (nota > 5):
    nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

print('Verificação feita. Todas as notas são válidas')
