soma = 0
cont = 0
for var in range(1, 200):
    if var % 3 == 0:
        soma += var
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é de {soma}...')        
        