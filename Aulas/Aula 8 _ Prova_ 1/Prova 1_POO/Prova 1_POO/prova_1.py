import math 

class Robo:
    '''Aqui será feito os robos'''
    
    def __init__(self, nome, posicaox, posicaoy, em_op):
        self.__nome = nome
        self.__posicaox = 0.0
        self.__posicaoy = 0.0
        self.em_op = True
        
    def __str__(self):
        '''Retorna uma string do robo'''
        return f'Robô: {self.__nome}, ocioso em  [ {self.posicaox} , {self.__posicaoy} ]'
    
    def distancia(self, px, py):
        a = (px - self.__posicaox)**2 + (py - self.__posicaoy)**2
        b =  math.sqrt(a)
        return b 
    
    def move(self, posicaox_n, posicaoy_n):
        '''Retona uma nova posicao do robo (x,y)'''
        self.__posicaox = posicaox_n
        self.__posicaoy = posicaoy_n
        return f'[{self.__posicaox} , {self.__posicaoy}]'
    
        
    @property
    def nome(self):
        '''Retornar  o nome do robo'''
        return self.__nome
    
    @nome.setter
    def nome(self, novo_n):
        '''Renomear o robo'''
        self.__nome = novo_n
        
            
    @property
    def posicaox(self):
        '''Retornar  a posicaox do robo'''
        return self.__posicaox
    
    @property
    def posicaoy(self):
        '''Retornar  a posicaoy do robo'''
        return self.__posicaoy
    
class SistemaMultiRobos:
    '''Feita para configurar os robos'''
    
    def __init__(self, quant_robos):
        self.__robos = []
        for i in range(quant_robos):
            self.__robos.append(Robo(i+1,i+1,i+1,i+1))
    
    def _acha_robo_ocioso(self):
        for i in range(self.__robos):
            if self.em_op == False:
                return f'{self.__nome}'
            else:
                print('Não há nenhum robo ocioso')
    
    def imprime_robos(self):
        ro = f'Robôs do sistema: '
        for s in self.__robos:
            ro += '\n' + str(s)
    
        return ro 
     
    
    def despacha(self, posicao_x, posicao_y):
        for i , rp in enumerate(self.__robos):
            if self.em_op == False: 
                self.__posicaox = posicao_x
                self.__posicaoy = posicao_y
        
        d = Robo.distancia(posicao_x, posicao_y)
        print(f'Despachando {self.__nome} para {d}')
    
    
    
    
#DADOS DA SAIDA:    
if __name__ == '__main__':
   
    smr = SistemaMultiRobos(3) # sistema com 3 robôs
    smr.imprime_robos()

    smr.despacha(5.0, 5.0)
    smr.imprime_robos()
    smr.despacha(-5.0, -5.0)
    smr.imprime_robos()
    smr.despacha(0.0, -10.0)
    smr.imprime_robos()
    smr.despacha(15.0, 15.0)
    smr.imprime_robos()
    