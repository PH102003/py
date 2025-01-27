print("25")
print("31")
print()
print("31")
print("31")
print("25", end='')
print("22")
#formatador
print(f"38")
print(" PREÇO: R$ {24.233: .2f}")
#sem o formatador 'f', a máquina entende que é um texto corrido
#2f se refere ao ponto flutuante (famoso float)
#sempre usar '{' e '}' pra dados numéricos com casa decimal, data e tempo e etc
#olhe o exemplo abaixo
#'e' é pra notaçao cientifica
#3 casas decimais- 3f
print(f"PREÇO: R${24.233: .3f}")
print(f"PREÇO: R$(24.233: .3f)")
print(f"PREÇO: R${24.233: .3e}")
#pra ano mes e dia print(f"{<dado>: %Y-%m-%d}")
#LISTA DE FORMATADORES EM PRINTS
#barra invertida coloca \\ 2 vezes
#aspas simples \'
#tabulação \t
#aspas dupla \"
#tab vertical \v
#apagar-backspace \b

print("O valor inteiro é:", 10)
print(f"O valor 10 em decimal é: {10: d}")
print(f"O valor 10 em binário é: {10: b}")
print(f"{10: d}")
print(f"O valor de Pi é: {3.14159265: f}")

#DESAFIO F-strings
# Impressão formatada com f-strings e caracteres de escape
print(f"Nome:\t{"Pedro"}\nIdade:\t{"13"} anos\nSalário:\tR$ {1544.43:.2f}\nNacionalidade:\t{"Brasileiro"}")

#ENTRADA DE DADOS
input("\'Escreva algo aqui\'")


