def eh_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):

        if numero % i == 0:
            return False

    return True


def filtrar_primos(lista):

    primos = []

    for numero in lista:

        if eh_primo(numero):
            primos.append(numero)

    return primos


print(filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))