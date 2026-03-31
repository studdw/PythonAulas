# Descontos e fretes

def valor_frete(total_compras): 
    if total_compras<200:
        return 25.0
    else:
        return 0.0

total_compras = float(input("Digite o valor total das compras: "))
fidelidade = int(input("""Qual o seu nível de fidelidade
(1) - Cliente comum
(2) - Cliente VIP
(3) - Cliente Premium
"""))

if fidelidade == 1:
    desconto = 0
    print(f"Seu desconto é de {desconto * 100:.0f}%")
    valor_final = total_compras - (total_compras * desconto)
    frete = valor_frete(valor_final)
    print(f"Frete: R${frete:.2f}")
    print(f"O valor total a pagar é R${valor_final + frete:.2f}")

elif fidelidade == 2:
    if total_compras >= 100:
        desconto = 0.05
        valor_final = total_compras - (total_compras * desconto)
        frete = valor_frete(valor_final)
        print(f"Seu desconto é de {desconto * 100:.0f}%")
        print(f"Frete: R${frete:.2f}")
        print(f"O valor total a pagar é R${valor_final + frete:.2f}")
    else:
        desconto = 0
        valor_final = total_compras - (total_compras * desconto)
        frete = valor_frete(valor_final)
        print(f"Seu desconto é de {desconto * 100:.0f}%")
        print(f"Frete: R${frete:.2f}")
        print(f"O valor total a pagar é R${valor_final + frete:.2f}")

elif fidelidade == 3:
    if total_compras >= 500:
        desconto = 0.15
        valor_final = total_compras - (total_compras * desconto)
        frete = valor_frete(valor_final)
        print(f"Seu desconto é de {desconto * 100:.0f}%")
        print(f"Frete: R${frete:.2f}")
        print(f"O valor total a pagar é R${valor_final + frete:.2f}")
    else:
        desconto = 0.1
        valor_final = total_compras - (total_compras * desconto)
        frete = valor_frete(valor_final)
        print(f"Seu desconto é de {desconto * 100:.0f}%")
        print(f"Frete: R${frete:.2f}")
        print(f"O valor total a pagar é R${valor_final + frete:.2f}")

else:
    print("Nível de fidelidade inválido!")
    desconto = 0
    print("Tente novamente!")


