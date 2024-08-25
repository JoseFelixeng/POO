'''
Interfaces Gráficas com Python e TK.

Lista de Filmes em TK
(Versão com MVC).

Módulo "Model".
'''

class Filme:
    def __init__(self, tit, ano, nota):
        self.titulo = tit
        self.ano = ano
        self.nota = nota

    def __str__(self):
        return f'{self.titulo} ({self.ano}) - {self.nota}'

class ListaFilmes:
    def __init__(self):
        self._filmes = []

    def insere_filme(self, f):
        self._filmes.append(f)

    def atualiza_filme(self, pos, novo_filme):
        self._filmes[pos] = novo_filme

    def remove_filme(self, pos):
        self._filmes.pop(pos)

    def converte_para_lista(self):
        '''
        Gera lista de strings para ser
        usada pela listbox.
        '''
        res = []
        for f in self._filmes:
            res.append(str(f))
        return res

    def __str__(self):
        s = ''
        for f in self._filmes:
            s += str(f) + '\n'
        return s

if __name__ == '__main__':

    l = ListaFilmes()

    f1 = Filme('Vingadores: Ultimato', 2019, 10.0)
    f2 = Filme('Vingadores', 2012, 8.5)
    f3 = Filme('Guerra Civil', 2016, 9.0)

    l.insere_filme(f1)
    l.insere_filme(f2)
    l.insere_filme(f3)

    print(l)

    novo_filme = Filme('Duro de Matar', 1989, 8.0)
    l.atualiza_filme(1, novo_filme)

    print(l)

    l.remove_filme(1)

    print(l)