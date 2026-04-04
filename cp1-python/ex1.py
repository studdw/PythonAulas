# Atividade de calculo de consumo

mes_anterior = float(input("Qual foi o volume mensal do mês anterior(m³)? "))
mes_atual = float(input("Qual foi o volume mensal do atual(m³)? "))

if mes_atual <= 20:
    valor = mes_atual * 2

elif mes_atual > 20 and mes_atual <= 35:
    valor = mes_atual * 3.5

elif mes_atual > 35 and mes_atual <= 50:
    valor = mes_atual * 5.5

else:
    valor = mes_atual * 7

# Regra de desconto ou multa
if mes_atual < mes_anterior:
    desconto = valor * 15 / 100
    total = valor - desconto
    print(f"Desconto: {desconto:.2f}")
else:
    multa = valor * 10 / 100
    total = valor + multa
    print(f"Multa: {multa:.2f}")

print(f"Valor do consumo: {valor:.2f}")
print(f"Total da conta: {total:.2f}")

