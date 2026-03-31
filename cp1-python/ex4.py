#Par e Impar

num = int(input("Quantos numeros deseja digitar? "))

while num > 0:
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        print("Par")
    else:
        print("Impar")
    num -= 1