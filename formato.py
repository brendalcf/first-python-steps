a = 'AAAA'
b = 'Brenda'
c = 1.1
formato = 'a={0} b={1} c={2:.2f}'.format(a,b,c)
print (formato)
#Quando uma função está dentro de um objeto essa funcção é chamada de método.

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))
nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))