class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa{self.nome, self.idade}'

    def compara_idades(self, p2):
        '''Retorna verdadeiro se self for mais novo que p2.'''
        return self.idade <= p2.idade

    def cumprimenta(self, p):
        '''Cumprimenta um objeto p do tipo Pessoa'''
        print(f'Olá {p.nome}, tudo bem?')

    def lista_idade(self, lista):
        '''Mede a idade de todos'''
        s = 0
        cont = 0
        for i in lista:
            s += i.idade
            cont += 1
        print(f'A média é: {s/cont}')


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def __repr__(self):
        return f'Aluno{self.nome, self.idade, self.matricula}'


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento):
        super().__init__(nome, idade)
        self.departamento = departamento

    def __repr__(self):
        return f'Professor{self.nome, self.idade, self.departamento}'


if __name__ == "__main__":
    p = Pessoa('joao', 25)
    a = Aluno('hugo', 20, 111)
    prof = Professor('santos', 40, 'ECT')

    p1 = Pessoa('maria', 28)
    # método "compara_idades" funciona com qualquer objeto que tenha o atributo "idade"
    print(p1.compara_idades(prof))
    lp = [p, a, prof, p1]

    for pess in [p, a, prof]:
        print(pess)  # executa o __repr__ de cada objeto na lista


p.lista_idade(lp)
