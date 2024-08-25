import math

class Robo:
    def __init__(self, nome):
        self.__nome = nome
        self.__posicao = [0.0, 0.0]
        self.em_op = False
        
    def __str__(self):
        if not self.em_op:
            return f'Robô: {self.__nome}, ocioso em {self.__posicao}'
        else:
            return f'Robô: {self.__nome}, esta operando nas coordenadas {self.__posicao}'
    
    def distancia(self, px, py):
        di = (px - self.__posicao[0])**2 + (py - self.__posicao[1])**2
        df = math.sqrt(di)
        return df
    
    def move(self, posicao_nx, posicao_ny):
        d = self.__posicao
        d[0] = posicao_nx
        d[1] = posicao_ny
        return d
    
    @property
    def nome(self):
        '''Retorna um nome'''
        return self.__nome 
    
    @nome.setter
    def nome(self, nome_n):
        '''Renomea o robo'''
        self.__nome = nome_n 
        
    @property
    def posicao(self):
        '''Retorna a posição'''
        return self.__posicao 
        
class SistemaMultiRobos:
    def __init__(self, quant_robos):
        self._robos = []
        for i in range(quant_robos):
            if i == 0:
                self._robos.append(Robo('Robo0'))
            elif i == 1:
                self._robos.append(Robo('Robo1'))
            elif i == 2: 
                self._robos.append(Robo('Robo2'))
    
    def _acha_robo_ocioso(self):
        r = self._robos
        for i , ro in enumerate(r):
            print(f'{ro}')
            if ro.em_op == False:
                return(f'{ro}')
    
    def imprime_robos(self):
        print('-------------------------------------------')
        print('Sistema de Robos: ')
        for i , ro in enumerate(self._robos):
            print(f'{ro}')
        print('-------------------------------------------')
      
    def despacha(self, l_nova):
        for i , ro in enumerate(self._robos):
            if not ro.em_op:
                print(f'Robô, {ro.nome} livre')
                print(f'Despachando {ro.nome} para {l_nova}')
                d = l_nova[0]**2 + l_nova[1]**2
                d1 = math.sqrt(d)
                print(f'A distancia até o local é {d1}')
            else:
                print('Todos os Robos Ocupados')
    
    
    
    
     
if __name__ == '__main__':
    r1 = Robo('Robo')
    print(r1)
    print(r1.distancia(5.0, 5.0))
    print(r1.move(6.0,6.0))
    smr = SistemaMultiRobos(3)
    smr.imprime_robos()
    smr._acha_robo_ocioso()
    smr.despacha((5.0 , 5.0))