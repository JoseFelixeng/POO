class PreProcessador:

    def __init__(self, texto):
        self._texto = texto
        self._lista_palavras = list()

    def processa(self):
        print('preprocess')
        palavras_brutas = self._texto.split()
        for palavra in palavras_brutas:
            palavra = palavra.lower()
            if not palavra[-1].isalpha():
                palavra = palavra.strip(palavra[-1])
            self._lista_palavras.append(palavra)

    def __str__(self):
        return str(self._lista_palavras)

class ContadorPalavras(PreProcessador):

    def __init__(self, texto):
        super().__init__(texto)
        self._ocorrencias = dict()

    def processa(self):
        print('contador')
        super().processa()
        for palavra in self._lista_palavras:
            palavra = palavra.lower()
            if palavra not in self._ocorrencias.keys():
                self._ocorrencias[palavra] = 0
            self._ocorrencias[palavra] += 1

    def __str__(self):
        s = 'Frequencia das palavras:\n'
        for pal, ocorr in self._ocorrencias.items():
            s += f'{pal}: {ocorr} vezes\n'
        return s

class Tradutor(PreProcessador):

    def __init__(self, texto):
        super().__init__(texto)
        self._traducoes = dict()
        self._lista_palavras_trad = list()

        self._traducoes['olá'] = 'hello'
        self._traducoes['este'] = 'this'
        self._traducoes['é'] = 'is'
        self._traducoes['um'] = 'a'
        self._traducoes['exemplo'] = 'example'
        self._traducoes['de'] = 'of'
        self._traducoes['texto'] = 'text'
        self._traducoes['com'] = 'with'
        self._traducoes['termos'] = 'terms'
        self._traducoes['repetidos'] = 'repeated'
        self._traducoes['possui'] = 'has'
        self._traducoes['vários'] = 'various'

    def processa(self):
        print('tradutor')
        super().processa()
        for palavra in self._lista_palavras:
            self._lista_palavras_trad.append(self._traducoes[palavra])
        print(ContadorPalavras.__str__(self))

    def __str__(self):
        return str(self._lista_palavras_trad)

class ProcessadorTexto(Tradutor, ContadorPalavras):
    
    def __init__(self, texto):
        super().__init__(texto)

    def processa(self):
        super().processa()

        print('Tradução robótica:')
        print(' '.join(self._lista_palavras_trad))


if __name__ == '__main__':
    # Descomente a seguir para testar apenas a classe PreProcessador
    # preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
    #                                 ' Este texto possui vários termos repetidos:'
    #                                 ' este, Este, ESte, esTE!')
    # preprocessador.processa()
    # print(preprocessador)
    
    # Descomente a seguir para testar apenas a classe ContadorPalavras
    # contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
    #                             ' Este texto possui vários termos repetidos:'
    #                             ' este, Este, ESte, esTE!')
    # contador.processa()
    # print(contador)

    # Descomente a seguir para testar apenas a classe Tradutor
    # tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
    #                     ' Este texto possui vários termos repetidos:'
    #                     ' este, Este, ESte, esTE!')
    # tradutor.processa()
    # print(tradutor)

    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    processadortexto.processa()