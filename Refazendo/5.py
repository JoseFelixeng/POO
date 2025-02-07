#Exercício para fixação: Números complexos
# Implemente a classe Complexo para representar um número complexo. Um número complexo é um número , no qual  é a sua parte real,  é a sua parte imaginária e 
#é .

#Sua classe deve oferecer os seguintes métodos:

#__init__: inicializa um objeto da classe recebendo como parâmetro a sua parte real e imaginária
#reset: atribui 0.0 à parte real e à parte imaginaria.
#__str__: converte o número complexo em uma string no formato 
#soma: retorna um número complexo dado pela soma do próprio objeto com outro. A soma de um número complexo  com outro  é igual ao número complexo 
#modulo: retorna o módulo do número complexo, dado por 
#Utilize o código a seguir como ponto de partida. O código de teste para a sua classe é dado e não deve ser modificado.

import math

class Complexo:
    # implemente o código da classe
    
    def __init__(self , real, img):
        '''Entrada dos dados'''
        self.real = real
        self.img = img
        
    def reset(self):
        '''Atribui 0 para real e 0 para imaginario.'''
        self.real = 0
        self.img = 0

    def modulo(self):
        return math.sqrt((self.real**2 + self.img**2))

    def soma(self, complexo):
        return Complexo(self.real+complexo.real, self.img+complexo.img)
        
    def __str__(self):
        '''Usada para transformar a entrada em numero imaginario.'''
        return '{} + {}i'.format(self.real, self.img)
        
if __name__ == '__main__':
    c1 = Complexo(2, 3)
    c2 = Complexo(10, 7)

    print(c1)
    print(c2)

    c3 = c1.soma(c2)
    print(c3.modulo())

    c3.reset()
    print(c3)