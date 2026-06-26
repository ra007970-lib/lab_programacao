def verificar_staus(media):
    if media >6:
        return "Aprovado"
    elif media >=4:
        return "Verifiação suplementar"
    else:
        return "Reprovado"

media_aluno = float(input("Digite a média do aluno: "))

status_final = verificar_staus(media_aluno)

print(f"O Status do aluno é: {status_final}")


