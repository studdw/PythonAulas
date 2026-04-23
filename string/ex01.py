espaco = " "
while True:
    s = str(input("Escreva UMA palavra:"))
    s = s.strip()

    if espaco in s:
        print("Eu disse apenas uma palavra")
        continue
    else:
        upper = s.upper()
        print(upper)
        break