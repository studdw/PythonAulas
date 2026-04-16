num = int(input("Digite um numero: "))

n = 1
divisores = 0

while n <= num:
    if num % n == 0:
        print("Divisor =", n)
        divisores = divisores + 1
    n = n + 1

if divisores > 2:
    print(f"O numero {num} não é primo, pois tem {divisores} divisores.")
else:
    print(f"O numero {num} é primo, pois tem apenas 2 divisores.")