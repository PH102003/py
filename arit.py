calc = int(5 )
print (calc)

#O % é usado para trabalhar com ciclos, como quando você precisa "voltar ao início" após alcançar um limite. 
# Isso é útil, por exemplo, para rotacionar listas ou calcular posições em estruturas cíclicas
dias_da_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
indice = 10 % 7  # 10º dia da semana cai no mesmo dia do 3º (10 ÷ 7 tem resto 3)
print(dias_da_semana[indice])  # Saída: "Ter"
calc2 = ( 12 % 2.1)
print (calc2)