grupo = ("México", "Republica Tcheca", "Coréia do Sul", "África do Sul")

def confrontos(grupo):
    for i in range(len(grupo)):
        for j in range(i + 1, len(grupo)):
            print(f"{grupo[i]} X {grupo[j]}")

confrontos(grupo)