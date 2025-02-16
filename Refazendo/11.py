class Carro:
    '''Usada  para instanciar carros'''

    def __init__(self, marca= '', modelo =''):
        '''Inicialização'''
        self._marca = marca
        self._modelo = modelo

    def __str__(self):
        return f'{self._marca}  {self._modelo}'

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

class Patio:
    '''Iniciaalização do patio'''

    def __init__(self, nome_p):
        self._patio = nome_p
        self._carros = []
        self._pos = 0

    @property
    def nome_p(self):
        return self._patio

    @property
    def carros(self):
        return self._carros

    def quantos(self):
        return len(self._carros)

    def adiciona_carro(self, carro):
        if self._pos == 0:
            self._carros.append(carro)
            self._pos += 1
        elif self._pos > 0:
            self._carros.append(carro)
            self._pos += 1


    def imprime_carros(self):
        s = f'Carros do Patio {self._patio}'
        for i in self._carros:
            s += '\n'+ '  ' + str(i)
        print(s)

class Oficina:
    def __init__(self):
        self._pf = Patio('frances')
        self._pa = Patio('alemão')
        self._pam = Patio('americano')
        self._ncarro = Carro()

    def adiciona_carro(self, carro):
        self._ncarro = carro
        if self._ncarro.marca == 'bmw' or self._ncarro.marca == 'audi':
            self._pa.adiciona_carro(carro)
        elif self._ncarro.marca == 'renault' or self._ncarro.marca == 'citroen':
            self._pf.adiciona_carro(carro)
        elif self._ncarro.marca == 'chevrolet' or self._ncarro.marca == 'ford':
            self._pam.adiciona_carro(carro)


    def imprime_carros(self):
        if self._pa.quantos() != 0:
            self._pa.imprime_carros()
        if self._pf.quantos() != 0:
            self._pf.imprime_carros()
        if self._pam.quantos() != 0:
            self._pam.imprime_carros()


if __name__ == "__main__":
    # cria instâncias da classe carro
    c1 = Carro('audi', 'a3')
    c2 = Carro('bmw', 'm3')
    c3 = Carro('citroen', 'c4')
    c4 = Carro('renault', 'clio')
    c5 = Carro('chevrolet', 'malibu')
    c6 = Carro('ford', 'focus')


    # cria uma instância de oficina
    # observe que pátios são criados pela oficina (composição)
    ofic = Oficina()
    # adiciona carros à oficina
    #(os carros são adicionados aos pátios apropriados dentro do métodos
    ofic.adiciona_carro(c1)
    ofic.adiciona_carro(c2)
    ofic.adiciona_carro(c3)
    ofic.adiciona_carro(c4)
    ofic.adiciona_carro(c5)
    ofic.adiciona_carro(c6)

    # imprime os carros da oficina (imprime os carros de cada pátio)
    ofic.imprime_carros()