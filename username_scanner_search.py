import requests

# lista usada para checar a existencia do usuário em redes sociais
SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}"
}

def usernameCheck(username):
    results = {}
    for site, url in SITES.items():
        profileURL = url.format(username)
        try:
            r = requests.get(profileURL, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            if r.status_code == 200: # checa a existencia da página
                results[site] = profileURL
            elif r.status_code == 404: # pagina nao existe
                results[site] = None
            else:
                results[site] = "418 I'm a teapot" # kkkkkk
        except requests.RequestException as e:
            results[site] = f"Error: {e}"
    return results

print("\n\033[31m!!! USUÁRIOS PODEM NÃO TER RELAÇÃO UM COM OS OUTROS !!!\033[0m\n")

username = input("Informe o nome do usuário: ").strip()
found = usernameCheck(username)

print("\n\033[31m!!! USUÁRIOS PODEM NÃO TER RELAÇÃO UM COM OS OUTROS !!!\033[0m")
print("\nRESULTADOS:")

for site, result in found.items():
    if result and not str(result).startswith("418") and not str(result).startswith("Error"): # imprime o resultado caso a saida não seja invalida
        print(f"{site}: {result}")
    elif result is None:
        print(f"{site}: NÃO ENCONTRADO")
    else:
        print(f"{site}: {result}")
