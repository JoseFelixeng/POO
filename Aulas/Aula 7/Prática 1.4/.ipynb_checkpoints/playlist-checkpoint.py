from musica import Musica
import random

class Playlist:
    '''Usado para criação e edição de playlist'''
    
    def __init__(self, musicas):
        self.__musicas = musicas
          
    def imprime(self):
        print('------------------------------------------')
        for i , mm in enumerate(self.__musicas):
            print(f'{mm}')
        print('-------------------------------------------')
    
    def adiciona(self, nova_m):
        if not nova_m in self.__musicas:
            self.__musicas.append(nova_m)
            
    def toca_proxima(self):
       r = self.__musicas.pop(0)
       print(f'Tocando agora: {r}')

    def embaralha(self):
        em = self.__musicas
        random.shuffle(em)
        return f'{em}'




