# Implemente um programa que leia do usuário um número N de números inteiros que fazem
# parte de uma sequência. O programa deve imprimir uma mensagem informando se a sequência
# é composta apenas de números 0s ou 1s, com a mensagem "sequência no padrão" ou com a
# ensagem "sequência não está no padrão", caso algum dos números digitados não seja 0 nem 1

n = int(input('Digite a entrada'))

def test_seq(n: int) -> int:
    seq = 0
    cont = 0
    for i in range(0, n):
        seq = int(input('digite um número:'))

        if seq !=0 and seq !=1:
            cont = cont + 1


    return cont

num = test_seq(n)

if num == 0:
    print('sequência no padrão')
elif num > 0:
    print('sequência não esta no padrão')
else:
    print('sequência digitada')