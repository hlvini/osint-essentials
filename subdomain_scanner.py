import socket
 
domain = input("Informe o domínio: ") 

listDomain = input("Informe o caminho do arquivo da lista de domínos: ")

# Abre o arquivo e lê cada linha como uma lista
with open(listDomain, "r") as f:
    subdomain = f.read().splitlines() 

# Laço loop para navegar cada subdomínio
for sub in subdomain:
    subdomainFinder = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(subdomainFinder)
        print(f"[DETECTADO] {subdomainFinder} -> {ip}")
    except socket.gaierror:
        pass
