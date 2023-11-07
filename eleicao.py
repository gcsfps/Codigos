print("Algoritmo para contar as pessoas em cada classe eleitoral") 
ne = ef = eo = 0

i = 0

while i < 1000:
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    
    if idade < 16:
        print("Menor de 16 anos. Não vota.")
        ne += 1
    elif 16 <= idade <= 17:
        print("16 ou 17 anos. Voto facultativo.")
        ef+= 1
    elif 18 <= idade <= 65:
        print("18 a 65 anos. Voto obrigatório.")
        eo += 1
    else:
        print("Maior de 65 anos. Voto facultativo.")
        ef+=1
        
    i += 1

print("\nResumo das Classes Eleitorais:")
print(f"Não eleitor : {ne} pessoas")
print(f"Eleitor facultativo (16-17-maior de 65 anos): {ef} pessoas")
print(f"Eleitor obrigatório (18-65 anos): {eo} pessoas")