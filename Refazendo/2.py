# Implemente um programa que leia três números inteiros denotando os lados de um triangulo. 
# Três números formam um triângulo se cada um deles for menor do que a soma dos outros dois.
# O programa deve informar se eles formam um triângulo e em caso positivo, qual é o triângulo formado 
# (equilátero, isósceles ou escaleno).

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

def test_triangulo(a: int, b: int, c: int) -> int:
    tt = True
    tpt = ''
    if a > b + c or b > a + c or c > a + b:
        tt = False
        return tt, tpt 
    elif (a != b) and (a != c) and (b != c):
        tpt = 'escaleno'
        return tt, tpt
    elif (a == b and a != c) or ((a == c and a != b)) or (b == c and b != a ):
        tpt = 'isoceles'
        return tt, tpt
    elif a == b == c:
        tpt = 'equilatero'
        return tt, tpt
    
resultado = test_triangulo(a, b, c)


if resultado[0] == True:
    print(f'é um triangulo de tipo {resultado[1]}')
else:
    print('Não é um triangulo')