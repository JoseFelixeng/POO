# Aula 1 

# 1 Ex: Implemente um programa que, dados três valores inteiros, informe quantos deles são pares.

# Exercício 0 - Solução

a = int(input('Informe o 1o. nr.: '))
b = int(input('Informe o 2o. nr.: '))
c = int(input('Informe o 3o. nr.: '))
# Dica: ao invés de ler a entrada do usuário
# com o comando 'input', vc pode atribuir
# os valores das entradas diretamente no código
# quando estiver testando o seu código.
# Exemplo:
# a = 5
# b = 2
# c = 3

pares = 0

def contar_pares(a: int, b: int, c: int) -> int:
    soma = 0
    for num in (a,b,c): 
        if num%2 == 0: 
            soma = soma +1
    return soma 
pares = contar_pares(a,b,c)

print('{} numero(s) par(es)'.format(pares))

