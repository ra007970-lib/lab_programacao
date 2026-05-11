
vetor = []
contador = 0

#entrada de dados
print("Digite 10 números:")
while contador < 10:
    item = input(f"Valor {contador + 1}: ")
    vetor.append(item)
    contador += 1 

#contando diferentes
unicos = []
indice = 0

while indice < 10:
    valor_atual = vetor[indice]
    ja_existe = False
    cont_indice = 0
    while cont_indice < len(unicos):
        if unicos[cont_indice] == valor_atual:
            ja_existe = True
        cont_indice += 1
        
    if not ja_existe:
        unicos.append(valor_atual)
        
    indice += 1

print(f"\nExistem {len(unicos)} valores diferentes.")
