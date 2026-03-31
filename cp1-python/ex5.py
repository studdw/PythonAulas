#Urna

print("""
1 - Candidato A
2 - Candidato B
3 - Voto nulo
4 - Voto em branco
0 - Encerrar votação
==================================================""")

voto = int(input("Digite seu voto: "))
total1 = 0
total2 = 0
total3 = 0
total4 = 0

while voto != 0:
    if voto == 1:
        print("Voto para o candidato A")
        total1 += 1
        voto = int(input("Digite seu voto: "))
    elif voto == 2:
        print("Voto para o candidato B")
        total2 += 1
        voto = int(input("Digite seu voto: "))
    elif voto == 3:
        print("Voto nulo")
        total3 += 1
        voto = int(input("Digite seu voto: "))
    elif voto == 4:
        print("Voto em branco")
        total4
        voto
    else:
        print("Voto inválido!")
        voto = int(input("Digite seu voto: "))
    print(f"""O candidato A tem {total1} votos
O candidato B tem {total2} votos
Teve {total3} votos nulos
Teve {total4} votos em branco
""")