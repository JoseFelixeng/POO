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