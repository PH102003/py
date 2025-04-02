texto = "oi"
#concat
print(texto + "dois")
#repetição
print(texto * 25)
#indexação
texto[0]
print(texto[0])
#pertencimento
#if subtexto in texto:
    #pass
#funções
texto.upper()
texto.lower()
#corta os espaçoes excedentes
texto.strip()
texto.lstrip()
texto.rstrip()
#hands-on

nome = (input("Diga seu nome: ")).capitalize()
sobrenome= (input("Diga seu sobrenome: ")).capitalize()

tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)

nome_completo = nome+" "+sobrenome
tamanho_nome_completo = len(nome_completo)

print(f"Seu nome tem: {tamanho_nome} caracteres.\n Seu sobrenome tem: {tamanho_sobrenome} caracteres.")
print(f"Seu nome completo é:{nome_completo}")
print(f"O seu nome completo tem:{tamanho_nome_completo} caracteres")

#desafio
# Lista para armazenar as palavras digitadas
lista_palavras = []

while True:
    entrada = input("Digite alguma palavra: ")
    
    # Verifica se o usuário quer sair
    if entrada == "/exit":
        break  # Sai do loop imediatamente
    
    # Adiciona a palavra à lista (lembrar do append quando quiser trabalhar com a inserção de elementos numa lista)
    lista_palavras.append(entrada)

# join junta todas as palavras (concatena automaticamente) da lista com " " (espaço)
resultado = " ".join(lista_palavras)


print(f"As palavras escritas foram: {resultado}")