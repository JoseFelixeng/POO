class InfoArquivo:
    '''Classe De informação'''

    def __init__(self, nome, tamanho):
        self._nome = nome
        self._tamanho = tamanho
        self._formatos_suportados = ['txt', 'pdf', 'jpg', 'zip', 'mp4']
        self.ex = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_n):
        self._nome = novo_n

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, n):
        self._tamanho = n

    def excede_tamanho(self):
        if self._tamanho >= 1000:
            self.ex = True
        else:
            self.ex = False
        return self.ex

    def imprime_metodos_suportados(self):
        print('------------------------------------------')
        print('Formatos Suportados: ')
        for i, mm in enumerate(self._formatos_suportados):
            print(f'{mm}')
        print('-------------------------------------------')

    def __str__(self):
        return f'Arquivo: {self._nome} ({self._tamanho} MB) '


class InfoImagem(InfoArquivo):
    '''Arquivo Imagem'''

    def __init__(self, nome, tamanho, resolucao):
        InfoArquivo.__init__(self, nome, tamanho)
        self._resolucao = resolucao

    @property
    def resolucao(self):
        return self._resolucao

    @resolucao.setter
    def resolucao(self, n):
        self._resolucao = n

    def redimensiona(self):
        d1 = self._resolucao[0]/2
        d2 = self._resolucao[1]/2
        d3 = [d1, d2]
        self._resolucao = d3

    def __str__(self):
        return f'Imagem: {self._nome}, resolucao: {self._resolucao}  ({self._tamanho} MB)'


class InfoVideo(InfoImagem):
    '''classe de Video'''

    def __init__(self, nome, tamanho, resolucao, duracao):
        InfoImagem.__init__(self, nome, tamanho, resolucao)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, n):
        self._duracao = n

    def excede_tamanho(self):
        if self._tamanho >= 1000 or self._resolucao[0] > 3840:
            self.ex = True
        else:
            self.ex = False
        return self.ex

    def redimensiona(self):
        d1 = self._resolucao[0]/2
        d2 = self._resolucao[1]/2
        d3 = [d1, d2]
        self._resolucao = d3

    def __str__(self):
        return f'Video: {self._nome}, resolução: {self._resolucao}, duracao: {self._duracao} ({self._tamanho} MB)'


if __name__ == '__main__':
    a1 = InfoArquivo('anotacoes.txt', 0.01)
    a2 = InfoArquivo('nota_fiscal.pdf', 2.0)
    a3 = InfoArquivo('arquivo.zip', 1500)
    i1 = InfoImagem('foto1.jpg', 3.0, [3000, 2000])
    i2 = InfoImagem('foto2.jpg', 3.0, [3000, 2000])
    v1 = InfoVideo('video1.mp4', 50.0, [1920, 1080], 3602)
    v2 = InfoVideo('video2.mp4', 20.0, [3840, 2060], 300)
    v3 = InfoVideo('video3.mp4', 65.0, [7680, 4320], 20)

    a1.imprime_metodos_suportados()

    diretorio = [a1, a2, a3, i1, i2, v1, v2, v3]

    print('\n>>>>>>>>>>>>>>>>>>>>>')
    print('Antes do redimensionamento:')
    for a in diretorio:
        print(a)  # chama o __str__ de acordo com a classe
        print(a.excede_tamanho())

    diretorio.remove(a3)
    i2.redimensiona()
    v3.redimensiona()

    print('\n>>>>>>>>>>>>>>>>>>>>>')
    print('Depois do redimensionamento:')
    for a in diretorio:
        print(a)
        print(a.excede_tamanho())
