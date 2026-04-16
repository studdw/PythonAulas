#cpf = (input("Digite os 11 digitos do seu CPF: "))

#cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
#print(cpf_formatado)

cpf = int(input("Digite os 11 numeros do seu CPF: "))

quociente = cpf
digitos = []

# Extrai os dígitos (de trás pra frente)
while quociente > 0:
    digito = quociente % 10
    digitos.append(digito)
    quociente = quociente // 10

# Garante 11 dígitos (caso tenha zero à esquerda)
while len(digitos) < 11:
    digitos.append(0)

# Inverte para ficar na ordem correta
digitos.reverse()

# Monta o CPF formatado
cpf_formatado = (
    f"{digitos[0]}{digitos[1]}{digitos[2]}."
    f"{digitos[3]}{digitos[4]}{digitos[5]}."
    f"{digitos[6]}{digitos[7]}{digitos[8]}-"
    f"{digitos[9]}{digitos[10]}"
)

print(cpf_formatado)


