class FilaPacientes:
    '''Usado para organizar a fila dos Pacientes'''
    def __init__(self):
        '''Definindo as operações da classe'''
        self.__fila = []
        self.__pos = 0


    def adiciona_consulta(self):
            self.__fila.append(f'C{self.__pos}')
            self.__pos += 1
            #print(f'# DEBUG: Consulta C{self.__pos} adicionada à fila')

    @property
    def consulta(self):
        return self.__fila


    def adiciona_exame(self):
        self.__fila.append(f'E{self.__pos}')
        self.__pos += 1
        #print(f' # DEBUG: Exame E{self.__pos} adicionada à fila')

    def imprime(self):
        if len(self.__fila) != 0:
            for i in range(len(self.__fila)):
                if self.__fila[i] == f'C{i}':
                    print(f'Consulta {self.__fila[i]}')
                elif self.__fila[i] == f'E{i}':
                    print(f'Exame {self.__fila[i]}')
        else:
            print('Fila Vazia')


    def tamanho(self):
        return len(self.__fila)

    def chama_proximo(self):
        if self.__pos > 0:
            print(f'Chamando próxima senha: {self.__fila[0]}')
            self.__fila.pop(0)
            self.__pos -= 1
        elif self.__pos == 0:
            print('Erro: Fila Vazia')






if __name__ == '__main__':
    f = FilaPacientes()

    f.adiciona_consulta()
    f.adiciona_consulta()
    f.adiciona_exame()
    f.adiciona_consulta()
    f.adiciona_exame()
    f.adiciona_consulta()

    print('# DEBUG: Fila no 1o momento')
    f.imprime()
    print(f'Tamanho da fila: {f.tamanho()}')

    f.chama_proximo()
    f.chama_proximo()
    f.chama_proximo()

    f.adiciona_exame()
    f.adiciona_exame()
    f.adiciona_consulta()

    print('# DEBUG: Fila no 2o momento')
    f.imprime()
    print(f'Tamanho da fila: {f.tamanho()}')
