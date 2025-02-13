class Conjunto:
    '''Representa um conjunto de objetos'''
    def __init__(self):
        '''Inicialização da Classe'''
        self.__conjunto = []
        self.__pos = 0

    def adiciona(self, item:str):
        '''Adicionar item caso o mesmo não esteja no conjunto'''
        if self.__pos == 0:
            self.__conjunto.append(item)
            self.__pos +=1
        elif self.__pos > 0 and self.__conjunto.count(item) != True:
            self.__conjunto.append(item)
            self.__pos +=1

    @property
    def conjunto(self):
        return self.__conjunto

    def interseccao(self, conjunto):
        self.__interseccao = Conjunto() # Cria uma variavel do tipo conjunto
        for i in self.__conjunto:
            if i in conjunto and i not in self.__interseccao:
                self.__interseccao.adiciona(i) # usado a função adicionar dos conjuntos para adicionar um elemento ao novo conjunto
        return self.__interseccao

    def __contains__(self, item):
        '''retorna True se o elemento existe dentro do conjunto'''
        return item in self.__conjunto

    def __str__(self):
        if len(self.__conjunto) == 0:
            return '{}'
        return '{' + ', '.join(str(self.__conjunto[i]) for i in range(self.__pos)) + '}'

    def ehVazio(self):
       return len(self.__conjunto) == 0 # Retorna Vazio se o conjunto estiver vazio

if __name__ == '__main__':
    c1 = Conjunto()
    print(c1.ehVazio())
    print(c1)

    c1.adiciona('a')
    c1.adiciona('b')
    c1.adiciona('c')

    print(c1)

    print('a' in c1)
    print('g' in c1)

    c2 = Conjunto()
    c2.adiciona('h')
    c2.adiciona('i')

    c3 = c1.interseccao(c2)
    print(c3.ehVazio())

    c2.adiciona('b')

    print(c2)

    c3 = c1.interseccao(c2)
    print(c3)