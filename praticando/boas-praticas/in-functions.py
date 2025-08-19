# Estudando sobre o operador 'in' do python

# O operador 'in' verifica se um valor está presente em uma sequência, como uma lista, tupla, dicionário ou conjunto.
# Ele retorna True se o valor estiver presente na sequência e False caso contrário.

# Exemplo de uso do operador 'in' em DevOps:
servers = ["server1", "server2", "server3"]

if "server1" in servers:
    print("O servidor server1 foi encontrado na lista de servidores.")


# Ao contrario disso, teriamos que percorrer todas a lista e fazer um verificaçao manualmente.

# Exemplo da forma manual:

servers = ["server1", "server2", "server3"]

for server in servers:
    if server == "server1":
        print("O servidor server1 foi encontrado na lista de servidores.")
