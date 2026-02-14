import socket
 
domain = input("SPECIFY DOMAIN: ") 

listDomain = input("DOMAIN LIST FILE PATH: ")

# Abre o arquivo e lê cada linha como uma lista
with open(listDomain, "r") as f:
    subdomain = f.read().splitlines() 

# Laço loop para navegar cada subdomínio
for sub in subdomain:
    subdomainFinder = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(subdomainFinder)
        print(f"[DETECTED] {subdomainFinder} -> {ip}")
    except socket.gaierror:
        pass
