import math

class Matriz:
    '''Representa uma matriz de tamanho nl x nc.'''

    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def _checa_dimensoes(self, b, op):
        if op == 0:
            if self._nl != b._nl or self._nc != b._nc:
                print('Dimensoes das matrizes nao sao iguais')
                return False
        if op == 1:
            if self._nc != b._nl:
                print('Dimensoes das matrizes nao sao compativeis')
                return False
        return True

    def __repr__(self):
        s = ''
        for i in range(self._nl):
            for j in range(self._nc):
                s += '{} '.format(self._dados[i][j])
            s += '\n'
        return s

    def seta_valores(self, valores):
        if len(valores) != self._nl or len(valores[0]) != self._nc:
            print('Lista de valores com tamanho incompatível')
        else:
            for i, lin in enumerate(valores):
                for j, v in enumerate(lin):
                    self[i, j] = v

    def __getitem__(self, pos):
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                return self._dados[l][c]

    def __setitem__(self, pos, v):
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                self._dados[l][c] = v

    def __add__(self, b):
        if type(b) != Matriz:
            print('b deve ser do tipo Matriz')
        else:
            if self._checa_dimensoes(b, 0):
                r = Matriz(self._nl, self._nc)
                for i in range(self._nl):
                    for j in range(self._nc):
                        r[i,j] = self[i,j] + b[i,j]
                return r

    def __mul__(self, b):
        if isinstance(b, Matriz):
            if self._checa_dimensoes(b, 1):
                r = Matriz(self._nl, b._nc)
                for i in range(self._nl):
                    for j in range(b._nc):
                        for k in range(self._nc):
                            r[i,j] += self[i,k]*b[k,j]
                return r
        elif isinstance(b, (int, float)):
            r = Matriz(self._nl, self._nc)
            for i in range(self._nl):
                for j in range(self._nc):
                    r[i,j] = b*self[i,j]
            return r
        else:
            print('Parâmetro deve ser do tipo Matriz ou escalar')

    def __eq__(self, b):
        if not self._checa_dimensoes(b, 0):
            return False
        else:
            for i in range(self._nl):
                for j in range(self._nc):
                    if self[i,j] != b[i,j]:
                        return False
        return True

    def __ne__(self, b):
        return not self.__eq__(b)

if __name__ == "__main__":
    a = Matriz(3, 3)
    a[0,2] = 1
    a[1,1] = 1
    a[2,0] = 1
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