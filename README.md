# Apostila 
Esse material será usado no estudo da linguagem python.


# Aula 1 - Python Básico

Neste documento serão apresentados comandos básicos em Python.

## 1. Terminal Python

O terminal Python pode ser utilizado como uma calculadora interativa,
imprimindo o resultado para cada comando. Por exemplo:

```jsx
3 * 40
x = 2
y = 3
x + y #isto é um comentário em Python
```

## 2. Declaração de Variáveis

Variáveis em Python assumem um tipo de acordo com o valor atribuído.
Utilize a função da biblioteca `type` para saber o tipo de uma variável.

```jsx
x = 5 #declara um inteiro (int)
y = 3.1415 #declara um real (float)
flag = True #declara um booleano (bool), que também pode assumir valor False
carac = 'a' #declara uma string (str)
palavra1 = 'aula de poo' #Python não difere entre char e str; tanto faz utilizar aspas simples ou duplas
palavra2 = "outra string"
palavra3 = '''terceira string''' #também aceito desta forma
type(flag)
```

### Conversão entre tipos

Utilize as funções com o nome do tipo correspondente para converter variáveis de um tipo em um outro

```python
s = '50' #string
x = int(s) #converte string s para int e atribui resultado a x
type(x)

a = 10 #a é int
b = 1.333 #b é float
c = a + b #qual o tipo de c?
type(c)

```

Em Python, existe a conversão implícita (assim como em C++)

# 3. Operadores

### Operadores aritméticos

- Adição: `+`
- Subtração: ``
- Multiplicação: ``
- Divisão: `/`
- Divisão inteira: `//` (divide e aplica a função `floor` no resultado)
- Resto da divisão: `%`
- Exponenciação: `*`
- Radiciação: função `sqrt` (é preciso importar o módulo `math`)
- Atribuição e operação: `+=, -=,`  etc.

Em comparação com C/C++:

- Existe o operador de divisão inteira
- O operador de resto funciona com `float`
- Existe um operador para potência ao invés de uma função
- Não existe o operador de incremento/decremento

```python
a = 5
b = 2
a + b
a - b
a/b
a//b
a**b
```

### Operadores relacionais

- Igual: `==`
- Diferente: `!=`
- Maior: `>`
- Maior ou igual: `>=`
- Menor: `<`
- Menor ou igual: `<=`

Em comparação com C++, expressões como `1 < 2 < 3 < 4` funcionam em Python

```python
1 < 2 < 3
```

### Operadores lógicos

- Negação: `not`
- E (conjunção): `and`
- Ou (disjunção): `or`

Interpretado como valor falso:

- `False`, `0`, `None`, `""` (string vazia) e sequências vazias

Interpretado como valor verdadeiro:

- Todo o resto

### Precedência de operadores

1. Operadores aritméticos
2. Operadores relacionais
3. Operadores lógicos

Na dúvida, utilize parênteses `()` para construir expressões

## 4. Comandos de Entrada e Saída

### Saída: `print`

```python
nome = 'joao'
idade = 20
print(nome) # imprime o valor da variável passada como parâmetro
print(idade) # observe que um '\n' é acrescentado ao final automaticamente
```

### Saída Formatada

```python
Saída formatada:

- Estilo `printf` da linguagem C: `print("x eh %i, y eh %i" % (x, y))`
- Estilo Python: `print("x e {0}, y e {1}".format(x, y))`
- Estilo Python "f-string" (a partir de Python 3.6): `print(f'x e {x}')`
```

```python
x = 5
y = 6
print("x é {0}, y é {1}".format(x, y)) # os números entre chaves denotam índices dos parâmetros (0 é o primeiro parâmetro do format, 1 é o segundo, etc.)
print("y é {1}, x é {0}".format(x, y))
print("x é {}, y é {}".format(x, y)) # caso os números sejam omitidos, os parâmetros são tomados na ordem
print(f"x é {x}, y é {y}")
```

### Entrada: `input`

O comando `input` é utilizado para ler dados do teclado. Observe que o comando sempre retorna o dado lido como uma string. Portanto, é necessário converter a string no tipo de dado necessário.

```python
nome = input('Insira o nome do usuário: ') # nome será do tipo str
idade = int(input('Insira a idade do usuário: ')) # idade será do tipo int, por causa da conversãor
```

## 5. Controle de Fluxo em Python

### Código indentado é obrigatório

- Em Python, não há `{` e `}` como em C++ para delimitar blocos
- Blocos são delimitados pelos espaços em branco
- Começar novo bloco: adicionar quatro espaços em branco
- Finalizar bloco: remover quatro espaços em branco
- Dica: configurar editor de texto para trocar tabulação por quatro espaços
- Isto é necessário para os comandos de controle de fluxo, mostrados a seguir

```python
### Comando condicional ```if```

Sintaxe:

```
if condicao: #observe o : (dois pontos)
	bloco de comandos
```

- ```else:``` é opcional
- Não existe ```else if``` e sim ```elif```
```

```python
x = 5
if 0 < x < 10:
    print('x está entre 0 e 10')
elif 10 < x < 20:
    print('x está entre 10 e 20')
else:
    print('x possui outro valor')
```

```python
### Comando de repetição ```while```

Sintaxe:

```
while condicao:
    bloco de comandos
```

```else:``` é opcional, executado quando a condição é/se torna falsa (não é executado se for utilizado um ```break```
```

```python
x = 5
while x > 0:
    print('valor de x: {}'.format(x))
    x = x - 1
else:
    print('fim do laço')
```

```python
### Comando de repetição ```for```

Sintaxe:

```
for variavel in range(inicio, fim): #itera no intervalo [inicio,fim[ com incremento igual a 1
    bloco de comandos
```

ou

```
for variavel in range(inicio, fim, inc): #itera no intervalo [inicio,fim[ com incremento igual a inc
    bloco de comandos
```

```else:``` é opcional, funciona de forma idêntica ao ```while```
```

Formas de uso do for:

```python
for i in range(0, 5):
    print('i = {}'.format(i))
else:
    print('chegou em {}'.format(i))
```

```python
for x in range(-5, 7, 2):
    print(x)
```

### Comandos `break` e `continue`

- `break`: encerra o laço (o `else` associado ao laço não é executado)
- `continue`: força a próxima iteração do laço

## 6. Funções em Python

Para definir uma função em Python, basta utilizar a palavra chave `def` junto com a seguinte sintaxe:

```
def nome_funcao(lista de parametros):
    corpo da funcao

```

- Uma função pode ter `return` ou não
- A lista de parâmetros é composta de variáveis separadas por vírgulas (sem especificação de tipo)

```python
def converte_temp(tf):
    '''
    Converte temperatura
    Farenheint em Celsius.
    '''
    
    return (tf - 32)/1.8
```

```python
help(converte_temp) #imprime a documentação da função
print(converte_temp(98.6)) #chama a função e imprime o seu resultado
```

## Arquivos .py

- O terminal interativo Python é útil, mas se torna inviável para códigos grandes
- Python suporta a edição de código fonte de forma tradicional: arquivo .py
    1. Insira o código do programa em um arquivo .py
    2. No terminal, vá até a pasta onde se encontra o arquivo e execute
    `python3 arquivo.py`

Agora mão a obra colocar em pratica o visto na aula 1 com os exemplos praticos.



# Aula 2 - Classes, Objetos e Abstração

Ao implementar uma classe, devemos definir:

- **Atributos**: características de cada objeto que devemos armazenar. Também chamados de membros.
- Um **inicializador**: método especial para inicializar os atributos.
- **Métodos**: funções que determinam o comportamento da classe.

Depois que a classe está definida, podemos instanciar/criar objetos da classe.

## 1. Inicializadores e atributos

A sintaxe a seguir mostra como definir uma classe em Python.

```python
class Pessoa:
    '''Representação de uma pessoa'''
    
    def __init__(self):
        '''Inicia uma pessoa com atributos com valor padrão'''
        self.nome = ''
        self.idade = 0
```

- `__init__` é o inicializador da classe (parecido com o construtor de outras linguagens)
- Chamado automaticamente quando um objeto da classe é criado
- `self` é a referência ao próprio objeto criado
    - É um nome utilizado para acessar os valores dos atributos dentro da classe
    - É sempre o primeiro parâmetro
    - Referência explícita (em outras linguagens a referência é implícita
    - Similar ao `this` do Java/C++
- `self.nome` e `self.idade` são os 2 atributos (características) da classe
    - Todos os atributos da classe devem ser declarados no `__init__`

## 2. Criando objetos

Uma vez que a classe foi definida, podemos criar objetos (também chamados de instâncias) desta classe. Para compreender melhor estes conceitos, lembre-se que um objeto está para a sua classe assim como uma variável está para o seu tipo.

```python
p = Pessoa() # constroi um objeto da classe Pessoa
# internamente Python chama o método __init__

p.nome = 'Joao' # atribui valores para o atributo nome
p.idade = 20 # atribui valores para o atributo idade
print(p.nome) # acessa os atributos
print(p.idade)

# por enquanto a classe não tem uso, já que não foi definido como podemos utilizá-la
```

## 3. Definindo os métodos de uma classe

O comportamento de uma classe é determinado quando os seus métodos são programados. Um método nada mais é do que uma função dentro do escopo de uma classe. Este deve ser executado/chamado/invocado através de objetos da classe.

### Exemplo usando a classe pessoa:

```python
class Pessoa:
    '''Representação de uma pessoa'''
    
    def __init__(self, nome, idade): # inicializador possui dois parâmetros
        '''Inicia uma pessoa com atributos com valor padrão'''
        self.nome = nome
        self.idade = idade
        
    def imprime(self):
        '''Imprime um texto com informações da Pessoa'''
        print(f'{self.nome} - {self.idade}')
        
# A partir deste ponto no código, o código está fora do escopo da classe
p = Pessoa('Joao', 20) # dois parâmetros passados
p.imprime()
```

### Exemplo 2 - Ponto 2D

```python
class Ponto2D:
    '''Representação de uma coordenada no plano cartesiano'''
    
    def __init__(self, x, y): # inicializador possui dois parâmetros
        '''Inicialização das coordenadas x e y'''
        self.x = x
        self.y = y
        
    def imprime(self):
        '''Imprime um texto com informações do Ponto2D'''
        print('Ponto2D({},{})'.format(self.x, self.y))

# A partir deste ponto no código, o código está fora do escopo da classe
P1 = Ponto2D(3,2)
P1.imprime()
```

### Métodos Mágicos em Python

A linguagem Python possui uma série de métodos mágicos, também conhecidos como "dunders" (*double underscores*), que começam e terminam com `__` (dois underscores). O `__init__` é um exemplo de método mágico.

Existe também um método mágico para converter um objeto em uma string, como mostrado a seguir.

```python
class Pessoa:
    '''Representação de uma pessoa'''
    
    def __init__(self, nome, idade): # inicializador possui dois parâmetros
        '''Inicia uma pessoa com atributos com valor padrão'''
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        '''Retorna uma representaçãoem formato de string de uma Pessoa'''
        return(f'{self.nome} - {self.idade}')

p = Pessoa('Joao', 20) # dois parâmetros passados
s = str(p) # string s recebe o resultado da conversão  
print(s) # imprime string
print(p.__str__()) # faz o mesmo que acima (quase nunca utilizada)
print(p) # melhor forma de imprimir um objeto
```

### Parâmetros de Métodos

Nada impede dos métodos receberem outras instâncias da mesma classe (ou de outras classes) como parâmetros. Por exemplo, pode ser interessante para a classe `Pessoa` ter um método `cumprimeta` implementado. Este método é utilizado para uma pessoa cumprimentar
uma outra passada como parâmetro:

```python
class Pessoa:
    '''Representação de uma pessoa'''
    
    def __init__(self, nome, idade): # inicializador possui dois parâmetros
        '''Inicia uma pessoa com atributos com valor padrão'''
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        '''Retorna uma representaçãoem formato de string de uma Pessoa'''
        return(f'{self.nome} - {self.idade}')
    
    def cumprimenta(self, p):
        '''Cumprimenta uma pessoa passada como parâmetro'''
        print(f'Olá {p.nome}, tudo bem?')

p1 = Pessoa('Joao', 20)
p2 = Pessoa('Maria', 21)
p1.cumprimenta(p2) # pessoa p1 cumprimenta p2
p2.cumprimenta(p1) # pessoa p2 cumprimenta p1
```

## 4. Classes que Utilizam Outras Classes

Em programação orientada a objetos é possível utilizar objetos como atributos das classes sendo construídas.

Um possível exemplo é a classe `Circulo`, que tem como atributos o seu raio e o seu centro. Este último é um objeto da classe `Ponto2D`. Observe o código a seguir.

```python
class Ponto2D:
    '''Representação de uma coordenada no plano cartesiano'''
    
    def __init__(self, x, y):
        '''Inicialização das coordenadas x e y'''
        self.x = x
        self.y = y
        
    def __str__(self):
        '''Retorna uma representação em formato string de um Ponto2D'''
        return 'Ponto2D({},{})'.format(self.x, self.y)
        
class Circulo:
    '''Representação de um círculo'''
    
    def __init__(self, centro, raio):
        '''Centro (x,y) e raio do círculo'''
        self.centro = centro
        self.raio = raio
    
    def move_centro(self, novoX, novoY):
        '''Move o centro do círculo'''
        self.centro = Ponto2D(novoX, novoY)
    
    def __str__(self):
        '''Retorna uma representação em formato string de um Circulo'''
        return 'Circulo({}, {})'.format(self.centro, self.raio)

# podemos criar objetos da classe Circulo
c1 = Circulo(Ponto2D(0,0), 5)
print(c1) #Conversão automática para str

# move o círculo para uma nova posição
c1.move_centro(4,10)
print(c1)

# sempre devemos documentar!
help(c1)
```

## 5. Função Main

Em Python, não é necessário definir a função `main` (ver exemplos acima). Porém, existem vantagens em escrever essa função como a seguir.

```python
def main():
    '''Função principal'''
    C = Circulo(Ponto2D(3,2),10)
    print(C)

# executar a função principal
if __name__ == "__main__":
    main()
```

O significado de `__name__ == "__main__"` vai ficar claro na aula de Módulos. Por enquanto, podemos dizer que o `if` está verificando se nosso programa está rodando no escopo principal (chamado de `__main___`) e não como um Módulo. Por enquanto, podemos ignorar esse `if` e o resultado é o mesmo.

## 6. Detalhes

### Chamada de método em Python

Existe uma alternativa de chamada de método em Python, que fará mais sentido algumas aulas à frente. Na chamada `C.move_centro(x, y)`, da implementação da classe `Circulo`, o que a linguagem faz é "traduzir" esta chamada para `Circulo.move_centro(C, x, y)`. Ou seja, `move_centro` pode ser vista como uma função do módulo/biblioteca `Circulo` para a qual estão sendo passados os parâmetros `C`, `x` e `y`.

```python
C = Circulo(Ponto2D(0,0), 1)
x = y = 1
C.move_centro(x, y) # forma comum de chamar um método
print(C)
Circulo.move_centro(C, x, y) # forma alternativa (nunca utilizada)
print(C)
```

### Python como linguagem dinâmica

Python é uma linguagem dinamicamente tipada. De uma forma curta, o tipo (classe) das variáveis (objetos) é determinado com o programa em execução e não no momento da compilação (como acontece com C++). Além disso, é possível modificar os tipos/classes já definidos.

Isto pode causar confusão. Observe o exemplo a seguir e veja como a linguagem se comporta com a criação dinâmica de atributos. Obviamente, esta forma de se trabalhar com a linguagem está incorreta e consta neste documento para que você entenda o funcionamento da linguagem com maior clareza.

```python
class Ponto2D:
    '''Representação de uma coordenada no plano cartesiano'''
    
    def __init__(self, x, y):
        '''Inicialização das coordenadas x e y'''
        self.x = x
        self.y = y
        
    def __str__(self):
        '''Retorna uma representação em formato string de um Ponto2D'''
        return 'Ponto2D({},{})'.format(self.x, self.y)

# separação do programa que usa as classes das definições das classes
if __name__ == "__main__":
    p1 = Ponto2D(0, 0)
    print(p1)
    p1.cor = 'vermelho' # novo atributo criado dinamicamente; observe que ele não está na definição da classe
    print(p1.cor)
    p2 = Ponto2D(1, 1)
    #print(p2.cor) #erro! o objeto p2 não possui o atributo cor
```

Agora com o visto até o momento refaça os exemplos anteriores e também os novos aplicando os conhecimentos adquiridos até o momento.

# Aula - Encapsulamento

## Motivação para encapsulamento

Considere o exemplo da classe `Estacionamento`, apresentada na aula.
Podemos definir a classe `Estacionamento` como a seguir.

```python
class Estacionamento:
    '''Estacionamento controlando o número de vagas'''
    
    def __init__(self, capacidade):
        '''Inicializa a capacidade e o número de vagas = capacidade'''
        self.capacidade = capacidade # este valor não muda
        self.vagas = capacidade # número de vagas livres
        
    def entrada(self):
        '''Registra entrada de um carro'''
        if self.vagas > 0: # verifica espaço disponível
            self.vagas -= 1 # uma vaga a menos
            print("Um carro entrou.")
        else:
            print("Estacionamento sem vagas... o carro não pode entrar")
            
    def saida(self):
        '''Registra saída de um carro'''
        if self.vagas < self.capacidade: # devemos ter pelo menos um carro dentro
            self.vagas += 1 # incrementa o número de vagas
            print("Um carro saiu")
        else:
            print("Estacionamento vazio... sem carros para sair")
            
    def comVagas(self):
        '''Determina se existem vagas disponíveis '''
        return self.vagas > 0
    
    def lotado(self):
        '''Testa se o estacionamento está lotado'''
        return self.vagas == 0
    
    def vazio(self):
        '''Determina se o estacionamento está vazio'''
        return self.vagas == self.capacidade
            
    def __str__(self):
        '''Converte um Estacionamento em String'''
        return '{} / {} vagas disponíveis.'.format(self.vagas, self.capacidade)
```

```python
est = Estacionamento(5)
print(est.vazio())
est.saida()  
est.entrada()
est.entrada()
est.entrada()
est.entrada()
est.entrada()
print(est)
est.saida()
print(est)
```

Entretanto, observe que nada impede que o usuário da classe `Estacionamento` (programador que está utilizando a classe, não usuário do sistema final) acesse os atributos diretamente, sem utilizar os métodos implementados para manipular objetos da classe.

Veja o código a seguir.

```python
# isto não deveria ser possível:
# acessar diretamente o atributo vagas pode levar a um estado inconsistente do sistema! 
# por exemplo, não teríamos como garantir que vagas <= capacidade. 
est.vagas += 100
print(est)
```

Os modificadores de acesso em Python funcionam assim:

- **Público**: Todo membro/método é público por padrão
- **Privado**: O membro/método se torna privado ao ser declarado com dois underscores `"_"` (**dunders**) na frente do seu nome.

Considere uma segunda versão da classe `Estacionamento` que declara como privados os dois atributos (capacidade e vagas), mostrada a seguir.

```python
class Estacionamento:
    '''Estacionamento controlando o número de vagas'''
    
    def __init__(self, capacidade):
        '''Inicializa a capacidade e o número de vagas = capacidade'''
        
        # note o uso de __ no identificador do atributo
        self.__capacidade = capacidade
        self.__vagas = capacidade
        
    def entrada(self):
        '''Registra entrada de um carro'''
        if self.__vagas > 0:
            self.__vagas -= 1
            print("Um carro entrou.")
        else:
            print("Estacionamento sem vagas")
            
    def saida(self):
        '''Registra saída de um carro'''
        if self.__vagas < self.__capacidade:
            self.__vagas += 1
            print("Um carro saiu")
        else:
            print("Estacionamento vacío")
            
    def comVagas(self):
        '''Determina se existem vagas disponíveis '''
        return self.__vagas > 0
    
    def lotado(self):
        '''Testa se o estacionamento está lotado'''
        return self.__vagas == 0
    
    def vazio(self):
        '''Determina se o estacionamento está vazio'''
        return self.__vagas == self.__capacidade
    
    def __str__(self):
        '''Converte um Estacionamento em String'''
        return '{} / {} vagas disponíveis.'.format(self.__vagas, self.__capacidade)
    
    
```

Agora os usuários da classe não podem acessar diretamente os atributos "privados" da classe.

```python
e = Estacionamento(50)
print(e)
print(e.vazio())
e.entrada()
e.entrada()
print(e)
```

```python
# python detecta o acesso e emite um erro
print(e.__vagas)
```

![image.png](attachment:6091e6de-2e85-48ec-912e-2f19b405839f:image.png)

```python
### 1.2 Acessando/Chamando Atributos e Métodos Privados em Python Fora da Classe

Em Python, sempre é possível acessar os atributos (privados ou não) da classe. 
Para isto, basta utilizar a sintaxe `<obj>._<nomeDaClasse__nomeDoAtributo>.`
```

```python
# truque Python para acessar atributos "privados"
e._Estacionamento__vagas
```

Resumidamente:

- **Nenhum bom programador Python deve acessar/modificar um**
    - Em outras palavras, se o atributo está sinalizado como privado, significa que usuários daquela classe não devem acessá-lo diretamente
    - Python segue uma filosofia que diz que **"programadores são adultos e sabem o que fazem"**
- O encapsulamento permite especificar a **interface pública** da classe
    - Interface pública: parte exposta da classe para quem vai utilizá-la (ela possui outras partes não expostas que compõem a sua implementação)
    - Esconder a sua implementação $\equiv$ encapsular
    - Na classe Estacionamento, os métodos `entrada` e `saida` devem ser utilizados para alterar o valor de `__vagas`

## Getters / Setters

Uma vez que os atributos privados de uma classe só podem ser acessados de dentro da classe, torna-se útil utilizar métodos `getters/setters` para acessar/atribuir novos valores a estes atributos através de métodos:

- Métodos `getters`: retornam o valor de um atributo
- Métodos `setters`: atribuem um novo valor para um atributo

Observe a seguir um exemplo de uso de getters/setters.

```python
class ContaBancaria:
    '''
    Uma conta bancária com saldo e titular.
    Set/get definidos para o titular
    Get definido para o saldo
    '''
    
    def __init__(self, titular):
        '''Saldo e titular (os dois privados)'''
        self.__titular = titular
        self.__saldo = 0
        
    def __str__(self):
        return '{0}: ${1}.'.format(self.__titular , self.__saldo)
    
    def getSaldo(self):
        '''retorna o saldo'''
        return self.__saldo
    
    def getTitular(self):
        '''retorna o titular'''
        return self.__titular
    
    def setTitular(self, novo_titular):
        '''Muda o titular da conta'''
        self.__titular = novo_titular
        
    def deposito(self, valor):
        '''Realiza deposito de um valor'''
        self.__saldo += valor
```

Podemos utilizar os métodos `set` e `get` da classe para acessar, de maneira controlada, os atributos da classe

```python
c = ContaBancaria("pedro")
c.deposito(1000)
print(c)
print(c.getSaldo())
c.setTitular("joão")
print(c)
print(c.getTitular())
```

Setters/Getters em Python:

- Os métodos `set` podem ser muito úteis para validar os novos valores dos atributos. Por exemplo, poderíamos exigir que o novo titular (um objeto do tipo Pessoa e não simplesmente uma string) deve possuir um CPF.
- Esta convenção de getters/setters é fortemente utilizada em Java
- Em Python, ela deve ser utilizada quando necessária. Motivos:
    - Mais código, por exemplo, `print(c.x)` vs `print(c.getX())` (lembre... o Zen de Python... *Beautiful is better than ugly*).
    - É possível burlar o acesso privado à classe, tornando estes métodos inúteis

## Properties: A forma "pythônica" para getters e setters

Existe uma forma mais elegante, eficiente e automática de se utilizar getters/setters em Python: uso da função `property`.

Observe a nova versão da classe `ContaBancaria` a seguir.

```python
class ContaBancaria:
    
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
        
    def __str__(self):
        return '{0}: ${1}.'.format(self.__titular , self.__saldo)
    
    def getSaldo(self):
        '''retorna o saldo'''
        print('Método getSaldo ')
        return self.__saldo
    
    def getTitular(self):
        '''retorna o titular'''
        print('Método getTitular')
        return self.__titular
    
    def setTitular(self, novo_titular):
        '''muda o titular da conta'''
        print('Método setTitular')
        self.__titular = novo_titular
        
    def deposita(self, valor):
        '''Deposita valor'''
        self.__saldo += valor
    
    # ainda dentro do escopo da classe
    titular = property(getTitular, setTitular)
    saldo = property(getSaldo)
```

```python
c1 = ContaBancaria("joao")
c1.deposita(2000)
print(c1.saldo) # saldo é um método "disfarçado" (acesso a um atributo que realiza uma chamada a um método)
print(c1.titular)
c1.titular = "jose"
#c1.saldo = 4  Erro!
print(c1)
```

### Decoradores em Python

Uma alternativa ainda mais interessante é definir setters e getters utilizando **decoradores**.

```python
class ContaBancaria:
    
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
        
    def __str__(self):
        return '{0}: ${1}.'.format(self.__titular , self.__saldo)
    
    @property
    def saldo(self):
        '''retorna o saldo'''
        print('Método getSaldo ')
        return self.__saldo

    @property
    def titular(self):
        '''retorna o titular'''
        print('Método getTitular')
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular): # observe que na verdade estamos redefinindo o método anterior. isso é possível com o uso de property 
        '''Muda o titular da conta'''
        print('Método setTitular')
        self.__titular = novo_titular
        
    def depositar(self, valor):
        '''Depositar valor'''
        self.__saldo += valor
```

```python
c1 = ContaBancaria("joao")
c1.depositar(2000)
print(c1.saldo) # chama o getter de saldo
print(c1.titular) # chama o getter de titular
c1.titular = "jose" # chama o setter de titular
#c1.saldo = 4 # erro! saldo não tem setter
print(c1)
```

Note que:

- O atributo privado titular possui um setter e getter.
- O atributo saldo só possui um getter (retornando o saldo atual)
- `@property` define o getter
- `@<atributo>.setter` define o setter (como no exemplo `@titular.setter`)