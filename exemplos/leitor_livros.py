# -*- coding: utf-8 -*-

from LivroBiblioteca import Livro, ExcecaoSistema

class LeitorLivros:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.livros = []
        self.arquivo = None

    def _obtem_num_livros(self):
        num = self.arquivo.readline().rstrip('\n')
        if not num.isnumeric():
            raise ErroLeitorQuantidade('Exceção: a primeira linha do arquivo deve conter o número de livros.', num)
        else:
            return int(num)

    def __call__(self):
        self.processa()

    def processa(self):
        with open(self.nome_arquivo, 'r') as self.arquivo:
            n = self._obtem_num_livros()
            for i in range(n):
                try:
                    l = Livro()
                    l.titulo = self.arquivo.readline().rstrip('\n')
                    l.ano = int(self.arquivo.readline().rstrip('\n'))
                    l.isbn = self.arquivo.readline().rstrip('\n')
                except ExcecaoSistema as err:
                    print('\t' + str(err.args[0]))
                    print('\tLinha lida do arquivo: "{}"'.format(err.args[1]))
                else:
                    self.livros.append(l)

if __name__ == "__main__":
    nom_arq = input('Insira o nome do arquivo: ')
    leitor = LeitorLivros(nom_arq)
    leitor()

    print('Livros lidos corretamente do arquivo:')
    for l in leitor.livros:
        print('\t' + str(l))
