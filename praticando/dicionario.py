#Praticando com dicionários em Python
pessoa = {
    'nome': 'Gustavo', 
    'sexo': 'M', 
    'idade': 22
}

#Acessando valores no dicionário
print(pessoa)  # Exibe o dicionário completo
print(pessoa['nome'])  # Acessa o valor associado à chave 'nome'
update = pessoa.update({'cidade': 'São Paulo'}) # Adiciona uma nova chave-valor ao dicionário
print(pessoa)  # Exibe o dicionário atualizado
print(f"{pessoa['nome']} tem {pessoa['idade']} anos.")  # Formata e exibe uma string com valores do dicionário
print(pessoa.keys())  # Exibe todas as chaves do dicionário
print(pessoa.values())  # Exibe todos os valores do dicionário
print(pessoa.items())  # Exibe todos os itens (pares chave-valor) do dicionário

# Excluindo um item do dicionário
del pessoa['sexo']  # Remove a chave 'sexo' e seu valor associado
print(pessoa)  # Exibe o dicionário após a remoção
remove = pessoa.pop('idade')  # Remove a chave 'idade' e retorna seu valor
print(pessoa)  # Exibe o dicionário após a remoção

# Trabalhando com uma lista de dicionários
lista_pessoas = [
    {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22},
    {'nome': 'Maria', 'sexo': 'F', 'idade': 25},
    {'nome': 'João', 'sexo': 'M', 'idade': 30}
]

#Acessando valores no dicionário com .get()
print(pessoa.get('nome'))  # Acessa o valor associado à chave 'nome'
print(pessoa.get('cidade', 'Não encontrada'))  # Tenta acessar 'cidade', retorna 'Não encontrada' se não existir
print(pessoa.get('idade', 0))


#Iteração eficiente: use .items() em loops para trabalhar com chave e valor ao mesmo tempo.
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")