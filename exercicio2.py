nome = 'Ricardo'
altura = 1.70
peso = 63.0
imc = peso / (altura * altura)
print(nome, 'tem', altura, 'de altura.')
print(nome, 'pesa', peso, 'kilos.')
print('O IMC de', nome, 'é: ', imc)
print('Fazendo formatações:')
linha_1 = f'{nome} tem altura de {altura:.1f}'
print(linha_1)
linha_2 = f'{nome} pesa {peso:.2f} kilos'
print(linha_2)
linha_3 = f'seu imc é {imc:.2f}'
print(linha_3)

