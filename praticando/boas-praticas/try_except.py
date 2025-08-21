# # Estudando sobre Tratamentos de Erro com Try Except
# # O try-except em Python é uma estrutura de controle que permite lidar com erros ou exceções durante a execução de um programa.
# # O bloco try contem o código que pode gerar uma exceção, enquanto o bloco except contem o código que deve ser executado em caso de uma exceção ser levantada.

# Exemplo de uso de try-except em DevOps:
try:                                            # Aqui chamamos o try para tentar executar o codigo abaixo
    with open('arquivo.txt', 'r') as f:         # Aqui abrimos o arquivo e o 'r' significa que estamos apenas lendo o arquivo e o as f significa que estamos usando o arquivo como um file object
        conteudo = f.read()                     # Aqui estamos lendo o conteudo do arquivo
        print(conteudo)                         # Aqui estamos printando o conteudo do arquivo
except FileNotFoundError:                       # Aqui estamos tratando o erro de arquivo nao encontrado
    print("Arquivo nao encontrado.")            # Aqui estamos printando uma mensagem de erro para o usuario final



# Exemplo de uso de try-except em DevOps:
import requests

try:
    resposta = requests.get("https://meu-servidor.dev/health")
    print("Status:", resposta.status_code)
except requests.ConnectionError:
    print("Erro: Não foi possível conectar ao servidor.")