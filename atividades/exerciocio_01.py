#Entreda de dados
print("Informe as corrosdenadas da primeira força (F1)")
f1 = []
f1.append(float(input("F1 - x: ")))
f1.append(float(input("F1 - y: ")))
f1.append(float(input("F1 - z: ")))

print("Informa as coordenadas da segunda força (F2)")
f2 = []
f2.append(float(input("F2 - x:  ")))
f2.append(float(input("F2 - y:  ")))
f2.append(float(input("F2 - Z:  ")))

rx= f1[0] + f2[0]
ry= f1[1] + f2[1]
rz= f1[2] + f2[2]

forca_resultante = [rx, ry, rz]

print("**"*30)
print(f"A forca resultante em 3d é: {forca_resultante}")

print(f"Componemtes idividuais: X = {rx}, Y = {ry}, Z = {rz} !")

print("**"*30)