num = int(input("Digite um numero: "))
somapar = 0


while num != 0:
    if num % 2 == 0:
        somapar = somapar + num
    num = int(input("Digite um numero: "))

    
print("A soma dos numeros pares é:", somapar)