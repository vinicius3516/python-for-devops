# Estudando sobre Loops em Python
# No python temos dois tipos de loops: for e while

# Loop For
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outros objetos iteráveis.
# A sintaxe básica do loop for é a seguinte:
# for item in sequencia:
#     # faça algo com o item

# Exemplo de uso de loop for em DevOps:
for i in range(5):
    print(i)    # Imprime os números de 0 a 4

# Loop While
# O loop while é usado para executar um bloco de código enquanto uma condição for verdadeira.
# A sintaxe básica do loop while é a seguinte:
# while condicao:
#     # faça algo
#     # se a condição for verdadeira, o bloco de código será executado novamente

# Exemplo de uso de loop while em DevOps:
i = 0
while i < 5:
    print(i)    # Imprime os números de 0 a 4
    i += 1

# Ambos os loops são úteis em diferentes situações. O loop for é mais adequado para iterar sobre uma sequência conhecida, enquanto o loop while é mais adequado para situações em que a condição de parada não é conhecida de antemão.

# Agora vamos praticar com exemplos reais de DevOps:

# Exemplo 1: Usando loop for para iterar sobre uma lista de servidores e verificar o status de cada um
servidores = ['server1', 'server2', 'server3']
for servidor in servidores:                         # Lembrando que 'servicor' é uma variável temporária que recebe cada valor da lista 'servidores' a cada iteração.
    print(f'Verificando status de {servidor}...')
    # Aqui você poderia adicionar código para verificar o status do servidor

# Exemplo 2: Usando loop while para monitorar o uso de CPU até que ele esteja abaixo de um certo limite
uso_cpu = 90  # Suponha que o uso inicial de CPU seja 90%
limite_cpu = 70
while uso_cpu > limite_cpu:
    print(f'Uso de CPU está em {uso_cpu}%. Aguardando para reduzir...')
    uso_cpu -= 5  # Simulando a redução do uso de CPU
print('Uso de CPU está abaixo do limite. Monitoramento encerrado.')



# Entendendo sobre 'contadores' em loops
# Contadores são variáveis que são usadas para contar o número de iterações em um loop.
# Eles são frequentemente usados para controlar o número de vezes que um loop é executado ou para rastrear a posição atual em uma sequência.
# Em Python, você pode usar um contador em um loop for ou while.

# Exemplo de uso de contador em loop for
for i in range(5):  # 'i' é o contador que começa em 0 e vai até 4
    print(f'Iteração número {i}')

# Exemplo de uso de contador em loop while
contador = 0
while contador < 5:
    print(f'Iteração número {contador}')
    contador += 1  # Incrementa o contador em 1 a cada iteração do loop, que seria a mesma coisa que contador = contador + 1



# Complementando

# Agora vamos ver sobre 'break', 'continue', 'pass', 'enumerate' e 'zip' em loops.

# 'break' é usado para sair de um loop antes que ele termine normalmente.
# Ele interrompe a execução do loop e continua com o código após o loop.
# vamos ver um exemplo pratico de uso de 'break' em DevOps:
for i in range(10):
    if i == 5:
        break
    print(i)

#'continue' é usado para pular a iteração atual do loop e continuar com a próxima iteração.
# Ele não interrompe o loop, mas pula o restante do código na iteração atual.
# Exemplo de uso de 'continue' em DevOps:
for i in range(10):
    if i % 2 == 0:  # Se o número for par
        continue  # Pula para a próxima iteração
    print(i)  # Imprime apenas números ímpares

# 'pass' é uma instrução nula em Python. Ela é usada quando você precisa de uma declaração sintática, mas não deseja executar nenhuma ação.
# É útil como um espaço reservado para código futuro.
# Exemplo de uso de 'pass' em DevOps:
for i in range(5):
    if i == 2:
        pass  # Aqui você pode adicionar código mais tarde
    print(i)  # Imprime os números de 0 a 4, mas não faz nada especial quando i é 2

# 'enumerate' é uma função embutida que adiciona um contador a um iterável e retorna pares de índice e valor.
# Isso é útil quando você precisa do índice de cada item enquanto itera sobre uma lista.
# Exemplo de uso de 'enumerate' em DevOps:
servidores = ['server1', 'server2', 'server3']
for indice, servidor in enumerate(servidores):
    print(f'Índice: {indice}, Servidor: {servidor}')
    # Aqui você pode adicionar código para verificar o status do servidor

# 'zip' é uma função embutida que cria uma iteração de tuplas com os elementos correspondentes de duas ou mais iterações.
# Isso é útil quando vocé precisa combinar dados de duas ou mais listas ou tuplas.
# Exemplo de uso de 'zip' em DevOps:
servidores = ['server1', 'server2', 'server3']
status = ['ativo', 'inativo', 'ativo']
for servidor, estado in zip(servidores, status):
    print(f'Servidor: {servidor}, Estado: {estado}')
    # Aqui você pode adicionar código para agir com base no estado do servidor