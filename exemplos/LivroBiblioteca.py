class ExcecaoSistema(Exception):
    '''Classe base de exceção do sistema'''
    pass

class ExcecaoTituloLivro(ExcecaoSistema):
    '''Exceção no título do livro'''
    pass

class ExcecaoAnoLivro(ExcecaoSistema):
    '''Exceção no ano do livro'''
    pass

class ExcecaoISBNLivro(ExcecaoSistema):
    '''Exceção no ISBN do livro'''
    pass

class ExcecaoISBNBiblioteca(ExcecaoSistema):
    '''Exceção de ISBN repetido entre dois livros diferentes'''
    pass

class ExcecaoArmazenamentoBiblioteca(ExcecaoSistema):
    '''Exceção de repetição no armazenamento da biblioteca'''
    pass

class Livro:

    def __init__(self):
        self._titulo = ''
        self._ano = 0
        self._isbn = ''

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, a_titulo):
        if bool(a_titulo):
            self._titulo = a_titulo
        else:
            raise ExcecaoTituloLivro('Exceção: título do livro deve ser uma string não vazia', a_titulo)
    
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, a_ano):
        if 1400 <= a_ano <= 2100:
            self._ano = a_ano
        else:
            raise ExcecaoAnoLivro('Exceção: ano do livro deve estar entre 1400 e 2100', a_ano)

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, a_isbn):
        if len(a_isbn) >= 6:
            self._isbn = a_isbn
        else:
            raise ExcecaoISBNLivro('Exceção: ISBN do livro deve conter pelo menos 6 caracteres', a_isbn)

    def __repr__(self):
        return f'{self.titulo}, {self.ano} - {self.isbn}'

class Biblioteca:

    def __init__(self):
        self._livros = []

    def cadastra(self, livro):
        if type(livro) != Livro:
            raise TypeError('Exceção: Parâmetro deve ser do tipo Livro')
        if livro in self._livros:
            raise ExcecaoArmazenamentoBiblioteca('Exceção: este livro já está cadastrado na biblioteca')
        if self.busca_por_isbn(livro):
            raise ExcecaoISBNBiblioteca('Exceção: este livro já está cadastrado com outro ISBN')

        self._livros.append(livro)

    def busca_por_isbn(self, livro):
        for l in self._livros:
            if l.isbn == livro.isbn:
                return True
        else:
            return False

if __name__ == "__main__":

    # Instanciação dos livros
    try:
        l1 = Livro()
        l1.titulo = '' # erro 1
        l1.ano = 2000 # erro 2
        l1.isbn = '123456' # erro 3

        l2 = Livro()
        l2.titulo = 'titulo 2'
        l2.ano = 2005
        l2.isbn = '123456'
    except ExcecaoTituloLivro as err:
        print(err.__class__.__name__ + ': ' + str(err))
        l1.titulo = input('Insira um novo título para o livro: ')
    except ExcecaoAnoLivro as err:
        print(err.__class__.__name__ + ': ' + str(err))
        l1.ano = int(input('Insira um novo ano para o livro: '))
    except ExcecaoISBNLivro as err:
        print(err.__class__.__name__ + ': ' + str(err))
        l1.isbn = input('Insira um novo ISBN para o livro: ')

    # Cadastro dos livros
    b = Biblioteca()

    b.cadastra(l1) # erro 4
    #b.cadastra(l1)
    #b.cadastra(l1) # erro 5
    #b.cadastra(l2) # erro 6
    for l in b._livros:
        print(l)