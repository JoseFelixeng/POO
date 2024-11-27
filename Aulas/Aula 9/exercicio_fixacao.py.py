import random


class Produto:
    """Produtos"""

    def __init__(self, preco):
        self.codigo = random.randint(1, 999)
        self.preco = preco
        self.d_a = False

    def preco_com_desconto(self, per):
        if self.d_a:
            return self.preco - (self.preco * (per / 100))
        else:
            return self.preco

    def ativa_desconto(self):
        self.d_a = True

    def __str__(self):
        s = f"cod: {self.codigo} - R$ {self.preco}\n"
        return s


class Jogo(Produto):
    """Produto Game"""

    def __init__(self, nome, plataforma, preco):
        Produto.__init__(self, preco)
        self._nome = nome
        self._plataforma = plataforma

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_n):
        self._nome = novo_n

    @property
    def plataforma(self):
        return self._plataforma

    @plataforma.setter
    def plataforma(self, novo_p):
        self._plataforma = novo_p

    def __str__(self):
        pdc = self.preco_com_desconto(18)
        s = Produto.__str__(self)
        s += f"Preço com desconto R$ {pdc}"
        return f"Livro: {self._nome} - Autor: {self._plataforma}  {s}"


class Livro(Produto):
    """Produto Livro"""

    def __init__(self, titulo, autor, preco):
        Produto.__init__(self, preco)
        self._titulo = titulo
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_t):
        self._titulo = novo_t

    def __str__(self):
        pdc = self.preco_com_desconto(30)
        s = Produto.__str__(self)
        s += f"Preço com desconto R$ {pdc}"
        return f"Livro: {self._titulo} - Autor: {self._autor}  {s}"


if __name__ == "__main__":
    l1 = Livro("O homem duplicado", "Jose Saramago", 30.00)
    l2 = Livro("O idiota", "Fiodor Dostoievski", 35.00)
    l2.ativa_desconto()
    print(l1)
    print(l2)

    l3 = Livro("Revolução dos bichos", "George Orwell", 35.00)
    print(l3)
    j1 = Jogo("Street Fighter V", "PS4", 200.00)
    j2 = Jogo("Call of Duty: Black Ops Cold War", "PS4", 250.00)
    j2.ativa_desconto()
    print(j1)
    print(j2)
    j3 = Jogo("Call of Duty: Black Ops Cold War", "Xbox One", 250.00)
    j3.ativa_desconto()
    print(j3)
    j4 = Jogo("Forza Horizon 4", "Xbox One", 200.00)
    j5 = Jogo("Zelda: Breath of the Wild", "Switch", 300.00)
    j5.ativa_desconto()
    print(j4)
    print(j5)
    # Produto.imprime_instancias()
