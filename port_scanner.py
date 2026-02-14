from socket import * 

def scanConnection(trgtHost, trgtPort): # Host alvo, porta alvo
    try:
        connect_sock = socket(AF_INET, SOCK_STREAM) # af_inet representa familia de endereco e protocolos, sock stream representa tipo de socket
        connect_sock.connect(trgtHost, trgtPort)
        print('%d/tcp open'% trgtPort)  
        connect_sock.close()
    except:
        print('%d/tcp closed'% trgtPort)

def scanPort(trgtHost, trgtPorts):
    try:
        trgtIP = gethostbyname(trgtHost)
    except:
        print('ERROR: COULD NOT RESOLVE %s '% trgtHost) 
        return
    try: 
        trgtName = gethostbyaddr(trgtIP)
        print('\nSCAN RESULT: %s '% trgtName[0])
    except:
        print('\nSCAN RESULT: %d '% trgtIP)
    setdefaulttimeout(1)
    for trgtPort in trgtPorts:
        print("SCANNING: %d"% trgtPort)
        scanConnection(trgtHost, int(trgtPort))
 
scanPort('example.com', [80,22]) # Input IP/hostname como primeiro arg. & porta como segundo arg.
