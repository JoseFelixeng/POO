import math

class Robo:
    '''Cria um Robo'''

    def __init__(self, nome):
        '''Inicializa um Robo'''
        self._nome = nome
        self._posicao = [0.0,0.0]
        self.em_op = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo):
        self._nome = novo

    @property
    def posicao(self):
        return self._posicao


    def distancia(self, nova):
        return math.sqrt((self._posicao[0] - nova[0])**2 + ((self._posicao[1] - nova[1])**2))

    def move(self, nova):
        self._posicao = list(nova)

    def __str__(self):
        if not self.em_op :
            return f'Robô: Robo{self._nome} Ocioso em {self._posicao}'
        else:
            return f'Robô: Robo{self._nome} operando em {self._posicao}'


class SistemaMultiRobos:
    '''Inicialização de varios robos'''

    def __init__(self, quantidade):
        self._robos = []
        for i in range(quantidade):
            self._robos.append(Robo(f'{i}'))

    def _acha_robo_ocioso(self):
        for robo in self._robos:
            if not robo.em_op:
                return robo

        return None

    def imprime_robos(self):
        s = '----------------- \n' + 'Robôs do sistema: \n'
        for i in self._robos:
            s += str(i) + '\n'
        print(s + '--------------------------- \n')

    def despacha(self, coordenadas):
        robo = self._acha_robo_ocioso()
        if robo:
            print(f'Robô{robo.nome} livre')
            print(f'Despachando Robo{robo.nome} para ({coordenadas}).')
            print(f'Distancia até o alvo: {robo.distancia(coordenadas)} \n')
            robo.em_op = True
            robo.move(coordenadas)
        else:
            print('Os robos já estão trabalhando')



if __name__ == '__main__':
    smr = SistemaMultiRobos(3) # sistema com 3 robôs
    smr.imprime_robos()

    smr.despacha((5.0, 5.0))
    smr.imprime_robos()
    smr.despacha((-5.0, -5.0))
    smr.imprime_robos()
    smr.despacha((0.0, -10.0))
    smr.imprime_robos()
    smr.despacha((15.0, 15.0))
    smr.imprime_robos()