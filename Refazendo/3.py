# Implemente um programa que leia do usuário um total N de números reais e imprima na tela qual foi o
# maior número digitado.

class Numero:
    '''Essa classe é feita para definir a quantidade de numeros a serem testados'''

    def __init__(self, n):
        '''Inicialização da classe'''
        self.n = n
        self.cont=0
        self.maior=0
        self.menor = 0

    def test_maior(self):

        for i in range(0, self.n):
            self.cont = int(input('digite um número \n'))

            if self.cont > self.maior:
                self.menor = self.maior
                self.maior = self.cont

        return self.maior

    def __str__(self):
        return 'O maior numero é {} e o menor é {}'.format(self.maior, self.menor)



if __name__ == "__main__":
    n = int(input('Quantos numeros serão digitados '))
    r = Numero(n)
    r.test_maior()
    print(r)
