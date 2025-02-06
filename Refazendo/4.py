# Implemente um programa que leia do usuário um número N de números inteiros que fazem
# parte de uma sequência. O programa deve imprimir uma mensagem informando se a sequência
# é composta apenas de números 0s ou 1s, com a mensagem "sequência no padrão" ou com a
# ensagem "sequência não está no padrão", caso algum dos números digitados não seja 0 nem 1


class Entrada:
    '''para ser usada para testa a sequencia'''

    def __init__(self, n):
        self.n = n
        self.cont = 0
        self.seq = 0
        self.test = True


    def test_seq(self):

        for i in range(0, self.n):
            self.seq = int(input('digite um número:'))

            if self.seq !=0 and self.seq !=1:
                self.cont = self.cont + 1

    def padrao(self):
        if self.cont == 0:
            self.test = True
        else:
            self.test = False

    def __str__(self):
        if self.test == True:
            return  'sequencia padrão'
        else:
            return 'sequência não está no padrão'

if __name__ == "__main__":
    n = int(input('Digite a entrada'))

    num = Entrada(n)
    num.test_seq()
    num.padrao()
    print(num)

