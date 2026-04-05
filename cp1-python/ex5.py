print("""
1 - Candidato A
2 - Candidato B
3 - Voto nulo
4 - Voto em branco
0 - Encerrar votação
==================================================""")

total1 = 0
total2 = 0
total3 = 0
total4 = 0

voto = int(input("Digite seu voto: "))

while voto != 0:
    if voto == 1:
        print("Voto para o candidato A")
        total1 += 1
    elif voto == 2:
        print("Voto para o candidato B")
        total2 += 1
    elif voto == 3:
        print("Voto nulo")
        total3 += 1
    elif voto == 4:
        print("Voto em branco")
        total4 += 1
    else:
        print("Voto inválido!")

    voto = int(input("Digite seu voto: "))

print(f"""
Candidato A: {total1}
Candidato B: {total2}
Votos nulos: {total3}
Votos em branco: {total4}
""")