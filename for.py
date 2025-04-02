"""for - diferente do while, precisa de algo iterável para funcionar devidamente
(ex.: listas)"""

lista = [1,2,3,4,5,6]
for x in lista:
#o 'x' assume o conteudo de cada item na lista a cada iteração 
    lista [x] = 1

#hands-on
#inicio = 1, fim = 11 (-1) e passo = 1 (ele incrementa o valor de 'i' em '1')
for i in range(1,11,1):
    print(i, " ", end="")

#desafio
entrada = (int(input("\n\nDigite um número de 1 a 10: ")))
if(entrada in range(1,11)):
    print(entrada, "é válido")
else:
    print("Fora do intervalo!")

#uso do continue - faz com que o elemento na 5 iteração não seja 'lido'
for i in range(1,11,1):
    if i == 5:
        continue
    print(i)    
#uso do break - faz com que todos os elementos após o 5 não sejam 'lidos'
for i in range(1,11,1):
    if i == 5:
        break
    print(i) 
#desafio contador
# Inicializa o contador com zero
contador = 0

# Loop infinito para manter o programa rodando
while True:
    # Exibe o valor atual do contador
    print(f"Contador atual: {contador}")
    
    # Exibe as opções para o usuário
    print("Escolha uma opção:")
    print("1 - Incrementar contador")
    print("2 - Sair")
    
    # Solicita a escolha do usuário
    escolha = input("Digite o número da opção desejada: ")
    
    # Verifica a escolha do usuário
    if escolha == "1":
        # Incrementa o contador em 1
        contador += 1
        print("Contador incrementado!")
        continue  # Volta ao início do loop
    elif escolha == "2":
        # Encerra o programa
        print("Encerrando o programa...")
        break  # Sai do loop
    else:
        # Mensagem de erro para opção inválida
        print("Opção inválida! Tente novamente.")


    


