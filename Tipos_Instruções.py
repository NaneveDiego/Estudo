""" 
A solução de problemas resolvidos pela computação envolvem a manipulação de informações
sendo essas informações divididas em grosso modo em dois tipos:

Dados e instruções

Dados são as informações a serem processadas por um computador

Em python temos várias categorias de tipos de dados

Texto, literal, alfanumérico ou string -> str
Numéricos -> int, float, complex
Sequencia - > list, tuple, range
Mapping -> dict
Set -> set, frozenset
Boolean ou lógico -> bool
Binário -> bytes, bytearray, memoryview
None -> NoneType

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
Variáveis são contêineres para armazenar valores de dados.

Python não tem comando para declarar uma variável,
a variavel é criada no momento que é atribuida a um valor

Exemplo
"""

c = 5
y = "John"
print(x)
print(y)


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


"""

