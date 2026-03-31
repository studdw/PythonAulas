login = str(input("Login: "))
senha = str(input("Senha: "))

if login == "scott" and senha == "tiger":
    print("Acesso concedido")
elif login == "walt" and senha == "disney":
    print("Acesso concedido")
elif login == "spock" and senha == "ncc1701":
    print("Acesso concedido")
else:
    print("Login ou senha incorreto!")