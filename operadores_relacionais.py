#Operadores de comparação (relacionais)
#> MAIOR 
#>= MAIOR OU IGUAL
#< menor
# == igual
#!= diferente

#maior = 2 > 1
#maior_ou_igual = 2 >= 2
#menor = 1 < 2
#menor_ou_igual = 2 <= 2
#igual = 'a' == 'a'
#diferente = 'a' != 'b'
#print(maior_ou_igual)

primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'que o {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )


