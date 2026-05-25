import random

lancamento = []

for i in range(100):
    resultado = (random.randint(1, 6))
    lancamento.append(resultado)



frequencia = []
for face in range(1, 7):
    quantidade = lancamento.count(face)
    frequencia.append(quantidade)

print("Vetor de lançamento (100 vezes)")
print(lancamento)
print("\nVetor de frequencia das faces: 1, 2, 3, 4, 5, 6")
print(frequencia)








