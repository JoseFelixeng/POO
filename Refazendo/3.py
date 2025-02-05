# Implemente um programa que leia do usuário um total N de números reais e imprima na tela qual foi o maior número digitado.

n = int(input('Quantos numeros serão digitados'))


def test_numeros(n: int) -> int:  
    cont = maior = menor = 0 

    for i in range(0, len(n)):
        