class PreProcessador:
    '''Classe Faz o pre Processamento de textos'''

    def __init__(self, texto):
        self._texto = texto
        self._lista_palavras = []

    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, texto_n):
        self._texto = texto_n

    @property
    def lista_palavras(self):
        return self._lista_palavras

    @lista_palavras.setter
    def lp(self, lp_n):
        self._lista_palavras = lp_n

    def processa(self):
        '''Classe usada para processar texto'''
        self._texto = self._texto.lower()
        self._texto = self._texto.split()
        self._lista_palavras = self._texto

    def __str__(self):
        p = self._lista_palavras
        s = ''
        for i in p:
            s += i
            s += ' '
        return f'{s}'


class ContadorPalavras(PreProcessador):
    '''Classe faz a contagem de Palavras'''

    def __init__(self, texto):
        PreProcessador.__init__(self, texto)
        self._ocorrencias = dict()

    @property
    def ocorrencias(self):
        return self._ocorrencias

    @ocorrencias.setter
    def ocorrencias(self, oc_n):
        self._ocorrencias = oc_n

    def processa(self):
        d = dict()
        self._texto = self._texto.strip()
        self._texto = self._texto.lower()
        w = self._texto.split()
        for i in w:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        self._ocorrencias = d
        for key in list(self._ocorrencias.keys()):
            print(key, ":", self._ocorrencias[key])


class Tradutor(PreProcessador):
    '''Classe faz a tradução de um texto'''

    def __init__(self, texto):
        PreProcessador.__init__(self, texto)
        self.tradutor = {'ola': 'hello', 'olá!': 'hello', 'este': 'this', 'este!': 'this', 'este,': 'this', 'é': 'is', 'um': 'a', 'exemplo': 'example', 'de': 'of',
                         'texto': 'text', 'com': 'with', 'termos': 'terms', 'repetidos.': 'repeated', 'repetidos:': 'repeated', 'repetidos': 'repeated', 'possui': 'has', 'vários': 'various'}
        self._lista_palavras_trad = []

    @property
    def lp(self):
        return self._lista_palavras_trad

    @lp.setter
    def ocorrencias(self, lp_n):
        self._lista_palavras_trad = oc_n

    def processa(self):

        self._texto = self._texto.strip()
        self._texto = self._texto.lower()
        w = self._texto.split()
        for i in w:
            if i in list(self.tradutor.keys()):
                l = self.tradutor[i]
            self._lista_palavras_trad[0] = l
            print(self._lista_palavras_trad)


class ProcessadorTexto(ContadorPalavras, Tradutor):
    '''Classe Faz o Processamento de texto'''

    def __init__(self, texto):
        ContadorPalavras.__init__(self, texto)

    def Processa(self):
        pass


if __name__ == '__main__':
    # testar as classes do Programa
    p = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
                       ' Este texto possui vários termos repetidos:'
                       ' este, Este, ESte, esTE!')
    p.processa()
    print(p)
    c = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
                         ' Este texto possui vários termos repetidos:'
                         ' este, Este, ESte, esTE!')
    c.processa()
    print(c)

    t = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
                 ' Este texto possui vários termos repetidos:'
                 ' este Este ESte esTE')
    t.processa()
    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    processadortexto.processa()
