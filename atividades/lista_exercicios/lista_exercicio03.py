lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]

lista_intercalada = []

if len(lista1) <= len(lista2):
    menor = lista1
    maior = lista2
else:
     menor = lista2
     maior = lista1

i = 0
while i < len(menor):
     lista_intercalada.append(menor[i])
     lista_intercalada.append(maior[i])
     i += 1

while i < len(maior):
     lista_intercalada.append(maior[i])
     #lista_intercalada.append(menor[i])
     i += 1

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista intercalada: {lista_intercalada})

    
