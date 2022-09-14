#SERVER SIDE

import threading
import socket

clientes = []

def main():

    udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostbyname(socket.gethostname()) # Endereco IP do Servidor
    PORT = 5000 # Porta que o Servidor esta
    orig = (HOST, PORT)
    try:
        udp.bind(orig)
        udp.listen()
    except:
        return print("n vai da n parceiro")

    while True:
        cliente, addr = udp.accept()
        print("Conexão recebida de", addr)
        clientes.append(cliente)
 
        thread = threading.Thread(target=gerencmsg, args=[cliente])
        thread.start()

def gerencmsg(cliente):
    while True:
        try:
            msg = cliente.recv(1024)
            transmicao(msg, cliente)
        except:
            excluircliente(cliente)
            break

def transmicao(msg, cliente):
    for numcliente in clientes:
        if numcliente != cliente:
            try:
                numcliente.send(msg)
            except:
                excluircliente(cliente)

def excluircliente(cliente):
    clientes.remove(cliente)







main()