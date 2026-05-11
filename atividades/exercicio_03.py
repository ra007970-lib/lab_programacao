import random


vetor_dados = []
contador = 0

while contador < 50:
    resultado = random.randint(1, 6)
    vetor_dados.append(resultado)
    contador += 1

#cantando face 6
total_face_6 = 0
i = 0

while i < 50:
    if vetor_dados[i] == 6:
        total_face_6 += 1
    i += 1

#calculo  percentual
percentual = (total_face_6 / 50) * 100

# Exibindo Resultados
print(f"Resultados dos lançamentos: {vetor_dados}")
print("-" * 30)
print(f"A face 6 apareceu {total_face_6} vezes.")
print(f"Percentual de ocorrências: {percentual}%")
