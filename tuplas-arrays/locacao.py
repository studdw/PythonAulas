from time import sleep

lista_carro = []

print("Seja Bem-Vindo ao sistema de locação de CARROS!!")
print("\n=============================================")
print("=============================================\n")
sleep(0.5)

def menu():
    print("="*40)
    print("\nSISTEMA DE LOCAÇÃO")

    return int(input("""Escolha a opção:
    1 - Cadastrar veículo
    2 - Consultar veículo
    3 - SAIR: 
    """))

def cadastrar():
    print("Vamos cadastrar seu veiculo")
    modelo = input("Escreva modelo do seu carro: ")
    placa = input("Escreva a placa do seu carro: ")
    cor = input("Escreva a cor do seu carro: ")
    ano = int(input("Escreva o ano do seu carro: "))
    lista_carro.append([modelo, placa, cor, ano])

def consultar():
    print("Aqui estão os veiculos disponiveis")
    print(lista_carro)


while True:
    op = menu()
    if op == 1:
        cadastrar()
    elif op == 2:
        consultar()
    elif op ==3:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida")
