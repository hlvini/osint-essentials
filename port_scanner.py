from socket import * 

def scanConnection(trgtHost, trgtPort): # Host alvo, porta alvo
    try:
        connect_sock = socket(AF_INET, SOCK_STREAM) # af_inet representa familia de endereco e protocolos, sock stream representa tipo de socket
        connect_sock.connect(trgtHost, trgtPort)
        print('[+]%d/tcp aberto'% trgtPort)  
        connect_sock.close()
    except:
        print('[-]%d/tcp fechado'% trgtPort)

def scanPort(trgtHost, trgtPorts):
    try:
        trgtIP = gethostbyname(trgtHost)
    except:
        print('[-] Não foi possível resolver %s '% trgtHost) 
        return
    try: 
        trgtName = gethostbyaddr(trgtIP)
        print('\n[+] Resultado do scan de: %s '% trgtName[0])
    except:
        print('\n[+] Resultado do scan de: %d '% trgtIP)
    setdefaulttimeout(1)
    for trgtPort in trgtPorts:
        print("Escaneando: %d"% trgtPort)
        scanConnection(trgtHost, int(trgtPort))
 
scanPort('example.com', [80,22]) # Input IP/hostname como primeiro arg. & porta como segundo arg.
