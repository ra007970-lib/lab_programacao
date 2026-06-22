nomes = []

#entrada de dados
print("Digite 5 nomes: ")
for i in range(5):
    nome = input(f"Qual é o {i + 1}° nome: ")
    nomes.append(nome)

nomes_invertidos = []
#montar a lista inversa


nomes_invertidos.append(nomes[4])
nomes_invertidos.append(nomes[3])
nomes_invertidos.append(nomes[2])
nomes_invertidos.append(nomes[1])
nomes_invertidos.append(nomes[0])

print(f"\nLista original: {nomes}")
print(f"Listas invertida: {nomes_invertidos}")