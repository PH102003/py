nota = (float(input("Diga qual sua nota aqui:")))
"""Se quiser que somente um bloco seja executado, o melhor é usar if + elif + else.
Se precisar que mais de uma condição seja verdadeira ao mesmo tempo, pode usar somente if separados.
    """

if(nota >= 7.0):
    print("Aprovado!")
elif(nota < 7.0 and nota >= 4.0):
    print("Tem direito a exame!")
else:
    print("Buuuuuurrrro")


idade = (int(input("Diga qual sua idade aqui:")))

nome = input("Diga seu nome: ").capitalize()
#desafio idade
if(idade >= 18):
    print(f"{nome} é maior de idade!")
else:
    print("Menor de idade!")

#desafio dia semana

numero_escolhido = int(input("Escolha um número entre 1 e 7: "))
if(numero_escolhido == 1):
    print("Domingo")
elif(numero_escolhido == 2):
    print("Segunda-feira")
elif(numero_escolhido == 3):
    print("Terça-feira")
else:
    print("Erro! Número inválido")

        


