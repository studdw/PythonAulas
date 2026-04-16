cpf = 497498398
quociente=cpf
i = 2
soma = 0

while quociente != 0:
    digito = quociente %10
    quociente = quociente // 10
    soma += digito * i
    i += 1
    print(soma%11)
