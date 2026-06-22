# Criar lista com 5 notas
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

# Descobrir a menor nota
menor_valor = notas[0]
indice_menor = 0

for i in range(1, len(notas)):
    if notas[i] < menor_valor:
        menor_valor = notas[i]
        indice_menor = i

#Criar uma nova lista  com as notas restantes
notas_restantes = []
for i in range(len(notas)):
    if i != indice_menor:
        notas_restantes.append(notas[i])

#Exibe as notas restantes
print("\nNotas restantes:")
for nota in notas_restantes:
    print(nota)
