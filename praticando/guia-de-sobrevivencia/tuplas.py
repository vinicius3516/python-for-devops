# Tecnologias fixas (imutáveis)
stack_base = ("Python", "PostgreSQL", "Docker")

# Tecnologias adicionais (sem duplicação)
tecnologias_usadas = {"Python", "AWS", "Linux"}

print(stack_base)  # Mostra tecnologias principais
print("AWS" in tecnologias_usadas)  # Verifica se AWS está presente

# Adicionando novas tecnologias
tecnologias_usadas.add("Kubernetes")
tecnologias_usadas.add("Docker")  # Não será duplicado

print(tecnologias_usadas)

# Removendo tecnologia
tecnologias_usadas.remove("Linux")
print(tecnologias_usadas)
