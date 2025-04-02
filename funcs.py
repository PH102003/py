import os
import math

x = 16
print(math.sqrt(x))

angulo = 30
print(math.sin(angulo))

#current working directory
diretorio = os.getcwd()
print("o diretorio atual é: ", diretorio)

"""apaga saidas do terminal"""
#os.system("cls")

lista = [10,20,30]

print(len(lista))
print(sum(lista))

ages = [5, 12, 17, 18, 24, 32]

#função que filtra/mostra idades maiores ou iguais a 18
#parametro 'y' se torna 'ages' e é usado como base para o filter
def myFunc(y):
  if y <= 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for y in adults:
  print(y)
"""filter, só que mostra números que são pares dentro de um array"""
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  


#sorted - coloca os itens na ordem correta, seja número ou letra
a = ("jonas alves", "aline cerqueira","carlos joao")
x = sorted(a)
print(x)
"""nesse caso o split remove qualquer outra string que venha depois de um espaço.
Notar o [-1], isso corresponde ao segundo item que vai ser removido.
Nesse caso, será o sobrenome das pessoas listadas acima. """
sobrenome = [sn.split()[-1] for sn in a]
print(sobrenome)

"""range - Pega a sequencia de números dentro de determinado alcance. 
Nesse exemplo, 6 (0,1,2,3,4,5)"""
z = range(6)
for n in z:
  print(n)

"""enumerate - Coloca uma enumeração numa tupla"""
algo = ("verde", "azul", "amarelo", "cinza")
result = enumerate(algo)
print(list(result))

"""zip - Combina 2 ou mais iteraveis"""
pessoas = ['jonas', 'leticia']
idades = [15, 17]
combinacao = zip(pessoas,idades)
print(list(combinacao))

"""lambda - função que faz outra função"""
"""map - Aplica uma função a cada elemento de um iterável"""
numeros = [1, 2, 3, 4]
quadrados = map(lambda x: x**2, numeros)
print(list(quadrados))  #elevando todos ao quadrado

"""type - retorna o tipo de um obj"""
print(type('c'))
#nesse caso, 'str'
"""id - Retorna o identificador único de um objeto na memória"""
co = 10
print(id(co))
print(id(quadrados))

def alguma():
  return 0

"""callable - verifica se um objeto pode ser  chamado como uma funçao"""
print(callable(alguma))  # True
print(callable(42))   # False
"""isinstace - verifica se o objeto é de determinado tipo"""
print(isinstance(10, str))  # False
print(isinstance("texto", str))  # True

"""any - retorna true se qualquer item de por exmeplo, uma lista, for verdadeiro """
lista_doidera = [1,2,3,6]
print(f"Oi {any([lista_doidera])}\n")
"""all - retorna true se *todos* os itens de uma lista forem verdadeiros (não pode conter 0, False, none..)"""
print(f"VOCÊ NÃO SABIA {all(lista_doidera)}")
"""eval - pega uma string e converte ela numa operação matemática"""

divisao = eval("2 / 2")
print(divisao)

"""help - mostra documentação das palavras reservadas/objetos python """
help(map)

"""exec - executa determinado bloco de código"""
codigo = """
for i in range(3):
    print(i)
"""
exec(codigo)

"""locals - mostra as variáveis dentro de determinado escopo"""

def outroexemplo():
  zy = 2
  print(locals())

outroexemplo()

"""globals = retorna todas as variáveis globais"""

zoa = "algo"
print(globals())


