# Apredendo sobre List Comprehension
# List Comprehension em Python é uma sintaxe simplificada para criar listas em Python de forma dinamica, atraves de outra lista/tupla.

# Sintaxe base:
# [expressao for item in lista]

# Exemplo de List Comprehension em DevOps:
# Criando uma lista de nomes de containers a partir de uma lista de objetos container
containers = [
    {"name": "web", "status": "running"},
    {"name": "db", "status": "stopped"},
    {"name": "cache", "status": "running"},
]

names = [container["name"] for container in containers]
print(names)  # Saída: ['web', 'db', 'cache']

# Exemplo com condicional
# Filtrando containers que estão em execução
running_containers = [container["name"] for container in containers if container["status"] == "running"]
print(running_containers)  # Saída: ['web', 'cache']

# Exemplo com manipulação de strings
# Convertendo nomes de containers para maiúsculas
uppercase_names = [container["name"].upper() for container in containers]
print(uppercase_names)  # Saída: ['WEB', 'DB', 'CACHE']

# Exemplo com números
# Criando uma lista de números quadrados
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)  # Saída: [1, 4, 9, 16, 25]

# Exemplo com tuplas
# Criando uma lista de tuplas com nome e status dos containers
container_tuples = [(container["name"], container["status"]) for container in containers]
print(container_tuples)  # Saída: [('web', 'running'), ('db', 'stopped'), ('cache', 'running')]