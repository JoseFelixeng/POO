import math
from abc import ABC, abstractmethod


class Poligono:
    """
    Classe Base Abstrata utilizada para representar um polígono qualquer.

    Um polígono é representado pelas coordenadas do seu centro
    e pelos comprimentos dos seus lados.

    Esta classe não deve ser instanciada.
    """

    def __init__(self, centro, lados):
        """
        Inicializa um polígono dadas as coordenadas do seu centro e os seus lados.

        Parameters
        ----------
        centro : tuple
            Tupla de 2 números reais contendo as coordenadas do centro do polígono.
        lados : tuple
            Tupla de tamanho n > 2 contendo os tamanhos dos lados de um polígono.

        """
        self.centro = centro
        self.lados = lados

    @property
    def num_lados(self):
        """
        int: número de lados do polígono.
        """
        return len(self.lados)

    @staticmethod
    def distancia(pol1, pol2):
        """
        Retorna a distância entre dois polígonos.

        Sendo P1 e P2 dois polígonos, a distância
        entre eles é dada por d(P1, P2) = sqrt(P1.x - P2.x)^2 + (P1.y - P2.y)^2,
        onde Pi.x e Pi.y são as coordenadas do centro do polígono Pi.

        Parameters
        ----------
        pol1
            O primeiro polígono.
        pol2
            O Segundo polígono.

        Returns
        -------
        float
            Distância Euclidiana entre os centros dos dois polígonos.

        """
        p1.x = pol1[0]
        p1.y = pol1[1]
        p2.x = pol2[0]
        p2.y = pol2[1]
        d = sqrt(p1.x - p2.x) ^ 2 + (p1.y - p2.y) ^ 2
        return d

    @abstractmethod
    def perimetro(self):
        """
        Retorna o perímetro do polígono.

        O perímetro de um polígono é dado pela soma de todos os seus
        lados.

        Returns
        -------
        float
            Perímetro do polígono.
        """
        n = self.lados
        pe = 0
        for i in range(n):
            pe += i

        return pe

    @abstractmethod
    def area(self):
        """
        Retorna a área do polígono.

        Este método abstrato deve ser implementado
        de acordo com cada subclasse.

        Returns
        -------
        float
            Área do polígono.
        """
        pass

    def lados_iguais(self):
        """
        Informa se o polígono possui lados iguais.

        Returns
        -------
        bool
            True se o polígono possuir todos os lados
            iguais, False caso contrário.
        """
        for i in self.lados:
            if self.lados[0] != i:
                return False
        return True

    @abstractmethod
    def __repr__(self):
        """
        Retorna uma representação do objeto em forma de str.

        Deve conter as coordenadas do centro do polígono
        no formato:
        " em (x,y)",
        onde x e y são as coordenadas do seu centro.

        Este método abstrato deve ser estendido
        em cada classe concreta.

        Returns
        -------
        str
            Representação do objeto em forma de str.
        """
        return f" em ({self.centro[0]},{self.centro[1]})"


class PoligonoRegular(Poligono):
    """
    Classe utilizada para representar um polígono regular.

    Um polígono regular é um polígono que possui todos os seus lados iguais.
    """

    def __init__(self, centro, lados):
        """
        Inicializa um polígono regular dadas as coordenadas do seu centro
        e os seus lados.

        Imprime mensagem de erro caso os lados informados não sejam todos iguais.

        Parameters
        ----------
        centro : tuple
            Tupla de 2 números reais contendo as coordenadas do centro do polígono.
        lados : tuple
            Tupla de tamanho n > 2 contendo os tamanhos dos lados de um polígono.

        """
        s = lados.iguais()
        if s == True:
            self.centro = centro
            self.lados = lados
        else:
            print("Lados informados não são iguais")

    def perimetro(self):
        """
        Retorna o perímetro do polígono.

        Reimplementa método da classe base:
        o perímetro é calculado como
        sendo o produto entre qualquer dos seus
        lados e o seu número de lados.

        Returns
        -------
        float
            Perímetro do polígono.
        """
        s = self.lados[0]
        n = num_lados(self.lados)

        p = s * n
        return p

    def area(self):
        """
        Retorna a área do polígono.

        Esta implementação calcula a área de um polígono regular
        utilizando a fórmula

        a =          n(s^2)
            -----------------------
                    4tan(PI/n)

        onde s é o tamanho do seu lado,
        n é o seu número de lados e o
        ângulo PI/n está em radianos.

        Notes
        -------
        Utilize a função math.tan que recebe a tangente de um ângulo
        em radianos. A constante PI pode ser usada como math.pi.

        Returns
        -------
        float
            Área do polígono.
        """

        s = num_lados()
        n = len(self.lados)
        a = n * (s ^ 2) / 4 * math.tan(math.pi / n)
        return a

    def __repr__(self):
        """
        Retorna uma representação do objeto em forma de str.

        Formato:

        "Poligono regular de n lados, lado igual a s",

        onde n é a quantidade de lados e s é o valor do lado.

        Returns
        -------
        str
            Representação do objeto em forma de str.
        """
        n = self.lados
        quant = 0
        for i in n:
            quant += 1

        return f"Poligono regular de {quant} lados, igual a {n} "


class Retangulo(Poligono):
    """
    Classe utilizada para representar um retângulo.

    Um retângulo é um polígono.
    """

    def __init__(self, centro, lados):
        """
        Inicializa um retângulo dadas as coordenadas do seu centro e
        uma tupla contendo a sua base e a sua altura.

        Parameters
        ----------
        centro : tuple
            Tupla de 2 números reais contendo as coordenadas do centro do polígono.
        lados : tuple
            Tupla de 2 números reais informando a base e altura do retângulo.

        """
        self.centro = centro
        self.lados = lados

    def perimetro(self):
        """
        Retorna o perímetro do retângulo.

        O perímetro de um retângulo é dado por 2 vezes a sua altura
        somada com 2 vezes a sua base.

        Returns
        -------
        float
            Perímetro do retângulo.
        """
        da = 2 * self.lados[1]
        db = 2 * self.lados[0]
        p = da + db
        return p

    def area(self):
        """
        Retorna a área do retângulo.

        A área de um retângulo é dada pela sua base multiplicada
        pela sua altura.

        Returns
        -------
        float
            Área do retângulo.
        """
        db = self.lados[0]
        da = self.lados[1]
        a = db * da

        return a

    def __repr__(self):
        """
        Retorna uma representação do objeto em forma de str.

        Formato:

        "Retângulo com base b e altura a",

        onde a base e altura são obtidos da tupla
        contendo os lados do polígono.

        Returns
        -------
        str
            Representação do objeto em forma de str.
        """
        db = self.lados[0]
        da = self.lados[1]
        return f"Retangulo com base{db} e altura {da} "


class TrianguloEquilatero(PoligonoRegular):
    """
    Classe utilizada para representar um triângulo equilátero.

    Um triângulo equilátero possui três lados iguais e portanto,
    é um polígono regular.
    """

    def __init__(self, centro, s):
        """
        Inicializa um triângulo equilátero dadas as coordenadas do seu centro e
        um único valor denotando o valor de todos os seus lados.

        Parameters
        ----------
        centro : tuple
            Tupla de 2 números reais contendo as coordenadas do centro do polígono.
        s : float
            Número real contendo o valor do lado do triângulo.

        """
        self.centro = centro
        self.lados = s

    def __repr__(self):
        """
        Retorna uma representação do objeto em forma de str.

        Formato:

        "Triangulo equilatero com lado igual a s",

        onde s é o valor do lado.

        Returns
        -------
        str
            Representação do objeto em forma de str.
        """
        s = self.lados
        c = self.centro
        return f"Triangulo equilatero com lados iguais a {s} em {c} "


class Quadrado(PoligonoRegular):
    """
    Classe utilizada para representar um quadrado.

    Um quadrado possui quatro lados iguais e portanto,
    é um polígono regular.
    """

    def __init__(self, centro, s):
        """
        Inicializa um quadrado dadas as coordenadas do seu centro e
        um único valor denotando o valor de todos os seus lados.

        Parameters
        ----------
        centro : tuple
            Tupla de 2 números reais contendo as coordenadas do centro do polígono.
        s : float
            Número real contendo o valor do lado do triângulo.

        """
        self.centro = centro
        self.lados = s

    def __repr__(self):
        """
        Retorna uma representação do objeto em forma de str.

        Formato:

        "Quadrado com lado igual a s",

        onde s é o valor do lado.

        Returns
        -------
        str
            Representação do objeto em forma de str.
        """
        s = self.lados
        return f"Quadrado com lados igual a {s}"


if __name__ == "__main__":
    r1 = Retangulo((-1.0, 1.0), (5.0, 10.0))
    print(r1)
    print(f">Perimetro: {r1.perimetro()}")
    print(f">Area: {r1.area()}")

    t1 = TrianguloEquilatero((5.0, 5.0), 2)
    print(t1)
    print(f">Perimetro: {t1.perimetro()}")
    print(f">Area: {t1.area()}")

    t2 = TrianguloEquilatero((0.0, -2.0), 3)
    print(t2)
    print(f">Perimetro: {t2.perimetro()}")
    print(f">Area: {t2.area()}")

    q1 = Quadrado((10.0, 10.0), 4)
    print(q1)
    print(f">Perimetro: {q1.perimetro()}")
    print(f">Area: {q1.area()}")

    p1 = PoligonoRegular((-10.0, -10.0), (7, 7, 7, 7, 7))  # inicializa um pentágono
    print(p1)
    print(f">Perimetro: {p1.perimetro()}")
    print(f">Area: {p1.area()}")
    print(f"Distancia entre o quadrado e o pentagono: {Poligono.distancia(q1, p1)}")

    p2 = PoligonoRegular(
        (2.0, 3.0), (7, 7, 6, 7, 7)
    )  # mensagem: lados informados não formam polígono regular
