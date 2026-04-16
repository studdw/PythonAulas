cpf = int(input("Digite os 9 numeros do seu cpf: "))
quociente = cpf
tamanho = len(str(cpf))

if tamanho == 9:
    while quociente > 0:
        digito = quociente % 10
        quociente = quociente // 10
        print(digito)

else:
    print("Seu texto nao possui 9 digitos")
