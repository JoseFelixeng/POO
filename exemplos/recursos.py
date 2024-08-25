# -*- encoding: utf-8 -*-

from gerenciador_recursos import GerenciadorRecursos
from abc import ABC, abstractmethod

class Recurso(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.num_tarefas = 0
        self.ocupado = False

    @abstractmethod
    def __repr__(self):
        return f'Recurso: {self.nome}, Tarefas: {self.num_tarefas}, Ocupado: {self.ocupado}'

    @property
    def tipo(self):
        return self.__class__.__name__

    def reserva(self, n):
        if not self.ocupado:
            self.num_tarefas = n
            self.ocupado = True

    @abstractmethod
    def processa(self):
        print(f'>Recurso {self.nome} com processamento solicitado')
        if self.num_tarefas > 0:
            self.num_tarefas -= 1
            print('>Tarefa processada')
            if self.num_tarefas == 0:
                print(f'>Recurso {self.nome} liberado')
                self.ocupado = False
            return True
        else:
            print(f'>Nao ha tarefas a serem processadas')
            return False

    def libera(self):
        print(f'>Recurso {self.nome} com liberacao solicitada')
        if self.ocupado:
            self.num_tarefas = 0
            self.ocupado = False
            print(f'>Recurso {self.nome} liberado')
        else:
            print(f'>Recurso {self.nome} ja se encontra livre para uso')

class Impressora(Recurso):

    def __repr__(self):
        s = Recurso.__repr__(self)
        s += ', Tipo: Impressora\n'
        s += '=============================================='
        return s
    
    def processa(self):
        if Recurso.processa(self):
            print('Realizando impressao')
            print('...')
            print('Impressao realizada com sucesso')
        else:
            print('>Impressora deve ser reservada previamente')

class Cafeteira(Recurso):

    def __repr__(self):
        s = Recurso.__repr__(self)
        s += ', Tipo: Cafeteira\n'
        s += '=============================================='
        return s

    def processa(self):
        if Recurso.processa(self):
            print('Fazendo cafe')
            print('...')
            print('Cafe feito com sucesso')
        else:
            print('>Cafeteira deve ser reservada previamente')

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