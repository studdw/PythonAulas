num = int(input("Quantos numeros deseja digitar? "))

pares = 0
impares = 0

while num > 0:
    valor = int(input("Digite um numero: "))
    
    if valor % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Impar")
        impares += 1
    
    num -= 1

print(f"Total de pares: {pares}")
print(f"Total de impares: {impares}")