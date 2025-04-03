class InfoArquivo:
    '''Classe inforações de arquivos'''

    def __init__(self, nome, tamanho):
        '''Inicialização dos dados'''
        self._nome = nome
        self._tamanho = tamanho
        self._formatos_suportados = ['txt','pdf','jpg','zip', 'mp4']


    def excede_tamanho(self):
        if self._tamanho >= 1000:
            return True
        else:
            return False

    def __str__(self):
        return f'Arquivo: {self._nome} ({self._tamanho} MB)'


class InfoImagem:
    '''Usada para definir uma imagem'''
    def __init__(self):


if __name__ == '__main__':
    pass