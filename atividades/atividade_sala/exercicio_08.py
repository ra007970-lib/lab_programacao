frase = input("Digite uma frase: ")

lista = []
palavra = " "

for i in frase:
    if i != " ":
        palavra += i
    else:
        if palavra != " ":
            lista.append(palavra)
            palavra = " "

if palavra != " ":
    lista.append(palavra)

print(f"A frase em uma lista ficará assim: {lista}")

