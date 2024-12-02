#Operadores lógicos
# and (e) or (ou) not (não)
#and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão
# inteira será avaliada naquele valor
# São considerado falsy (que você já viu) 0 0.0 '' (string vazia) False
# Também existe o tipo None que é usado para representar um NÃO valor

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
 # print('Entrar')
#else:
#   print('Sair')

#if 0 and 1:

 #   print(True and 1)

#avaliação de curto circuito
#senha = input('Senha: ') or 'Sem senha'
#print(senha)

#OPERADOR LÓGICO NOT
#O QUE FOR TRUE VIRA FALSE E O QUE FOR FALSE VIRA TRUE
senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta')