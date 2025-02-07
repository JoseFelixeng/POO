
"""Exercício para fixação: Máquina de Café

Uma máquina de café aceita moedas de 5 e 10 centavos. Um café custa X reais. Implemente uma classe que simule
a operação da máquina de café. A classe deve oferecer métodos para saber se o café está disponível e se
houver troco. Por exemplo, se $X=50$ centavos, a máquina funcionaria como a seguir:

```
10 c. (faltam 40 c)
10 c. (faltam 30 c)
5 c. (faltam 25 c)
10 c. (faltam 15 c)
5 c. (faltam 10 c)
5 c. (faltam 5 c)
10 c. Troco: 5 c.
Café disponível!!
```

Antes de escrever código, reflita:
- Quais são os atributos para determinar o estado da máquina?
- Quais desses atributos deveriam ser privados e quais públicos?
- Dos atributos privados, em quais você implementaria getters? Em quais setters?
- Quais são os métodos que a máquina deveria oferecer em sua interface pública?

"""

class Maquina_cafe:
    '''Classe irá descrever uma maquina de café'''

    def __init__(self, moeda):
        '''Inicializaçõa da classe'''
        self.__moeda = moeda
        self.__valor = 50
        self.__totalPago = 0
        self.__cd = False

    def __str__(self):
        '''Interface de Saída'''
        return '{} c. (faltam {} c'.format(self.__moeda, self.__totalPago)



if __name__ == "__main__":
