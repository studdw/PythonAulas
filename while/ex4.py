quantidade = int(input("Digite a quantidade de números: "))

positivos = 0
negativos = 0

while quantidade > 0:
    numero = int(input("Digite um número: "))
    quantidade = quantidade - 1
    if numero >0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

print(f"""Quantidade de números positivos: {positivos}
Quantidade de números negativos: {negativos}""")