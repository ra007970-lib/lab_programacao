vetor = []
cont = 0
#entreda de dados
print("Digite 5 números para o vetor:")
while cont < 5:
    valor = input(f"Posição {cont}: ")
    vetor.append(valor)
    cont += 1

#pedindo posição
x = input("\nDigite o valor que você deseja buscar (x): ")


posicao_encontrada = -1
i = 0

while i < 5:
    if vetor[i] == x:
        posicao_encontrada = i
        break  
    i += 1

#exibindo resultados
print(f"Resultado: {posicao_encontrada}")
