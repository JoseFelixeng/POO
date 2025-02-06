# Aula 1 

# 1 Ex: Implemente um programa que, dados três valores inteiros, informe quantos deles são pares.

# Exercício 0 - Solução


class pares:
    '''Defini um par apartir de 3 valores'''

    def __init__(self, a, b, c):
        '''Inicialização da classe'''
        self.a = a
        self.b = b
        self.c = c
        self.soma = 0

    def contar_pares(self: int, a: int, b: int, c: int) -> int:
        soma = 0
        for num in (self.a, self.b, self.c):
            if num % 2 == 0:
                self.soma = self.soma + 1

        return self.soma

    def __str__(self):
        '''Saída da função pares '''
        return 'Quantos numeros são pares = {}'.format(self.soma)


if __name__ == "__main__":
    a = int(input('Informe o 1o. nr.: '))
    b = int(input('Informe o 2o. nr.: '))
    c = int(input('Informe o 3o. nr.: '))
    # Dica: ao invés de ler a entrada do usuário
    # com o comando 'input', vc pode atribuir
    # os valores das entradas diretamente no código
    # quando estiver testando o seu código.
    # Exemplo:
    # a = 5
    # b = 2
    # c = 3

    p = pares(a, b, c)
    p.contar_pares(a, b, c)

    print(p)