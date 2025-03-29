# Implemente um programa que leia do usuário um total N de números reais e imprima na tela qual foi o
# maior número digitado.

class Numero:
    """A Classe deve testar uma entrada de N Números

    Returns:
        _Inteiro_: _O maior e o menor numero da sequência_
    """
    '''Essa classe é feita para definir a quantidade de numeros a serem testados'''

    def __init__(self, n: int):
        '''Inicialização da classe'''
        self.n = n
        self.maior = None
        self.menor = None

    def test_maior(self):

        for i in range(self.n):
            self.atual= int(input(f'Digite um numero n°{i+1}\n'))

            if self.maior is None or self.atual > self.maior:
                self.maior = self.atual
                
            if self.menor is None or self.atual < self.menor:
                self.menor = self.atual
            
 
        return self.maior, self.menor 

    def __str__(self):
        return 'O maior numero é {} e o menor é {}'.format(self.maior, self.menor)



if __name__ == "__main__":
    n = int(input('Quantos numeros serão digitados '))
    
    if n <= 0:
        print("O número digitado é menor que zero, Por favor digite um novo número!!!!")
    else:
        r = Numero(n)
        r.test_maior()
        print(r)
