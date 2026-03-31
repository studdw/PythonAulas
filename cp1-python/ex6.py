#Plano Cartesiano

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante")
elif x == 0 and y == 0:
    print("O ponto está na origem")
elif x == 0:
    print("O ponto está sobre o eixo y")
elif y == 0:
    print("O ponto está sobre o eixo x")