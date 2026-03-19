salario = float(input("Qual o seu salário atua? "))

if salario <= 1621:
    aliquota = salario*7.5/100
    print(salario - aliquota)

elif 1621 < salario <= 2902.85:
    aliquota = 1621 * 7.5/100 #Valor da primeira faixa (121,58)
    salariox = salario - 1621 #Valor do salario diante a segunda faixa
    aliquota2 = salariox*9/100 #Valor da segunda faixa (x)
    print(f"""O valor dos descontos ficaram assim|
Faixa 1 = {aliquota}
Faixa 2 = {aliquota2}
Ficando com um valor total de descontos de {aliquota + aliquota2:.2f}
Seu salario ficou de: {salario - (aliquota+aliquota2):.2f}""")

elif 2902.85 < salario <= 4354.27:
    aliquota = 1621 * 7.5/100 #Valor da primeira faixa (121,58)
    aliquota2 = 1281.83*9/100 #Valor da segunda faixa (115,37)
    salariox = salario-2902.85 # Valor do salario diante a terceira faixa
    aliquota3 = salariox * 12/100 # Valor da terceira faixa (x)
    print(f"""O valor dos descontos ficaram assim|
Faixa 1 = {aliquota}
Faixa 2 = {aliquota2}
Faixa 3 = {aliquota3}
Ficando com um valor total de descontos de {aliquota+aliquota2+aliquota3:.2f}
Seu salario ficou de: {salario - (aliquota+aliquota2+aliquota3):.2f}""")

elif 4354.27 < salario <= 8475.55:
    aliquota = 1621 * 7.5/100 #Valor da primeira faixa (121,58)
    aliquota2 = 1281.83*9/100 #Valor da segunda faixa (115,37)
    aliquota3 = 1451.42*12/100 # Valor da terceira faixa (174,17)
    salariox = salario-4354.27 #Valor do salario diante a quarta faixa
    aliquota4 = salariox *14/100 # Valor da quarta faixa (x)
    print(f"""O valor dos descontos ficaram assim|
Faixa 1 = {aliquota}
Faixa 2 = {aliquota2}
Faixa 3 = {aliquota3}
Faixa 4 = {aliquota4}
Ficando com um valor total de descontos de {aliquota+aliquota2+aliquota3+aliquota4:.2f}
Seu salario ficou de: {salario - (aliquota+aliquota2+aliquota3+aliquota4):.2f}""")

else:
    print("Ainda nao sei fazer a conta")
     

