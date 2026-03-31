# Atividade de calculo de consumo

mes_anterior = float(input("Qual foi o volume mensal do mês anterior(m³)? "))
mes_atual = float(input("Qual foi volume mensal do mês atual(m³)? "))

if mes_atual <= 20:
    if mes_anterior>mes_atual:
        valor = mes_atual * 2
        multa = valor * 10 / 100
        total = valor + multa
        print(f"Sua conta ficou no total de: {total}")
    else:
        valor = mes_atual*2
        desconto = valor * 15/100
        total = valor - desconto
        print(f"Sua conta ficou no total de {total}")


elif mes_atual > 20 and mes_atual<=35:
    if mes_anterior > mes_atual:
        valor = mes_atual * 3.5
        multa = valor * 10/100
        total = valor + multa
        print(f"Sua conta ficou no total de: {total}")
    else:
        valor = mes_atual*3.5
        desconto = valor * 15 / 100
        total = valor - desconto
        print(f"Sua conta ficou no total de {total}")

elif mes_atual > 35 and mes_atual <= 50:
    if mes_anterior > mes_atual:
        valor = mes_atual * 5.5
        multa = valor * 10 / 100
        total = valor + multa
        print(f"Sua conta ficou no total de: {total}")
    else:
        valor = mes_atual*5.5
        desconto = valor * 15 / 100
        total = valor - desconto
        print(f"Sua conta ficou no total de {total}")

else:
    if mes_anterior>mes_atual:
        valor = mes_atual * 7
        multa = valor * 10 / 100
        total = valor + multa
        print(f"Sua conta ficou no total de: {total}")
    else:
        valor = mes_atual*5.5
        desconto = valor * 15 / 100
        total = valor - desconto
        print(f"Sua conta ficou no total de {total}")

