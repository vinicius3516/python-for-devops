# Estudando Sobre Unpacking no Python
# Unpacking é um recurso do Python que permite desempacotar valores de listas, tuplas, ou outros iteráveis em variáveis individuais de forma concisa e legível.
# Ao usar unpacking, podemos atribuir os valores individuais a variáveis separadas, facilitando a leitura e manipulação dos dados.

# Exemplo de uso de unpacking em DevOps:
environment_list = ["development", "staging", "production"]
dev, stg, prod = environment_list

print(f"Siglas para os ambientes: dev = {dev}, stg = {stg}, prod = {prod}")


# Exemplo com tuplas
# Desempacotando uma tupla de coordenadas
servers = (
    {"name": "server1", "ip": "192.168.1.1"},
    {"name": "server2", "ip": "192.168.1.2"},
    {"name": "server3", "ip": "192.168.1.3"}
)

for server in servers:
    name, ip = server.values()  # Aqui estamos utilizando o funçao values() para desempacotar os valores do dicionário, esse função nos retornos somente os valores, sem as chaves.
    print(f"Server: {name}, IP: {ip}")

# Exemplo, eliminando o Ip:

for server in servers:  
    name, _ = server.values()  # O underscore (_) é usado para indicar que não precisamos do segundo valor
    # Aqui estamos ignorando o IP, pois não é necessário para este exemplo
    print(f"Server: {name}")

# Exemplo: ignorando mais de um valor
# itens, _, = servers # Isso aqui vai dar um erro, pois estamos tentando ignorar mais de um valor, mas o unpacking só pode ignorar um valor por vez.
# Para ignorar mais de um valor, podemos usar o operador * para capturar os valores
itens, *rest = servers  # Aqui estamos capturando o primeiro valor e ignorando o restante
print(f"Primeiro item: {itens}, Restante: {rest}")

# Pode filtrar pelo primeiro e pelo último valor
first, *_, last = servers  # Aqui estamos capturando o primeiro e o último valor e ignorando o restante
print(f"Primeiro item: {first}, Último item: {last}")

# Exemplo: Agroa vamos utilizar o '**' para desempacotar dicionarios.

# Vamos criar uma função que vai printar esses valores, e vamos passar os paramentros dessa função, utilizando o unpacking.
def print_server_info(name, ip):
    print(f"Server Name: {name}, IP Address: {ip}")

for server in servers: # Lembrando que 'server' esta retornando um dicionário
    print_server_info(**server)  # Aqui estamos desempacotando o dicionário e passando os valores como argumentos nomeados para a função
    # O operador ** desempacota o dicionário, passando as chaves como nomes de parâmetros e os valores como argumentos.