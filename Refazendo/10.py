class Obra:

    def __init__(self, nome, autor, ano):
        self._nome = nome
        self._autor = autor
        self._ano = ano


    @property
    def nome(self):
        '''Nome da Obra'''
        return self._nome

    @property
    def autor(self):
        '''Autor da Obra'''
        return self._autor

    @property
    def ano(self):
        '''Ano de lançamento da Obra'''
        return  self._ano


    def __str__(self):
        return f'{self._nome}, da {self._autor} ({self._ano})'


class Museu:
    #insira aqui o código da classe

    def __init__(self, museu):
        self._museu = museu
        self._obras =[]
        self._pos = 0

    @property
    def obras(self):
        return self._obras

    @property
    def nome(self):
        return self._museu

    def adiciona_obra(self, obra):
        if self._pos == 0:
            self._obras.append(obra)
            self._pos +=1
        elif self._pos > 0:
            self._obras.append(obra)
            self._pos += 1


    def remove_obra(self, nome):
        '''
           obra representa cada objeto da classe Obra dentro da lista _obras.
           obra.nome acessa o atributo nome de cada instância de Obra.
           obra.nome.lower() != nome.lower() compara sem diferenciar maiúsculas e minúsculas.
        '''
        self._obras = [obra for obra in self._obras if obra.nome.lower() != nome.lower()]

    def imprime_obras(self):
        m = f'Obras do museu "{self._museu}" '
        for i in self._obras:
            m += '\n'+ '  ' + str(i)
        print(m)


if __name__ == '__main__':
    # cria obras
    o1 = Obra('mona lisa', 'da vinci', 1797)
    o2 = Obra('a noite estrelada', 'van gogh', 1889)
    o3 = Obra('guernica', 'picasso', 1937)
    o4 = Obra('a persistencia da memoria', 'dali', 1931)

    # cria museu
    m = Museu('museu magnifico')

    # adiciona obras criadas ao museu
    m.adiciona_obra(o1)
    m.adiciona_obra(o2)
    m.adiciona_obra(o3)
    m.adiciona_obra(o4)

    # imprime obras
    m.imprime_obras()


    # remove obras do museu
    m.remove_obra('a ultima ceia') # nao faz nada
    m.remove_obra('guernica')

    # imprime obras
    m.imprime_obras()

    # obra continua a existir mesmo tendo sido removida do museu
    print('Obra removida:')
    print(o3)
