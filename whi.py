import sys


i = 1

while i<=10:
    #end ="" pra não quebrar linha
    print(i)
    
    i += 1
    print(f"\n")

#desafio

j = 10

while j>= 1:
    j -= 1
    print(j, end="")
#outro desafio

while True:
    numero_escolhido = int(input("\nDigite um número: "))
    if numero_escolhido == 0:
        print("Programa encerrado.")
        sys.exit(1)
        


