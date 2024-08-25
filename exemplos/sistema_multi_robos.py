import math

class Robo:
    def __init__(self, nome):
        self._nome = nome
        self._posicao = [0.0, 0.0]
        self.em_op = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, n):
        self._nome = n

    @property
    def posicao(self):
        return self._posicao

    def __str__(self):
        if self.em_op:
            return f'Robô: {self._nome}, operando em {self._posicao}'
        else:
            return f'Robô: {self._nome}, ocioso em {self._posicao}'

    def distancia(self, posicao):
        return math.sqrt((self._posicao[0] - posicao[0])**2 +
                         (self._posicao[1] - posicao[1])**2)

    def move(self, posicao):
        self._posicao[0] = posicao[0]
        self._posicao[1] = posicao[1]

class SistemaMultiRobos:
    def __init__(self, n_robos):
        self._robos = []
        ult_x = 0.0
        for i in range(n_robos):
            r = Robo('Robo' + str(i))
            r.move((ult_x, 0.0))
            ult_x += 1.0
            self._robos.append(r)

    def _acha_robo_ocioso(self):
        for r in self._robos:
            if not r.em_op:
                print(f'Robô {r.nome} livre')
                return r
        else:
            print('Todos os robôs ocupados')

    def imprime_robos(self):
        print('-----------------')
        print('Robôs do sistema:')
        for r in self._robos:
            print(r)
        print('-----------------')

    def despacha(self, posicao):
        r = self._acha_robo_ocioso()
        if r:
            r.em_op = True
            print(f'Despachando {r.nome} para {posicao}.\n'
                  f'Distancia até o alvo: {r.distancia(posicao)}')
            r.move(posicao)

if __name__ == '__main__':
    smr = SistemaMultiRobos(3)
    smr.imprime_robos()

    smr.despacha((5.0, 5.0))
    smr.imprime_robos()
    smr.despacha((-5.0, -5.0))
    smr.imprime_robos()
    smr.despacha((0.0, -10.0))
    smr.imprime_robos()
    smr.despacha((15.0, 15.0))
    smr.imprime_robos()
