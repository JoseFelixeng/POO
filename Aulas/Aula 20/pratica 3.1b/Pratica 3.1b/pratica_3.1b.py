class ExcecaoSistema(Exception):
    pass


class Livro:
    '''Esta classe representa um livro virtual'''

    def __init__(self, titulo='', ano=0, isbn='000000'):
        '''Inserindo as informações do livro'''
        self._titulo = titulo
        self._ano = ano
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, n_titulo):
        if n_titulo != '':
            self._titulo = n_titulo
        else:
            raise NameError('O titulo precisa ser preenchido!')

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, n_ano):
        if n_ano >= 1400 and n_ano <= 2100:
            self._ano = n_ano
        else:
            raise ValueError('Ano inválido, por favor preencha novamente!')

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, n_isbn):
        if len(n_isbn) >= 6:
            self._isbn = n_isbn
        else:
            raise TypeError(
                'ISBN inválido por favor preencha novamente os 6 digitos!')

    def __str__(self):
        '''Função mostra o nome do livro'''
        return f'Nome: {self._titulo} - Ano: {self._ano} - Codigo do Livro: {self._isbn}\n'


class LeitorLivros:
    '''classe de um leitor de livros digital'''

    def __init__(self, nome):
        self.nome_arquivo = nome
        self.livros = list()
        self.arquivo = ''

    def processa(self):
        with open(self.nome_arquivo, 'r') as self.arquivo:
            # Lê a a qtd. de livros n
            # Para i = 0.. n-1
            m = self.arquivo.readlines()
            p = int(m[0])
            i = 0
            while p > i:
                titulo = m[1]
                ano = int(m[2])
                isbn = m[3]
                try:
                    l = Livro()
                    # Obtém título (método privado auxiliar)
                    if titulo != '\n':
                        l.titulo = titulo
                    else:
                        try:
                            l.titulo = titulo
                        except:
                            print('Titulo Inválido')
                        else:
                            print('Titulo com erros, por favor tente novamente')
                        finally:
                            l.titulo = input('Digite o nome do livro: \n')
                            print(f'Titulo Atualizado para => {l.titulo}\n')
                    # Obtém ano (método privado auxiliar)
                    if ano >= 1400 and ano <= 2100:
                        l.ano = ano
                    else:
                        try:
                            l.ano = ano
                        except:
                            print('Ano inválido')
                        else:
                            print('Ano errado, por favor tente novamente')
                        finally:
                            n_ano = int(input('Digite o ano do livro: '))
                            l.ano = n_ano
                            print(f'Ano atualizado para => {l.ano}\n')
                    # Obtém ISBN (método privado auxiliar)
                    if len(isbn) >= 6:
                        l.isbn = isbn
                    else:
                        try:
                            l.isbn = ' '
                        except:
                            print('Erro de Código')
                        else:
                            print('Erro de código, por favor tente novamente')
                        finally:
                            l.isbn = input('Digite o código correto: ')
                            print(f'Código atualizado => {l.isbn}\n')
                except ExcecaoSistema as err:  # (prática anterior)
                    print(err)
                else:
                    # Adiciona livro à self.livros
                    self.livros.append(l)
                    print(l)
                m.pop(1)
                m.pop(1)
                m.pop(1)
                i += 1


if __name__ == '__main__':

    nom_arq = input('Insira o nome do arquivo: ')
    leitor = LeitorLivros(nom_arq)
    leitor.processa()

    print('Livros lidos corretamente do arquivo:')
    for l in leitor.livros:
        print('\t' + str(l))

    # para testar a classe livro
    #livro = Livro()
    # try:
    #    livro.titulo = ''
    # except:
        #print('Titulo Inválido')
    # finally:
    #   print('Preencha um titulo válido')
    #    livro.titulo = input('Titulo do livro: ')

    # try:
    #   livro.ano = 0
    # except:
    #    print('Ano Inadequado')
    # finally:
    #    print('Preencha um ano valido')
    #    livro.ano = int(input('Ano do livro'))

    # try:
    #    l.isbn = ''
    # except:
    #    print('Erro de Código')
    # finally:
    #    print('Preencha com código válido')
    #    livro.isbn = input('Código do livro: ')

    # print(livro)
