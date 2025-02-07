
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

    def __init__(self):
        '''Inicializaçõa da classe'''

        self.__moeda = 0
        self.__valor = 50
        self.__cd = False
        self.__troco = 0

    def __str__(self):
        '''Interface de Saída'''
        return 'Voce inseriu {} c. (troco {} c)'.format(self.__moeda, self.__moeda - self.__valor)

    def pagamento(self):
        while(self.__moeda < self.__valor):

            inserida = int(input('insira uma moeda para receber o café \n'))

            if inserida == 5 or inserida == 10:
                self.__moeda += inserida
                print('{} c (faltam {} c)'.format(inserida, self.__valor -self.__moeda))
            else:
                print('Erro por favor insira uma moeda correta \n')


    def solta_cafe(self):
        if self.__moeda == self.__valor or self.__valor < self.__moeda:
            print('=====================')
            print('Café Disponível')
            print('=====================')


    def troco(self):
        if self.__moeda > self.__valor:
            self.__troco = self.__moeda - self.__valor
            return self.__troco
        else:
            print('Você não possui troco\n')


if __name__ == "__main__":
    m = Maquina_cafe()
    m.pagamento()
    m.solta_cafe()
    m.troco()
    print(m)