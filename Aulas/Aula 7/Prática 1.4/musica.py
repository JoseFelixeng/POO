class Musica:
    '''Usado para inserir musica'''
    
    def __init__(self, artista, titulo):
        self.__artista = artista
        self.__titulo = titulo
        

    @property
    def artista(self):
        '''Retorna o artista'''
        return self._artista
    
    @artista.setter
    def artista(self, novo):
        self.__artista = novo

    @property
    def musica(self):
        '''retorna o titulo'''
        return self._titulo
    
    @artista.setter
    def musica(self, novo):
        self.__titulo = novo
        
    def __str__(self):
        return f'{self.__artista} - {self.__titulo} '

