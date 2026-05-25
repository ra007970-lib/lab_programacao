vetor = [2.5, 7.5, 10, 4.0]
soma = 0
for valor in vetor:
    soma = soma + valor
    media = soma / len(vetor)

print(f"A media do vetor é {media:.2f}")


mais_proximo = vetor[0]

#testa menor distancia
if mais_proximo > media:
    menor_distancia = mais_proximo - media
else:
    menor_distancia = media - mais_proximo

#testando valores
for valor in vetor:
    if valor > media:
        distancia = valor - media
    else:
        distancia = media - valor

    #encontrar o mais proximo
    if distancia < menor_distancia:
        menor_distancia = distancia
        mais_proximo = valor
print(f"O valor mais próximo da média é {mais_proximo}")