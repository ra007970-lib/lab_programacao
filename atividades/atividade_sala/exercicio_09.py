historico = []

while True:
    valor = float(input("Digite o valor da operação ou 0 para sair. R$ "))
    if valor == 0:
        break
    historico.append(valor)

for i in range(len(historico) -1, -1, -1):
    if abs(historico[i]) < 5.0 and abs(historico[1]):
        del historico[i]

saldo_final = sum(historico)

print("="*50)
print(f"Historico filtrado: {historico}")
print(f"Saldo final do caixa: R$ {saldo_final:.2f}")
