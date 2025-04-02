L = ["A", "B", "C", "D"]
print(L[0])
L.pop(0)
#append adiciona o elemento em determinado indice (nesse caso, o indice 2)no final daquela lista
L.append(L[2])
print(L)

#hands on
lista_vazia = []
soma = 0
media = 0 
for i in range (5):
    dado = (int(input("Digite um número inteiro: ")))
    #add o elemento escolhido no fim da lista_vazia
    lista_vazia.append(dado)
    #acumula a soma a partir das inserções dos dados
    soma += dado
media = soma / 5
#navegando pelos elementos da lista_vazia
for elem in lista_vazia:
    print(elem)
print(f"Media dos elementos: {media}")
print(lista_vazia)

#desafio
lista_vazia_dois = []
while(True):
    novo_numero = int(input("Digite um numero que será add na lista: "))
    lista_vazia_dois.append(novo_numero)
    if novo_numero == 0:
        break
    
lista_vazia_dois.remove(0)
print(len(lista_vazia_dois))
print(f"O menor número da lista é: {min(lista_vazia_dois)}.\n\n O maior é {max(lista_vazia_dois)}")
