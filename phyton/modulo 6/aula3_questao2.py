# 2) Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.

# URLs: ["www.google.com&quot;, "www.gmail.com&quot;, "www.github.com&quot;, "www.reddit.com&quot;, "www.yahoo.com&quot;]
# dominios:  ["google", "gmail", "github", "reddit", "yahoo"]
# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista vazia para armazenar os domínios
dominios = []

# Extrai o nome do domínio principal de cada URL
for url in urls:
    dominio = url[4:-4]  # Remove os primeiros 4 caracteres 'www.' e os últimos 4 caracteres '.com'
    dominios.append(dominio)

# Imprime a lista de domínios
print("Domínios:", dominios)