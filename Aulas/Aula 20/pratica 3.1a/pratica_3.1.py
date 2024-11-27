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
        if n_ano <= 1400 or n_ano >= 2100:
            raise ValueError('Ano inválido, por favor preencha novamente!')
        else:
            self._ano = n_ano

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, n_isbn):
        if len(n_isbn) != 6:
            raise TypeError(
                'ISBN inválido por favor preencha novamente os 6 digitos!')
        else:
            self._isbn = n_isbn

    def __str__(self):
        '''Função mostra o nome do livro'''
        return f'Nome: {self._titulo} - Ano: {self._ano} - Codigo do Livro: {self._isbn}  '


class Biblioteca:
    '''Esta classe representa uma biblioteca de livros virtuais'''

    _livros = list()

    def metodoComparar(self, livro):
        '''metodo usado para saber se já existir um livro com o mesmo ISBN'''
        b = Biblioteca._livros
        c = livro
        print('Metodo comparar:\n')
        for i in b:
            print(i)
            if c == i:
                raise TypeError('Livro com mesmo ISBN')
            else:
                print('Não há códigos iguais')

    def metodoCadastrar(self, livro):
        if isinstance(livro, Livro):
            Biblioteca._livros.append(livro)
        else:
            raise TypeError('As Informações Inseridas não são de um livro!')

    def __str__(self):
        s = 'Lista de Livros:\n'
        for i in self._livros:
            s += f'{i} \n'
        return s


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
        if len(n_isbn) != 6:
            raise TypeError(
                'ISBN inválido por favor preencha novamente os 6 digitos!')
        else:
            self._isbn = n_isbn

    def __str__(self):
        '''Função mostra o nome do livro'''
        return f'Nome: {self._titulo} - Ano: {self._ano} - Codigo do Livro: {self._isbn}  '


class Biblioteca:
    '''Esta classe representa uma biblioteca de livros virtuais'''

    _livros = list()

    def metodoComparar(self, livro):
        '''metodo usado para saber se já existir um livro com o mesmo ISBN'''
        b = Biblioteca._livros
        c = livro
        print('Metodo comparar:\n')
        for i in b:
            print(i)
            if c == i:
                raise TypeError('Livro com mesmo ISBN')
            else:
                print('Não há códigos iguais')

    def metodoCadastrar(self, livro):
        if isinstance(livro, Livro):
            Biblioteca._livros.append(livro)
        else:
            raise TypeError('As Informações Inseridas não são de um livro!')

    def __str__(self):
        s = 'Lista de Livros:\n'
        for i in self._livros:
            s += f'{i} \n'
        return s


if __name__ == '__main__':
    # Bloco de Teste
    l = Livro()
    # Entrada o programa
    #l.titulo = input('Nome do livro: ')
    #l.ano = int(input('Ano do livro: '))
    #l.isbn = input('Codigo do livro: ')

    try:
        l.titulo = ''
    except NameError:
        print('Titulo Inválido')
        l.titulo = input('Nome do livro: ')
    else:
        l.titulo = 'Livro sem Nome'
    finally:
        print('Proxima Etapa')

    try:
        l.ano = 1399
    except:
        l.ano = int(input('Insira o ano: '))
    else:
        l.ano = 2000
    finally:
        print('Proxima Etapa')

    try:
        l.isbn = '0000001'
    except:
        print('Erro de Código')
        l.isbn = input('Insira o codigo: ')
    else:
        l.isbn = '000000'
    finally:
        print('Fim do programa')

    print(l)
    l1 = Livro('Capitães de sol', 1941, '000002')
    l2 = Livro('Capitães de mar', 1942, '000003')
    l3 = Livro('ONP', 1399, '000013')
    l4 = Livro('Bleach', 1900, '101928')

    b = Biblioteca()

    b.metodoCadastrar(l)
    b.metodoCadastrar(l1)

    # b.metodoComparar(l1)

    b.metodoCadastrar(l2)
    b.metodoCadastrar(l3)
    b.metodoCadastrar(l4)
    print(b)

    # Bloco para tratar as exceções
