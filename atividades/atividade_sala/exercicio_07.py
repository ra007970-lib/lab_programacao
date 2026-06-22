pares = []
impares = []

print("Digite 10 números diferentes:")

while len(pares) + len(impares) < 10 :
    num = int(input("Digite um número: "))
    if num in pares or num in impares:
        print("Esse número ja foi digitado! Tente outro.")
        continue
    else:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")