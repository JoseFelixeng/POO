class Pessoa:
    '''Representa uma pessoa a ser vacinada.'''

    def __init__(self, nome, idade):
        '''Inicializa uma pessoa com o seu nome e idade.'''
        self.__nome = nome
        self.__idade = idade
        self.__doses_vac = 0
        self.__tipo_vac = ''

    def __str__(self):
        if self.__doses_vac == 0:
            return (f'{self.__nome}, {self.__idade} anos ({self.__doses_vac} doses)')
        else:
            return (f'{self.__nome}, {self.__idade} anos ({self.__doses_vac} doses tipo {self.__tipo_vac})')

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, i):
        self.__idade = i

    @property
    def doses_vac(self):
        return self.__doses_vac
    
    @property
    def tipo_vac(self):
        return self.__tipo_vac

    def toma_vacina(self, vac):
        '''Aplica uma vacina na pessoa.'''
        if self.__doses_vac == 0:
            self.__doses_vac += 1
            self.__tipo_vac = vac
            print(f'>Debug: aplicando vacina tipo {vac} em {self.__nome}')
        elif self.__tipo_vac == vac:
            self.__doses_vac += 1
            print(f'>Debug: aplicando vacina do mesmo tipo em {self.__nome}')
        else:
            print(f'>Debug: {self.__nome} tem uma dose do tipo {self.__tipo_vac} e por isso não pode tomar {vac}')
            print('Paciente já vacinado com outro tipo de vacina')

if __name__ == "__main__":
    print('Inicialização:')
    p1 = Pessoa('mario', 33)
    p2 = Pessoa('roberta', 21)
    p3 = Pessoa('vilma', 57)
    print(p1)
    print(p2)
    print(p3)

    print('\nVacinação:')
    p1.toma_vacina('C')
    p1.toma_vacina('C')
    print(p1)

    p3.toma_vacina('A')
    p3.toma_vacina('C')
    print(p3)
    
    p2.nome = 'francisca'
    p2.idade = 48
    p2.toma_vacina('B')
    p2.toma_vacina('B')
    print(p2)