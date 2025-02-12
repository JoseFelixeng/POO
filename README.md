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


# Aula - Estruturas de Dados da Biblioteca Padrão Python

As classes a seguir, que representam **sequências** em Python (`tuple`, `list` e `str`), possuem um conjunto de operações bem definido na sua interface pública.

## 1. Tuplas

- Utilizadas para guardar vários valores agrupados
    - Observe que em Python os valores são objetos e como tudo é objeto em Python, uma tupla pode armazenar qualquer coisa
- Definidas pela especificação de vários elementos separados por vírgula entre parênteses `()`
- Exemplos:
    - Tupla de inteiros: `a = (1,2,3)`
    - Tupla de strings: `b = ('alo','mundo')`
    - Tupla mista: `c = ((1, 'cálculo',10), (2, 'álgebra', 9))`
- Uma tupla não é alterável: uma vez definida, ela não pode ser alterada

Observe como se trabalha com tuplas em Python a seguir.

```python
l = ('alo', 3, ('e', 'f')) # declara uma tupla
print(type(l)) # tuple
x = l[0] # acessa o primeiro elemento da tupla
y = l[1] # acessa o segundo elemento da tupla
print(x,y)

# "desempacota" (unpack) tupla: atribui tupla a um número de valores (deve ser igual ao tamanho da tupla)
x,y,z = l
print(x,y,z)

# tuplas são imutáveis: não é possível adicionar, remover ou alterar elementos
#l[0] = 'mundo' # erro

# toda função que retorna mais de um valor em Python
# na verdade retorna uma tupla com todos os valores.

def sumprod(x, y):
    '''Retorna a soma e o produto de um número'''
    return (x+y, x*y)

if __name__ == "__main__":

    # duas formas equivalentes de atribuição de tuplas
    
    # forma 1: atribui em a o primeiro resultado e em b o segundo
    a,b = sumprod(3,5)
    print('Soma: {}, produto: {}'.format(a, b))

    # forma 2: atribui o resultado a uma tupla
    t = sumprod(3,5)
    print('Soma: {}, produto: {}'.format(t[0], t[1]))
```

## 2. Listas

- Utilizadas para guardar uma coleção de valores que pode ser alterada
- Definidas pela especificação de vários elementos separados por vírgula entre colchetes `[]`
- Exemplos:
    - Lista de inteiros: `a = [1,2,3]`
    - Lista de strings: `b = ['alo','mundo']`
    - Lista mista: `c = [1.93, 'alo', (0,'aula')]`

Observe como se trabalha com listas em Python a seguir.

```python
l = ['alo', 3, ('e', 'f')] # declara uma lista
print(type(l)) # list
x = l[0] # acessa o primeiro elemento da lista
y = l[1] # acessa o segundo elemento da lista
print(x,y)

# "desempacota" (unpack) lista: atribui lista a um número de valores (deve ser igual ao tamanho da lista)
x,y,z = l
print(x,y,z)

# listas são mutáveis: é possível adicionar, remover ou alterar elementos
l[0] = 'mundo'
print(l)
```

Listas em Python possuem outras operações, definidas na interface pública da classe (digite `help(list)` em um terminal para mais detalhes):

- `append`: adiciona objeto ao final da lista
- `insert`: adiciona objeto em posição específica da lista
- `remove`: remove primeira ocorrência do parâmetro passado
- `extend`: adiciona todos os objetos do parâmetro
- `clear`: remove todos os objetos
- `pop`: remove o último objeto ou objeto na posição do parâmetro
- `sort`: ordena a lista
- `copy`: retorna uma cópia da lista
- `count`: retorna quantos objetos são iguais ao parâmetro

```python
l = [] # cria lista vazia
l.append(1)
print(l)
l2 = [2,3,4]
l.extend(l2) # adiciona os elementos de l2 em l
print(l)
l3 = l + l # operador de soma concatena listas
print(l3)
l = [1,3]
l.insert(1,2) # insere o número 2 na posição 1
print(l)
l.clear() # remove todos os elementos
print(l)
l = ['a','b','c','b']
l.remove('b') # remove a primeira ocorrência 
print(l)
l.pop() # remove o último elemento
print(l)
l += ['e','f','g'] # soma e atribuição também está implementado
print(l)
l.pop(1) # remove o elemento na posição 1
print(l)
l = [1,4,2,6,4]
l.sort() # ordena
print(l)
l2 = l.copy() # cria uma copia
print(l2)
print(l.count(4)) # número de ocorrências do número 4 na lista
```

## 3. Strings

Strings também são consideradas sequências em Python e portanto, possuem diversos comportamentos em comum com tuplas e listas. Assim como tuplas, strings são imutáveis.

O uso básico de strings é mostrado a seguir. Para mais detalhes da interface pública da classe `str`, digite `help(str)` em um terminal.

```python
s = "alo"
print(type(s)) # str
print(s[0]) # acessa primeiro caractere da string
s2 = "alo mundo Python"
print(s2.count(' ')) # conta espaços em branco na string
#s2[2] = 'a' # erro: string é imutável
s2 += "!" # concatena string com uma outra
print(s2)
```

## 4. Dicionários

Aleḿ das classes que representam sequências, Python também possui o tipo dicionário. Apesar de não ser considerado uma sequência, esta classe possui alguma similaridade com as sequências.

- Tipo de dados `dict`
- Utilizado para armazenar vários pares formados por uma chave e um valor
- Definido pela especificação de vários pares `chave: valor` separados por vírgula entre chaves `{}`
- Exemplos de dicionários:
    - `d1 = {0: 'zero', 1: 'um', 2: 'dois'}`
    - `d2 = {'zero': 0, 'um': 1, 'dois': 2}`
    - `d3 = {'zero': 0, 1: [1,2,3], 'c': (3.0, -3.0)}`
- O acesso aos seus elementos se dá com o uso da chave entre colchetes

Observe como se trabalha com dicionários em Python a seguir.

```python
d = {1:'um', 2:'dois', 3:'três'} # declara um dicionário
print(type(d)) #dict
print(d[2])
d[4] = 'quatro' # adiciona novo par chave (4) -> valor ('quatro')
print(d)
d[1] = 'one' # podemos alterar o valor de uma chave
print(d)
```

Os dicionários são muito úteis para acessar informações indexadas por uma chave. Observe a seguir.

```python
class Pessoa:
    '''Definição de uma Pessoa'''
    def __init__(self, cpf, nome, fone):
        self.cpf = cpf
        self.nome = nome
        self.fone = fone
        
    def __str__(self):
        # esta forma de formatar string funciona com Python versão > 3.6
        return f'cpf={self.cpf}, nome={self.nome}, fone={self.fone}'
        #return 'cpf={}, nome={}, fone={}'.format(self.cpf, self.nome, self.fone)

if __name__ == "__main__":
    # cria objetos da classe Pessoa
    P1 = Pessoa('11111-1', 'carlos', '12345')
    P2 = Pessoa('22222-2', 'mario', '54321')
    P3 = Pessoa('33333-3', 'joão', '133245')

    pessoas = {} # cria um dicionário
    pessoas[P1.cpf] = P1 # chave: cpf, valor: pessoa
    pessoas[P2.cpf] = P2
    pessoas[P3.cpf] = P3

    cpf = '22222-2'
    if cpf in pessoas:
        print(f'Pessoa: {pessoas[cpf]}')
    else:
        print('CPF não cadastrado')
```

## 5. Operações comuns em estruturas de dados

Todos os tipos de sequências apresentados suportam um conjunto comum de operações. Estas operações são dadas pela forma de acesso aos objetos das sequências, formas de se iterar nos objetos contidos nas sequências e a funções/operadores utilitários que recebem sequências como parâmetros.

### Acesso a posições das sequências

Sendo `s` seja uma sequência (`tuple`, `list` ou `str`):

- `s[0]` acessa o primeiro elemento de `s`, `s[1]` o segundo e assim por diante
- `s[-1]` acessa o último elemento de `s`, `s[-2]` o penúltimo e assim por diante
- Caso o índice `i` em `s[i]` seja maior ou igual ao total de elementos, ocorre um erro de execução

### Fatiamento (*slicing*)

Sendo `s` seja uma sequência (`tuple`, `list` ou `str`):

- É possível realizar o seu "fatiamento":
    - `s[2:5]`: retorna os elementos de índice 2, 3 e 4
    - `s[i:j]`: retorna os elementos de índice `i` até `j-1`
    - `s[i:]`: retorna os elementos de índice `i` até o último índice da sequência
    - `s[:i]`: retorna os elementos do primeiro índice até o índice `i-1`
    - `s[i:j:d]`: retorna os elementos de índice `i` até `j-1` com incremento de `d`
    - `s[::]`: retorna todos os elementos
    - `s[::-1]`: retorna todos os elementos na ordem inversa

```python
s = ('x', 'y', 'z', 1, 2, 3, 'a', 'b', 'c')
print(s[1:3]) # seq. com objetos nas posições 1 e 2
print(s[-1]) # objeto na última posição
print(s[-1:1:-1]) # seq. com objetos nas posições 8, 7, 6... até 2
```

### Outras funções em sequências

Sequências em Python também possuem funções especiais que as recebem como parâmetro (estas funções também funcionam em dicionários):

- `len`: retorna o tamanho de uma sequência/dicionário
- `in`: operador (e não função) que retorna verdadeiro caso um objeto pertença à sequência/chaves de um dicionário
- `max`: retorna o maior valor da sequência/chaves de um dicionário (os objetos precisam ter o mesmo tipo)
- `min`: retorna o menor valor da sequência/chaves de um dicionário (os objetos precisam ter o mesmo tipo)
- `sum`: retorna o somatório da sequência/chaves de um dicionário (se eles tiverem tipo numérico)
- `any`: retorna verdadeiro se algum valor da sequência/chaves de um dicionário tiver valor lógico `True`
- `all`: retorna verdadeiro se todos os valores da sequência/chaves de um dicionário tiverem valor lógico `True`

```python
s = [1, 2, 3]
print(len(s))
print(5 in s)
print(max(s))
print(min(s))
print(sum(s))
print(any(s))
s = [0, 2, 3]
print(all(s))
d = {1: 'um', 2: 'dois', 3: 'tres'}
print(sum(d)) # opera nas chaves do dicionário
```

### Percorrendo os elementos de uma sequência

Sequências em Python podem ser percorridas (iteradas) de diversas maneiras, como mostrado a seguir.

```python
l = ['a','b','c']

# 1. Estilo c++ 
for i in range(len(l)): # range é uma função que cria um intervalo de valores
    print(l[i], end='-') # end é o caractere a ser impresso no final (padrão, \n)
print('\n============================')

# Lembre o Zen de Python... "Beautiful is better than ugly."
# 2. com o operador 'in' -> a variável do laço recebe cada objeto da sequência diretamente
for i in l:
    print(i, end='-')    
print('\n============================')    

# 3. função enumerate: retorna uma enumeração (tuplas formadas por (posição, valor))
for e in enumerate(l):
    print(e, end='-')
print('\n============================')    

#Uso comum
for (i,v) in enumerate(l):
    print('posição={}, valor={}'.format(i, v))
```

```python
d = {1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco'}

# percorre todas as chaves
for c in d.keys(): # mesma coisa se só usar d
    print(c)

# percorre todos os valores
for v in d.values():
    print(v)
    
# percorre todos pares chave/valor
for c, v in d.items(): # mesma coisa se usar enumerate(d)
    print('chave: {}, valor: {}'.format(c,v))
```

## Extra: `Iterators` e `Generators`

### Iteradores

Em linguagens orientadas a objetos, é comum utilizar objetos especiais, chamados de **iteradores** (*iterators*), para percorrer suas estruturas de dados.

Em Python, é possível utilizar as função `next`, que retorna o próximo elemento ou resulta no erro de execução `StopIteration` quando não houver mais elementos (mais na frente estudaremos o mecanismo de erros e exceções).

Para isto, você deve primeiramente criar um objeto do tipo `iter` passando um objeto iterável (sequência ou dicionário) no construtor.

```python
t = ('a','b','c')
it = iter(t) # objeto iterador da tupla t 
print(next(it)) # 'a'
print(next(it)) # 'b'
print(next(it)) # 'c'
#next(it) # este next resulta em erro
```

### Generators

Um outro comando muito útil em Python é o `yield`. Este comando, ao ser utilizado em uma função ao invés de um `return`, faz com que a função se torne um objeto especial chamado de `generator`.

Desta forma, uma chamada à função gera um objeto iterável. Ao ser utilizada a função especial `next` neste objeto, um valor de retorno é produzido, mas a função "se lembra" onde estava (guarda o seu estado) para produzir o resultado correto em uma próxima chamada.

Observe um exemplo de `generator` que retorna, sob demanda, a sequência de Fibonacci.

```python
# gera a sequência Fibonacci sob demanda
def fib(n):
    '''n >= 2 é o número de elementos a serem gerados'''
    a = b = 1 # sim, isso funciona em Python
    yield a # gera o primeiro valor
    yield b # gera o segundo valor

    # gera os outros valores
    for i in range(n-2):
        s = a + b
        yield s
        # atualiza a e b
        a,b = b, s # atribuição simultânea

if __name__ == "__main__":
    for x in fib(10): # chamada de função gera um iterável (generator)
        print(x) # laço itera e imprime todos os valores produzidos

    type(fib(10)) # função se torna um objeto generator
    
    #seq = fib(10) # alternativa: seq é o generator, que é um iterável
    #print(next(seq)) # chamar função next no iterável gerado
    #print(next(seq))
    #print(next(seq))
```