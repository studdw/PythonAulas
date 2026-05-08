grupo = ("México", "Republica Tcheca", "Coréia do Sul", "África do Sul")

def confrontos(grupo):
    for i in range(len(grupo)):
        for j in range(i + 1, len(grupo)):
            print(f"{grupo[i]} X {grupo[j]}")

confrontos(grupo)

print("\n=========================================")
print("=========================================\n")

grupo = ("México", "Republica Tcheca", "Coréia do Sul", "África do Sul")
def confronto(grupo):
    resp = (f"{grupo[0]} X {grupo[1]}",
            f"{grupo[0]} X {grupo[2]},"
            f"{grupo[0]} X {grupo[3]}",
            f"{grupo[1]} X {grupo[2]}",
            f"{grupo[1]} X {grupo[3]}",
            f"{grupo[2]} X {grupo[3]}")
    return resp

print(confronto(grupo))