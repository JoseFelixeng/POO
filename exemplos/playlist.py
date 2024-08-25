import random

class Playlist:
    def __init__(self, musicas):
        self._musicas = musicas

    def imprime(self):
        print('----------------')
        for m in self._musicas:
            print(m)
        print('----------------')

    def adiciona(self, musica):
        self._musicas.append(musica)

    def toca_proxima(self):
        m = self._musicas.pop(0)
        print(f'Tocando agora: {m}')

    def embaralha(self):
        random.shuffle(self._musicas)