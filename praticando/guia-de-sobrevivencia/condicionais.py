# Estudando sobre condicionais em Python
# Condificionales são estruturas de controle que permitem executar diferentes blocos de código com base em condições específicas.

# A sintaxe básica de uma condicional em Python é a seguinte:

# if <condição>:  # Se a condição for verdadeira, o bloco de código será executado.
#     <bloco de código>
# elif <condição>: # Se a condição anterior for falsa e essa for verdadeira, este bloco será executado.
#     <bloco de código>
# else:           # Se todas as condições anteriores forem falsas, este bloco será executado.
#     <bloco de código>

# Exemplo de uso de condicionais em DevOps:
status = "erro"

if status == "sucesso":
    print("A operação foi bem-sucedida.")
elif status == "aviso":
    print("A operação foi concluída com um aviso.")
else:
    print("A operação falhou. Verifique os logs para mais detalhes.")

# Operações lógicas também podem ser usadas para combinar condições:
# and (e), or (ou) e not (não) são operadores lógicos que permitem combinar condições de forma mais complexa.
# Exemplo de uso de operadores lógicos em DevOps:
instance_type = "t2.micro"
size = 20

if instance_type == "t2.micro" and size >= 20:
    print("A instância é do tipo t2.micro e tem tamanho suficiente.")
elif instance_type == "t2.micro" or size >= 40:
    print("A instância é do tipo t2.micro ou tem tamanho suficiente.")
else:
    print("A instância não atende aos critérios.")


# Agora, vamos ver sobre os operadores como ==, !=, <, >, <=, >=.
# Esses operadores são usados para comparar valores e determinar a relação entre eles.

# '==': verifica se dois valores são iguais.
# '!=': verifica se dois valores são diferentes.
# '<': verifica se um valor é menor que outro.
# '>': verifica se um valor é maior que outro.
# '<=': verifica se um valor é menor ou igual a outro.
# '>=': verifica se um valor é maior ou igual a outro.

# Exemplo de uso de operadores de comparação em DevOps:
cpu_usage = 75

if cpu_usage > 80:
    print("Uso de CPU alto. Considere otimizar a aplicação.")
elif cpu_usage < 20:
    print("Uso de CPU baixo. A aplicação pode estar ociosa.")
elif cpu_usage == 50:
    print("Uso de CPU estável. A aplicação está funcionando normalmente.")
