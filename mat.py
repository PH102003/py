mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#elementos da primeira linha
for elem in mat[0]:
    print(elem)
    print()
#todos os elementos da matriz
for linha in mat:
    for elem in linha:
        print(elem)

#pegar elemento do meio da segunda coluna

for i, row in enumerate(mat):
    if(i == 1):
        for j, elem in enumerate(row):
            if(j == 1):
                print(elem)

"""Desafio - Crie um programa que peça pra um usuário preencher uma matriz 3x4, 
depois realizar busca e achar o menor e maior
#número da matriz
"""

#matriz 3x4
linhas = []
for i in range(3):  # 3 linhas
    colunas = []
    for j in range(4):  # 4 colunas
        valor = int(input(f"Digite o número para a linha {i} e coluna {j}: "))
        colunas.append(valor)
    linhas.append(colunas)  # Adiciona a linha (com colunas) à lista de linhas

# Encontra o menor e o maior valor da matriz inteira
menor_valor = min(min(colunas) for colunas in linhas)  # Menor valor de toda a matriz
maior_valor = max(max(colunas) for colunas in linhas)  # Maior valor de toda a matriz

# Exibe os resultados da matriz inteira
print(f"\nMenor valor da matriz: {menor_valor}.")
print(f"Maior valor da matriz: {maior_valor}.")

# Encontra e imprime o maior e o menor valor de cada linha
for i, linha in enumerate(linhas):
    print(f"\nLinha {i}:")
    print(f"Menor valor: {min(linha)}")
    print(f"Maior valor: {max(linha)}")