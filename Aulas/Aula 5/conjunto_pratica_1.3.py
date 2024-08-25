class Conjunto:
    def __init__(self):
        self.__elementos = []

    def __str__(self):
        s = '{'
        for i, e in enumerate(self.__elementos):
            s += f'{e}'
            if(i != len(self.__elementos) - 1):
                s+= ', '
        s += '}'
        return s

    def adiciona(self, o):
        if not o in self.__elementos:
            self.__elementos.append(o)

    def __contains__(self, e):
        return e in self.__elementos

    def ehVazio(self):
        return not bool(len(self.__elementos))

    def interseccao(self, c):
        r = Conjunto()
        for e in self.__elementos:
            if e in c:
                r.adiciona(e)
        return r

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
