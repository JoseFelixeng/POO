class Matriz:
    '''Representa uma matriz de tamanho nl x nc.'''

    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        '''Inicializa a matriz com 0s.'''
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __repr__(self):
        '''Retorna a matriz em formato de str'''
        s = ''
        for i in range(self._nl):
            for j in range(self._nc):
                s += f'{self._dados[i][j]} '
            s += '\n'
        return s

    def seta_valores(self, valores):
        '''Atribui valores em lista de listas à matriz.'''
        if len(valores) != self._nl or len(valores[0]) != self._nc:
            print('Lista de valores com tamanho incompatível')
        else:
            for i, lin in enumerate(valores):
                for j, v in enumerate(lin):
                    self._dados[i][j] = v

    def _checa_dimensoes(self, b, op=None):
        '''Retorna falso se as dimensões da matriz não são
           compatíveis com as dimensões do parâmetro b, de
           acordo com a op (soma ou multiplicação) desejada.
        '''

        if op == '+' and (self._nc == b._nc and self._nl == b._nl) or op == '*' and (self._nl == b._nc):
            return True
        else:
            return False

    def __getitem__(self, pos):
        '''Operador []: permite acessar
           um elemento da matriz através de m[i,j].
        '''
        for i, lin in enumerate(pos):
            for j, v in enumerate(lin):
                self._dados[i][j] = v
            return v

    def __setitem__(self, pos, v):
        '''Operador []: permite atribuir um valor
           a um elemento da matriz através de m[i,j].
        '''
        i, j = pos
        self._dados[i][j] = v

    def __add__(self, b):
        '''Operador +'''
        s = Matriz._checa_dimensoes(self, b, '+')
        c = []
        if s:
            for i in range(self._nl):
                c.append([])
                for j in range(self._nc):
                    soma = self._dados[i][j] + b._dados[i][j]
                    c[i].append(soma)
        return c

    def __mul__(self, b):
        '''Operador *'''
        nm = []
        if isinstance(b, int):
            for i in range(self._nl):
                nm.append([])
                for j in range(self._nc):
                    mul = self._dados[i][j] * b
                    nm[i].append(mul)
        else:
            m = Matriz._checa_dimensoes(self, b, '*')
            if m == False:
                return 'A matriz é Incompatével'
            elif m == True:
                for i in range(self._nl):
                    nm.append([])
                    for j in range(self._nc):
                        mul = self._dados[i][j] * b._dados[j][i]
                        nm[i].append(mul)

        return nm

    def __eq__(self, b):
        '''Operador =='''
        eq = Matriz._checa_dimensoes(self, b)
        if eq == True:
            for i in range(self._nl):
                for j in range(self._nc):
                    if self._dados[i][j] == b._dados[i][j]:
                        return True
                    else:
                        return False
        else:
            return 'Matrizes com tamanhos Diferentes'

    def __ne__(self, b):
        '''Operador !='''

        if Matriz.__eq__(self, b) == True:
            return False
        else:
            return True


if __name__ == "__main__":
    a = Matriz(3, 3)
    a[0, 2] = 1
    a[1, 1] = 1
    a[2, 0] = 1
    print('Matriz a:')
    print(a)

    b = Matriz(3, 3)
    b.seta_valores([[1.0, 2.0, 0.0],
                    [2.0, 4.0, 5.0],
                    [3.0, 3.0, 0.0]])

    mat_soma = a + b
    print('A + B:')
    print(mat_soma)

    mat_prod = a * b
    print('A * B:')
    print(mat_prod)

    mat_prod = b * 5
    print('B * escalar:')
    print(mat_prod)

    print(f'A != B: {a!=b}')
    b.seta_valores([[0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0]])
    print(f'A == B: {a==b}')
