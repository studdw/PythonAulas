num = int(input("Digite um numero e descubra seus divisores: "))

print(f"Os divisores de {num} são: ")
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i = i + 1
