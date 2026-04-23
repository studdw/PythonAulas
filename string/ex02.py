espaco = " "
while True:
    s = str(input("Escreva UMA palavra:"))
    s = s.strip()

    if espaco in s:
        print("Eu disse apenas uma palavra")
        continue
    else:
        stamanho = 0
        while stamanho < len(s):
            print(s[stamanho], end=" ")  # imprime na mesma linha com espaço
            stamanho += 1
        break

