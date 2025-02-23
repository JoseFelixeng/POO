class Musica:
    '''Usada para criar uma musica'''

    def __init__(self, artista: str, musica: str):
        self._musica = musica
        self._artista = artista

    @property
    def musica(self):
        '''Retorna a musica'''
        return  self._musica

    @property
    def artista(self):
        '''Retorna o artista'''
        return self._artista

    def __str__(self):
        '''Retorna Artista - Musica'''
        return f'{self._artista} - {self._musica}'


