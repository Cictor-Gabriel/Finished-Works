#VICTOR GABRIEL PEDROSA - LADO CLIENTE 

import socket
import string
import threading

def main():
    HOST = '192.168.1.8' # Endereco IP do Servidor
    PORT = 5000 # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    print ('\n...Para sair digite <byebye>...\n')
    passw = ()

    try:
        udp.connect((dest))
    
    except:
        return print("Não foi possível conectar.....")

    username = input('Usuário> ')

    print('\nConectado')

    thread1 = threading.Thread(target=recebermsg, args=[udp])
    thread2 = threading.Thread(target=enviarmsg, args=[udp, username])

    thread1.start()
    
    print("\nseja educado e digite <hello> para continuar\n")
    while True:
        if passw != 'hello':
            print("\nPor favor, digite <hello> para habilitar o chat\n")
            passw = input("--> ")
            
        else:
            
            thread2.start()
            break

            

def recebermsg (udp):
    while True:
        try: 
            
            msg = udp.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            print("\n...Desconectado...")
            udp.close()
            break



    
        

def enviarmsg (udp, username):
    while True:
        try:
                
                msg = input("\n")
                
                if msg != 'byebye':
                    msg = udp.send(f'<{username}> {msg}'.encode('utf-8'))
                else:
                    udp.close()
                    break
        except:
            return


main()
