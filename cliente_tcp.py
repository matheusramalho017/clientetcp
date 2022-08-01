import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as erro:
        print("Conexão falhou")
        print("Erro: {}".format(erro))
        sys.exit()

    print("Socket criado com sucesso")
    
    HostAlvo = input("Digite o host ou ip a ser conectado")
    PortaAlvo = input("Digite a porta a ser conectada")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))

        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + "e na Porta: " + PortaAlvo)
        s.shutdown(2)

    except socket.error as erro:
        print("Não foi possivel conectar ao host: " + HostAlvo + "- Port:"  + PortaAlvo)
        print("Erro: {}".format(erro))
        sys.exit()

if __name__ == "__name__":
    main()
