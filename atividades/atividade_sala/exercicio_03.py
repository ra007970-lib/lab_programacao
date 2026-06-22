palavra = input("Digite uma palvra: ").lower()
contador_vogais = 0

for letra in palavra:
    if letra in "aeiou":
        contador_vogais += 1

print(f"A palvra {palavra} contém {contador_vogais} vogais.")
