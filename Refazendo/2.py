# Implemente um programa que leia três números inteiros denotando os lados de um triangulo. 
# Três números formam um triângulo se cada um deles for menor do que a soma dos outros dois.
# O programa deve informar se eles formam um triângulo e em caso positivo, qual é o triângulo formado 
# (equilátero, isósceles ou escaleno).

class Triangulo:
    '''Essa é a classe que defini um triangulo'''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.tt = True
        self.tpt = ''


    def test_tipo(self:int , a: int, b: int, c: int) -> int:

        if a > b + c or b > a + c or c > a + b:
            self.tt = False
        elif (a != b) and (a != c) and (b != c):
            self.tpt = 'escaleno'
        elif (a == b and a != c) or ((a == c and a != b)) or (b == c and b != a ):
            self.tpt = 'isoceles'
        elif a == b == c:
            self.tpt = 'equilatero'

    def test_triangulo(self):
        if self.tt != True:
            print('Não é um triangulo')
        else:
            print('É Um triangulo')


    def __str__(self):
        return '{}, {}'.format(self.tpt, self.tt)

if __name__ == "__main__":
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

    t = Triangulo(a, b, c)
    t.test_tipo(a,b,c)
    print(t)
    t.test_triangulo()


