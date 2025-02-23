import random

class Playlist:
    '''Cria uma playlist de musicas'''

    def __init__(self, musicas):
        '''criar uma playlist de musicas'''
        self._musicas = musicas


    @property
    def musicas(self):
        return self._musicas

    def adiciona(self, musica):
        '''adiciona uma musica a playlist'''
        self._musicas.append(musica)

    def toca_proxima(self):
        print(f'tocando agora: {self._musicas[0]}')
        self._musicas.pop(0)

    def embaralha(self):
        return random.shuffle(self._musicas)

    def imprime(self):
        s = '------------------------------- \n'
        for i in self._musicas:
            s +=  str(i) + '\n'
        print(s + '-------------------------------')



