from gerenciador_recursos import GerenciadorRecursos
from abc import ABC, abstractmethod


class Recurso(GerenciadorRecursos):
    '''Classe de Recurso'''

    def __init__(self, nome):
        self.nome = nome
        self.numero_tarefas = 0
        self.ocupado = False

    def reserva(self, n_tarefas):
        if not self.ocupado:
            self.ocupado = True
            self.numero_tarefas = n_tarefas

    @abstractmethod
    def processa(self):
        if self.ocupado == True:
            self.numero_tarefas = self.numero_tarefas - 1
            print('Tarefa sendo realizada')
        if self.numero_tarefas == 0:
            self.ocupado = False
            print('Recurso Liberado')

    def libera(self):
        if self.ocupado == True and self.numero_tarefas != 0:
            self.ocupado = False
            self.numero_tarefas = 0
        elif self.ocupado == False:
            self.numero_tarefas = 0

    def __repr__(self):
        return f'Recurso: {self.nome}, Tarefas: {self.numero_tarefas}, Ocupado: {self.ocupado}, Tipo:'

    @property
    def tipo(self):
        return self.__class__.__name__


class Impressora(Recurso):
    '''Classe Impressora'''

    def __init__(self, nome):
        super().__init__(nome)

    def processa(self):
        return super().processa()

    def Estender(self):
        e = Recurso.__repr__(self)
        r = Recurso.tipo(self)
        return f'{e} Impressor {r}'


class Cafeteira(Recurso):
    '''Classe Cafeteira'''

    def __init__(self, nome):
        super().__init__(nome)

    def processa(self):
        return super().processa()

    def Estender(self):
        e = __repr__(self)
        return f'{e} Cafeteira'


if __name__ == "__main__":
    g = GerenciadorRecursos()

    r1 = Cafeteira('cafeteira1')
    r2 = Cafeteira('cafeteira2')
    r3 = Impressora('impressora1')
    r4 = Impressora('impressora2')
    g.adiciona(r1)
    g.adiciona(r2)
    g.adiciona(r3)
    g.adiciona(r4)
    print('>>> Estado Inicial:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 1)
    g.reserva('Impressora', 1)
    print('\n>>> Após reservar:')
    g.imprime_recursos()
    print('')

    g.processa_todos()
    print('\n>>> Após processar tarefas:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 5)
    g.reserva('Cafeteira', 1)
    g.libera('cafeteira1')
    print('\n>>> Após reservar e liberar:')
    g.imprime_recursos()
    print('')
