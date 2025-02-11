# Criar a classe pessoa

class Pessoa:
    '''Classe Pessoa'''

    def __init__(self, nome , idade):
        '''Inicializador da classe'''
        self.__nome = nome
        self.__idade = idade
        self.__doses_vac = 0
        self.__tipo_vac = ''

    @property
    def nome(self):
        '''Retorna o nome'''
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    def __str__(self):
        if self.__doses_vac == 0:
            return '{}, {} anos ({} doses )'.format(self.__nome, self.__idade, self.__doses_vac)
        else:
            return '{}, {} anos ({} doses tipo {})\n'.format(self.__nome, self.__idade, self.__doses_vac, self.__tipo_vac)

    def toma_vacina(self, tipo: str):
        '''Usada para gerenciar a quantidade de vacinas tomadas'''
        self.__novo_tipo = tipo

        if self.__doses_vac == 0:
            self.__doses_vac += 1
            self.__tipo_vac = self.__novo_tipo
            print(f"#aplicando vacina tipo {self.__tipo_vac} em {self.__nome}")
        elif self.__doses_vac  >= 1:
            if self.__tipo_vac == self.__novo_tipo:
                self.__doses_vac += 1
                print(f"#aplicando vacina do mesmo tipo em {self.__nome}")
            else:
                print(f"#{self.__nome} tem uma dose do tipo {self.__tipo_vac} e por isso não pode tomar {self.__novo_tipo}.")


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
    p1.idade = 58
    print(p1)

    p3.toma_vacina('A')
    p3.toma_vacina('C')
    print(p3)

    p2.nome = 'francisca'
    p2.idade = 48
    p2.toma_vacina('B')
    p2.toma_vacina('B')
    print(p2)