'''
Interfaces Gráficas com Python e TK.

Lista de Filmes em TK
(Versão com MVC).

Módulo "Controller"
'''

from lista_filmes_model import Filme, ListaFilmes
from lista_filmes_view import ListaFilmesGUI
import tkinter as tk

class ListaFilmesController:

    def __init__(self, model, view):

        self._model = model
        self._view = view
        self._configura_eventos()

    def _configura_eventos(self):
        self._view.botoes['adiciona']['command'] = self._insere_filme
        self._view.botoes['atualiza']['command'] = self._atualiza_filme
        self._view.botoes['remove']['command'] = self._remove_filme

    def _insere_filme(self):
        tit, ano, nota = self._view.obtem_dados_filme()
        f = Filme(tit, ano, nota)

        self._model.insere_filme(f) # Insere novo filme no Model (que é um ListaFilmes)

        self._view.atualiza_listbox(self._model.converte_para_lista()) # Reflete inserção na View

    def _atualiza_filme(self):
        tit, ano, nota = self._view.obtem_dados_filme()
        f = Filme(tit, ano, nota) # Constroi novo filme

        idx = self._view.obtem_item_selecionado()
        if idx:
            self._model.atualiza_filme(idx, f) # Substitui no Model o filme da lista lá armazenada pelo novo filme

            self._view.atualiza_listbox(self._model.converte_para_lista()) # Reflete substituição na View

    def _remove_filme(self):
        idx = self._view.obtem_item_selecionado()
        self._model.remove_filme(idx) # Remove no Model o filme indicado pela posição

        self._view.atualiza_listbox(self._model.converte_para_lista()) # Reflete remoção na View

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Lista de Filmes')

    model = ListaFilmes()
    view = ListaFilmesGUI(root)
    controller = ListaFilmesController(model, view)

    root.mainloop()

