'''
Interfaces Gráficas com Python e TK.

Lista de Filmes em TK
(Versão com MVC).

Módulo "View"
'''

import tkinter as tk

class ListaFilmesGUI:

    def __init__(self, root):

        self.botoes = {} # Público: acessível pelo Controlador para configurar os eventos
        self._lb = None # Listbox será privada
        self._master = root # Widget Tk que é o mestre desta GUI

        self._inicializa_vars()
        self._inicializa_gui()
    
    @staticmethod
    def _inicializa_vars():
        _v_tit = tk.StringVar()
        _v_ano = tk.StringVar()
        _v_nota = tk.StringVar(value='0.0')
        _v_filmes = tk.StringVar()

    def _inicializa_gui(self):
        frame_esq = tk.Frame(self._master, bd=10, relief=tk.SUNKEN)
        frame_esq.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        frame_dir = tk.Frame(self._master, bd=10, relief=tk.SUNKEN)
        frame_dir.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)

        self._lb = tk.Listbox(frame_dir, height=30, width=40, listvariable=self._v_filmes)
        self._lb.pack(side=tk.TOP)

        l_tit = tk.Label(frame_esq, text='Título:')
        l_tit.grid(row = 0, column = 0)
        e_tit = tk.Entry(frame_esq, width=30, textvariable=self._v_tit)
        e_tit.grid(row = 0, column = 1, columnspan=3, sticky='W')

        l_ano = tk.Label(frame_esq, text='Ano:')
        l_ano.grid(row = 1, column = 0, sticky='W')
        e_ano = tk.Entry(frame_esq, width=8, textvariable=self._v_ano)
        e_ano.grid(row = 1, column = 1, sticky='W')

        l_nota = tk.Label(frame_esq, text='Nota:')
        l_nota.grid(row = 1, column = 2, sticky='E')
        e_nota = tk.Entry(frame_esq, width=8, textvariable=self._v_nota)
        e_nota.grid(row = 1, column = 3, sticky='W')

        self.botoes['adiciona'] = tk.Button(frame_esq, text='Insere')
        self.botoes['adiciona'].grid(row = 2, column = 1, sticky='W')

        self.botoes['atualiza'] = tk.Button(frame_esq, text='Atualiza')
        self.botoes['atualiza'].grid(row = 2, column = 2, sticky='W')

        self.botoes['remove'] = tk.Button(frame_esq, text='Remove')
        self.botoes['remove'].grid(row = 2, column = 3, sticky='W')

    def atualiza_listbox(self, lista_strings):
        '''
        Interface pública da classe:
        deve ser chamada pelo Controller.
        Atribui a lista de strings do parâmetro
        à Listbox.
        '''
        self._v_filmes.set(lista_strings)

    def obtem_dados_filme(self):
        '''
        Interface pública da classe:
        deve ser chamada pelo Controller.
        Retorna os dados presentes nas
        Entry do título, ano e nota.
        Formato: uma tupla com três strings
        '''
        return(self._v_tit.get(), self._v_ano.get(), self._v_nota.get())

    def obtem_item_selecionado(self):
        '''
        Interface pública da classe:
        deve ser chamada pelo Controller.
        Retorna a posição da lista (inteiro)
        que está selecionada no Listbox.
        '''

        selecao = self._lb.curselection()
        if selecao:
            return selecao[0]
        else:
            return None

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Lista de Filmes')

    gui = ListaFilmesGUI(root)
    gui.atualiza_listbox(['um', 'dois', 'tres']) # Observe: LISTA DE STRINGS

    root.mainloop()