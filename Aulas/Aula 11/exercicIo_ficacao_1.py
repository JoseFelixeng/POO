from abc import ABC, abstractmethod


class Animal(ABC):
    '''Classe de animais'''

    def nasce(self):
        pass

    def morre(self):
        pass

    @abstractmethod
    def emite_som(self):
        return('O animal Faz Barulho')


class Mamifero(Animal):
    '''Animal mamifero'''

    def amamentar(self):
        pass


class Ave(Animal):
    '''Animal Ave'''

    def voa(self):
        pass


class gato(Mamifero):
    def emite_som(self):
        s = Animal.emite_som(self)
        return f'{s} O animal era um gato'


class cachorro(Mamifero):
    pass


class ornitorrinco(Mamifero):
    pass


class Aguia(Ave):
    pass


class Pinguim(Ave):
    pass


if __name__ == "__main__":
    a = gato()
    a.emite_som()
