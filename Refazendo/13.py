import random

class Produto:
    '''Esta é a classe Produto'''
   __produtos = []

    def __init__(self, preco):
        self._codigo = random.randint(1, 999)
        self._preco = preco
        self.desconto = False


    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, new):
        self._preco = new

    def preco_com_desconto(self, new_d):
        self.desconto = True
        desconto = self._preco * (new_d/100 )
        self._preco = self._preco - desconto
        return self._preco

    def imprime_instancias(self):
        for i in __produtos:
            print(i)


class Livro:
    '''Definir o que é um livro'''

    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor



class Jogo:
    '''defini o que é um jogo '''

    def __init__(self, nome, plataforma):
        self._nome = nome
        self._plataforma = plataforma

    def ativa_desconto(self):




if __name__ == "__main__":
    if __name__ == '__main__':
        l1 = Livro('O homem duplicado', 'Jose Saramago', 30.00)
        l2 = Livro('O idiota', 'Fiodor Dostoievski', 35.00)
        l2.ativa_desconto()
        l3 = Livro('Revolução dos bichos', 'George Orwell', 35.00)
        j1 = Jogo('Street Fighter V', 'PS4', 200.00)
        j2 = Jogo('Call of Duty: Black Ops Cold War', 'PS4', 250.00)
        j2.ativa_desconto()
        j3 = Jogo('Call of Duty: Black Ops Cold War', 'Xbox One', 250.00)
        j3.ativa_desconto()
        j4 = Jogo('Forza Horizon 4', 'Xbox One', 200.00)
        j5 = Jogo('Zelda: Breath of the Wild', 'Switch', 300.00)
        j5.ativa_desconto()
        Produto.imprime_instancias()
