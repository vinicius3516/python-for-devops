# Estudando Sobre Funcões em Python
# Basicamente, quando o nosso codigo começa a ficar grande, é interessante que a gente comece a pensar em como modularizar ele, ou seja, quebrar ele em pedaços menores. Isso ajuda na organização do código e também na reutilização de código.
# Funções são blocos de código que podem ser reutilizados várias vezes ao longo do programa. Elas podem receber entradas (parâmetros) e retornar saídas (valores).
# Em Python, as funções são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses que podem conter parâmetros.

# Exemplo de função simples.
def saudacao(nome): # Aqui, a função 'saudacao' recebe um parâmetro chamado 'nome'. Nesse caso, esse parametro é obrigatorio.
    return f"Olá, {nome}!"

# Chamando a função e imprimindo o resultado.
print(saudacao("Vinicius"))
# ou, podemos associar o resultado a uma variavel.
mensagem = saudacao("Maria")
print(mensagem)

# Função com múltiplos parâmetros.
def soma(a, b):
    return a + b

# Chamando a função e imprimindo o resultado.
print(soma(5, 3))

# Função com parâmetro padrão.
def potencia(base, expoente=2): # Aqui, o parametro 'expoente' tem um valor padrão de 2. Se não for fornecido, ele será 2.
    return base ** expoente

# Chamando a função com e sem o parâmetro padrão.
print(potencia(4))      # Usa o valor padrão do expoente (2), resultado é 16
print(potencia(4, 3))   # Usa o valor fornecido (3), resultado é 64