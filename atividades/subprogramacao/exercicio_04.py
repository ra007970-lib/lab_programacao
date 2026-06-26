def exibir_cabecalho(texto):
    tamanho = (len(texto))
    print("*" * tamanho)
    print(texto)
    print("*" * tamanho)


frase = input("Digite um pequeno texto: ")
exibir_cabecalho(frase)