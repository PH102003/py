idade = int(input("Digite sua idade aqui: "))
nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
brasileiro = input("Você é brasileiro? (True/False): ").strip().capitalize() == "True"
print(f"Sua idade é: {idade}\nSeu nome é {nome}\nSeu salario é de: R$ {salario}\nÉ brasileiro? {brasileiro}")

#A função strip() remove os espaços em branco (ou outros caracteres especificados) 
#do início e do fim de uma string. Por padrão, ela remove espaços, quebras de linha (\n) e tabulações (\t).
#A função capitalize() transforma o primeiro caractere da string em maiúsculo e todos os outros em minúsculo. 