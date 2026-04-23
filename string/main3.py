palavra = str(input("Digite uma palavra: ")).upper()
letra = str(input("Digite uma letra: ")).upper()
resultado = ""

for caractere in palavra:
    if caractere == letra:
        resultado += "*"
    else:
        resultado += caractere

print(resultado)