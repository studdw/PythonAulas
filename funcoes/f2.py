def media_notas(notas):

    if len(notas) == 0:
        return "Lista vazia"

    soma = sum(notas)

    return soma / len(notas)

print(media_notas([7, 8, 10]))