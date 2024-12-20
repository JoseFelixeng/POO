
import tkinter as tk


class Filme:
    '''Instância por Filmes'''

    def __init__(self, titulo='', ano=0, nota=0.0):
        self._titulo = titulo
        self._ano = ano
        self._nota = nota

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, n_titulo):
        self._titulo = n_titulo

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, n_ano):
        self._ano = n_ano

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, n_nota):
        self._nota = n_nota

    def __repr__(self):
        '''Metodo usado para saida de Filme'''
        return f'{self.titulo} {self.ano} {self.nota}'


class Locadora:
    '''Guardar vários Filmes'''

    def __init__(self):
        self._filmes = []

    def cadastra(self, filme):
        if filme in self._filmes:
            print('Filme já cadastrado')
        elif type(filme) == Filme:
            self._filmes.append(filme)
            print(f'Filme cadastrado: {self._filmes}')

    def atualiza(self, filme):
        for f in self._filmes:
            if filme.titulo in f.titulo:
                filme.titulo = input('Insira novo Titulo: ')
                filme.ano = int(input('Atualize o ano: '))
                filme.nota = float(input('Atualize a nota: '))
                break
            else:
                print('Filme Não encontrado')

    def remove(self, filme):
        for l in self._filmes:
            if l.titulo == filme.titulo:
                self._filmes.remove(filme)
                break
        else:
            print('Titulo não encontrado')

    def __str__(self):
        s = ''
        for i in (self._filmes):
            s += f'{i}'
            s += '\n'
        return s

# Criando a Interface para Cadastrar os Filmes:


class LocadoraView:
    '''Interface gráfica da Calculadora: '''
    _filmes = []

    def __init__(self, root):
        self.root = root
        self.botoes_fun = {}
        self._inicializa_gui()

    def _inicializa_gui(self):
        # Interface de Cadastramento
        f1 = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        f1.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        self.titu = tk.Label(f1, text='Titulo: ')
        self.titu['font'] = ('Arial', 14)
        self.titu.grid(row=0, column=0, sticky="NSWE")
        self.e_titulo = tk.Entry(f1)
        self.e_titulo['font'] = ('Helvetica', 10)
        self.e_titulo.grid(row=0, column=1, columnspan=3, sticky="NSWE")

        self.ano = tk.Label(f1, text='Ano: ')
        self.ano['font'] = ('Arial', 14)
        self.ano.grid(row=1, column=0, sticky="NSWE")
        self.e_ano = tk.Entry(f1)
        self.e_ano['font'] = ('Helvetica', 10)
        self.e_ano.grid(row=1, column=1, sticky="NSWE")

        self.nota = tk.Label(f1, text='Nota: ')
        self.nota['font'] = ('Arial', 14)
        self.nota.grid(row=1, column=2, sticky="NSWE")
        self.e_nota = tk.Entry(f1)
        self.e_nota['font'] = ('Helvetica', 10)
        self.e_nota.grid(row=1, column=3, sticky="NSWE")
        self.e_nota.insert(0, '0.0')

        self.botoes_fun['Inseri'] = tk.Button(f1, text="Inserir")
        self.botoes_fun['Inseri']['font'] = ('Arial', 14)
        self.botoes_fun['Inseri']['bg'] = 'green'
        self.botoes_fun['Inseri'].grid(row=3, column=1, sticky="NSWE")
        self.botoes_fun['Atualiza'] = tk.Button(f1, text="Atualizar")
        self.botoes_fun['Atualiza']['font'] = ('Arial', 14)
        self.botoes_fun['Atualiza']['bg'] = 'yellow'
        self.botoes_fun['Atualiza'].grid(row=3, column=2, sticky="NSWE")
        self.botoes_fun['Remove'] = tk.Button(f1, text="Remover")
        self.botoes_fun['Remove']['font'] = ('Arial', 14)
        self.botoes_fun['Remove']['bg'] = 'red'
        self.botoes_fun['Remove'].grid(row=3, column=3, sticky="NSWE")

        # configura linhas e colunas quanto ao redimensionamento
        f1.rowconfigure(0, weight=0)
        f1.rowconfigure(1, weight=0)
        f1.rowconfigure(1, weight=0)
        f1.rowconfigure(3, weight=0)
        f1.columnconfigure(0, weight=0)
        f1.columnconfigure(1, weight=0)
        f1.columnconfigure(1, weight=0)
        f1.columnconfigure(3, weight=0)

        f2 = tk.Frame(self.root, bd=4, relief=tk.SUNKEN)
        f2.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)

        self.f_titu = tk.Label(
            f2, text='LOCADORA FILMES', bg='blue', fg='white')
        self.f_titu['font'] = ('Agency FB', 20)
        self.f_titu.pack(side=tk.TOP)

        f_lista_itens = tk.StringVar()
        f_lista_itens.set(LocadoraView._filmes)
        lf = tk.Listbox(f2, listvariable=f_lista_itens)
        lf.pack(expand=True, fill=tk.BOTH)

    def processa_i(self, lista):
        print(type(lista))
        f = str(lista)
        LocadoraView._filmes.append(f)
        print('f')
        print(f)
        print(f'Filmes=> {LocadoraView._filmes}')


class LocadoraController:
    '''Usada para intermedia a classe Biblioteca com a interface gráfica'''

    def __init__(self):
        self.model = None
        self.view = None

        self.root = tk.Tk()
        self.root.geometry('600x400+300+10')
        self.root.title('Aplicativo Locadora de Filmes')

        self.var_titulo = tk.StringVar()
        self.var_ano = tk.StringVar()
        self.var_nota = tk.StringVar()

    def inicializa(self, model, view):
        '''faz a comunicação ente o modelo e o view: '''
        self.model = model
        self.view = view
        self._configura()

    def _configura(self):
        '''Configurações dos botões'''
        self.view.e_titulo['textvariable'] = self.var_titulo
        self.view.e_ano['textvariable'] = self.var_ano
        self.view.e_nota['textvariable'] = self.var_nota

        self.view.botoes_fun['Inseri']['command'] = lambda: self.inseri()
        self.view.botoes_fun['Atualiza']['command'] = lambda: self.atualiza()
        self.view.botoes_fun['Remove']['command'] = lambda: self.remove()

    def executa(self):
        '''Executa metodo de loop'''
        tk.mainloop()
        print('Fechando Locadora...')

    def inseri(self):
        f = Filme()
        f.titulo = str(self.var_titulo.get())
        f.ano = str(self.var_ano.get())
        f.nota = str(self.var_nota.get())
        self.model.cadastra(f)
        f = []
        f = self.model._filmes
        LocadoraView.processa_i(self, f)

    def atualiza(self):
        f = Local
        for i in self.model._filmes:
            if tup.titulo in f.titulo:
                tup.titulo = self.var_titulo.get()
                tup.ano = self.var_ano.get()
                tup.nota = self.var_nota.get()
                break
            else:
                print('Filme Não encontrado')

    def remove(self):
        tup = self.view.lf.curselection()
        f = top[0]
        print(f)
        s = self.view.f_lista_itens.remove(f)
        print(f'Item: {s}')


if __name__ == "__main__":

    # cria controller
    controller = LocadoraController()

    # cria modelo
    model = Locadora()

    # cria view
    view = LocadoraView(controller.root)

    # chama os métodos necessários do controller
    # para inicar a aplicação
    controller.inicializa(model, view)
    controller.executa()
