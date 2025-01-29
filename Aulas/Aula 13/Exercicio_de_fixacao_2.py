from abc import ABC, abstractmethod


class Animal(ABC):
    '''Classe abstrata'''

    def __init__(self):
        self.nasce()

    @abstractmethod
    def nasce(self):
        pass

    def morre(self):
        print('Animal morreu')

    @abstractmethod
    def emite_som(self):
        pass


class Mamifero(Animal):
    '''Abstrata: não implementa o método emite_som'''

    def amamenta(self):
        print('Mamífero amamentou')

    def nasce(self):
        print('Mamífero nasceu do ventre')


class Ave(Animal):
    '''Abstrata: não implementa o método emite_som'''

    def voa(self):
        self.voar = True
        print('Ave voou')

    def nasce(self):
        print('Ave nasceu do ovo')

    @abstractmethod
    def pode_voar(self):
        '''Se o animal puder Voar'''
        if self.voar:
            return True
        else:
            return False

    def classe_ave(self, l_a):
        s = []
        for i in l_a:
            if i.voa:
                s += i
                print(s)
        return s


class Gato(Mamifero):

    def emite_som(self):
        print('Miau')


class Cachorro(Mamifero):

    def emite_som(self):
        print('Au')


class Ornitorrinco(Mamifero):

    def emite_som(self):
        print('Prprpr')

    def nasce(self):
        print('Ornitorrinco nasceu do ovo')


class Pinguim(Ave):

    def emite_som(self):
        print('Quack')

    def voa(self):
        self.voar = False
        print('Pinguim não voa')

    def pode_voar(self):
        return False


class Aguia(Ave):

    def voa(self):
        self.voar = True
        print('Gararrr')

    def pode_voar(self):
        return True

    def emite_som(self):
        print('In')


if __name__ == "__main__":
    g = Gato()
    c = Cachorro()
    o = Ornitorrinco()
    p = Pinguim()
    a = Aguia()
    p1 = Pinguim()
    a1 = Aguia()
    a.voa()
    p.voa()

    aves = [p, p1, a, a1]

    animais = [g, c, o, p, a]

    for a in animais:
        # So para testar, imprimimos o nome da classe
        print(f'Nome da classe: {a.__class__.__name__}')
        a.emite_som()
        a.morre()
        print(p.pode_voar())

    Ave.classe_ave(aves, aves)
