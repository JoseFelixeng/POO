# Implemente um programa que leia do usuário um total N de números reais e imprima na tela qual foi o maior número digitado.

n = int(input('Quantos numeros serão digitados '))


def test_numeros(n: int) -> int:  
    cont = maior = menor = 0

    for i in range(0, n):
        cont = int(input('digite um número \n'))

        if cont > maior:
            menor = maior
            maior = cont

    return maior


test = test_numeros(n)

print(f'O maior numero é {test}')





