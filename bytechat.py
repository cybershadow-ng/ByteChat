import socket, os

def servidor():
    os.system("clear")
    print("IP PADRÃO: 127.0.0.1")
    ip = input("Digite o IP: ")
    if ip == "":
        ip = "127.0.0.1"
    else:
        ip = ip
    os.system("clear")
    print("IP PADRÃO: 8080")
    port_input = input("Digite a porta: ")
    if port_input == "":
        port = 8080
    else:
        port = int(port_input)

    os.system("clear")
    opc_password = input("Definir senha(Y/n): ")
    if opc_password in ["Y", "y", "Yes", "yes", ""]:
        senha_input = input("\tDigite a senha: ")
        senha_input += "\n"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        os.system("clear")
        print("Esperando conexão..")

        con, client = s.accept()

        os.system("clear")
        titulo = "Chat Local"
        conectado = f"Conectado: {client[0]}:{client[1]}"

        largura = max(len(titulo), len(conectado)) + 4
        topo = "╔" + "═" * largura + "╗"
        meio1 = "║ " + titulo.ljust(largura - 2) + " ║"
        meio2 = "║ " + conectado.ljust(largura - 2) + " ║"
        base = "╚" + "═" * largura + "╝"

        print(topo)
        print(meio1)
        print(meio2)
        print(base)

        con.send("\tDigite a senha: ".encode())
        senha = con.recv(1024)

        if senha.decode() == senha_input:
            while True:
                msg = input("\nYou: ")
                con.send(msg.encode())

                dados = con.recv(1024)
                print(f"   ({client[0]}): {dados.decode()}")
        else:
            s.close()
    elif opc_password in ["N", "n", "No", "no"]:
        os.system("clear")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        print("Esperando conexão..")

        con, client = s.accept()
        os.system("clear")
        titulo = "Chat Local"
        conectado = f"Conectado: {client[0]}:{client[1]}"

        largura = max(len(titulo), len(conectado)) + 4
        topo = "╔" + "═" * largura + "╗"
        meio1 = "║ " + titulo.ljust(largura - 2) + " ║"
        meio2 = "║ " + conectado.ljust(largura - 2) + " ║"
        base = "╚" + "═" * largura + "╝"

        print(topo)
        print(meio1)
        print(meio2)
        print(base)

        while True:
            msg = input("\nYou: ")
            con.send(msg.encode())

            dados = con.recv(1024)
            print(f"   ({client[0]}]: {dados.decode()}")


def client():
    os.system("clear")
    ip = input("Digite o IP: ")
    if ip == "":
        ip = "127.0.0.1"
    else:
        ip = ip
    os.system("clear")
    port_input = input("Digite a porta: ")

    if port_input == "":
        port = 8080
    else:
        port = int(port_input)

    os.system("clear")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
    except ConnectionRefusedError:
        print(
            "Ops! Não conseguimos conectar. Confira se o servidor está em execução e tente novamente."
        )
        exit()
    opc_security = input(
        "Autenticação por senha está habilitada neste servidor? (y/n): "
    )
    if opc_security in ["Y", "y", "Yes", "yes"]:
        msg = s.recv(1024).decode()
        senha = input(msg)
        senha += "\n"
        s.send(senha.encode())
        os.system("clear")
        print("╔═════════════════════════════════╗")
        print("║         Seja Bem-Vindo!         ║")
        print("╚═════════════════════════════════╝")

        while True:
            print(f"\nGuest: {s.recv(1024).decode()}")

            msg = input("   You: ")
            s.send(msg.encode())
    elif opc_security in ["N", "n", "No", "no"]:
        os.system("clear")
        print("╔═════════════════════════════════╗")
        print("║         Seja Bem-Vindo!         ║")
        print("╚═════════════════════════════════╝")

        while True:
            print(f"\nGuest: {s.recv(1024).decode()}")

            msg = input("   You: ")
            s.send(msg.encode())


while True:
    os.system("clear")
    print(r"""
   ██████╗██╗  ██╗ █████╗ ████████╗
  ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
  ██║     ███████║███████║   ██║   
  ██║     ██╔══██║██╔══██║   ██║   
  ╚██████╗██║  ██║██║  ██║   ██║   
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

          LOCAL TCP CHAT v1.0
    """)
    print("────────────────────────────────────────")
    print("                MENU")
    print("────────────────────────────────────────")
    print("  1  ▶  Iniciar Servidor")
    print("  2  ▶  Iniciar Cliente")
    print()
    print(" 99  ▶  Encerrar")
    print("────────────────────────────────────────")

    try:
        opc = int(input("Digite uma opção: "))
    except ValueError:
        input("Digite apenas números! Pressione Enter...")
        continue

    if opc == 1:
        servidor()
        break
    elif opc == 2:

        client()
        break
    elif opc == 99:
        os.system("clear")
        exit()
    else:
        input("Esta opção não esta disponível..")
