""" 
A solução de problemas resolvidos pela computação envolvem a manipulação de informações
sendo essas informações divididas em grosso modo em dois tipos:

Dados e instruções

Dados são as informações a serem processadas por um computador

Em python temos várias categorias de tipos de dados



-F-

Texto, literal, alfanumérico ou string -> str
Numéricos -> int, float, complex
Sequencia - > list, tuple, range
Mapping -> dict
Set -> set, frozenset
Boolean ou lógico -> bool
Binário -> bytes, bytearray, memoryview
None -> NoneType

"""
""" 
#exemplos

#Texto str
x = str("Hello World")
print(x)

#Numéricos

#int
x = 20
print(x)

#float
x = 20.5
print(x)

#complex
x = 1j 
print(x)

"""

""" 
Variáveis são contêineres para armazenar valores de dados.

Python não tem comando para declarar uma variável,
a variavel é criada no momento que é atribuida a um valor

Exemplo
"""

"""

c = 5
y = "John"
print(x)
print(y)

"""

""" 
Regras da variavel
- O primeiro caractere do nome de uma variável não poderá ser, em hipótese alguma, um número; sempre deverá ser uma letra; 
- O nome de uma variável não poderá possuir espaços em branco;
- O nome de uma variável não poderá ser uma palavra reservada (uma instrução)
- Não poderão ser utilizados caracteres especiais ( # ! ?)

Constantes são contêineres para armazenar valores de dados que não podem ser mudados

Em python não temos uma palavra chave ou uma instrução para definir as constantes
Apenas utilizamos uma variavel com a letra maiuscula e separada com underscores (snake_case)

PI = 3.14159
EULER_NUMBER = 2.71828


-F-
Operadores

Operadores são usados para realizar operações matemáticas ou atribuir variavies

Em python temos vários tipos de operadores

Aritméticos
Atribuição
Comparação
Lógicos
Identidade
Associação
bit a bit




Operadores Aritméticos

+ adição
- subtração
* multiplicação
/ divisão
% modulo (ou resto)
** exponenciação
// divisão apromixada


Operadores de atribuição

=   x=5  x recebe 5
+=  x+=3  x= x+3
-=  x-=3  x= x-3
*=  x*=3  x= x*3
/=  x/=3  x= x/3





Instruções
São o conjunto de palavras-chaves de uma linguagem de programação que tem como finalidade
comandar, em um computador, o funcionamento e o tratamento dos dados armazenados

Vamos utilizar input() para entrada de dados
e print() para saida de dados

exemplo:


"""

"""

#Calculo da area de uma circunferencia
PI = 3.14159
R = float(input("Insira o r em metros:\n"))
Area = PI*R**2
print(Area)

"""

ht = int(input("Horas trabalhadas:\n"))
vh = float(input("Valor da hora aula:\n"))
pd = float(input("Percentual de desconto:\n"))

sb = ht * vh
td = (pd/100)*sb
sl = sb - td

print(sb,sl)


