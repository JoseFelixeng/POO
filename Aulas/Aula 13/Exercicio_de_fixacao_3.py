class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto2D({self.x}, {self.y})'

    def __add__(self, soma):
        if isinstance(soma, int):
            return Ponto2D(int.x + soma.x, int.y + soma.x)

        if isinstance(soma, Ponto2D):
            return Ponto2D(self.x + soma.x, self.y + soma.y)


if __name__ == '__main__':

    p1 = Ponto2D(2.0, -2.0)
    p2 = Ponto2D(-2.0, 2.0)
    print(p1 + p2)  # retorna Ponto2D
    print(p1 + (5.0, 5.0))  # retorna tupla

    # p3 = p1 * 4  # multiplica por escalar, retorna Ponto2D
    # print(p3)

    # print(p1 * p2)  # produto interno/escalar, retorna nr. real

    #print(p3 == (8.0, -8.0))
    #print(p3 == p1)
