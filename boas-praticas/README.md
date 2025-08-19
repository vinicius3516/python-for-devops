# Boas praticas em Python

&nbsp;
<details>
<summary class="summary">Sumário</summary>

- [Virtual Environment (venv)](#virtual-environment-venv)
- [Operador `in` em Python](#operador-in-em-python)
</details>

## Virtual Environment (venv)

> ### O que é e por que usar?

Um **Virtual Environment (venv)** é um recurso fundamental em Python para manter **isolamento de dependências**.

Em projetos diferentes, pode ser que você precise de versões diferentes da mesma biblioteca. Se você instalar tudo no sistema principal, logo vai ter conflitos.

Com o `venv`, cada projeto tem seu próprio “mini-ambiente Python”, contendo apenas o que ele realmente precisa.

No mundo de **DevOps** e desenvolvimento de aplicações, isso é ainda mais importante porque:

- Garante **reprodutibilidade** (o que roda na sua máquina, roda no servidor).
- Evita **conflitos de dependências** entre projetos.
- Facilita a **portabilidade** do código.

> ### Criando um Virtual Environment

O comando básico é:

```bash
python3 -m venv venv
```

Aqui estamos criando uma pasta chamada `venv` (ou `.venv`, como alguns preferem para deixar escondida).

Essa pasta vai conter todo o ambiente isolado com suas próprias dependências.

> ### Ativando o Virtual Environment

No Linux/macOS:

```bash
source venv/bin/activate
```

No Windows (PowerShell):

```powershell
.\venv\Scripts\activate
```

Ao ativar, o **prompt do terminal muda**, mostrando que você está “dentro” do ambiente virtual.

> ### Desativando o Virtual Environment

Quando terminar de trabalhar:

```bash
deactivate
```

Isso retorna você ao ambiente global do sistema.

> ### Exemplo prático em DevOps

Imagine que você está configurando um **script de automação de deploy**.

- No projeto A, você precisa do `boto3==1.20.0` (para AWS).
- No projeto B, você precisa do `boto3==1.28.0`.

Sem o `venv`, isso seria um problema, porque só poderia ter uma versão instalada no sistema.

Com o `venv`, cada projeto tem a sua versão isolada e ambos funcionam perfeitamente.

> ### Boas Práticas

- Sempre use **`.venv/`** ou **`venv/`** dentro do projeto.
- Adicione o diretório `venv/` no **`.gitignore`**, para não versionar o ambiente.
- Gere um **`requirements.txt`** para documentar e replicar as dependências:

```bash
pip freeze > requirements.txt
```

E depois, em outra máquina/servidor:

```bash
pip install -r requirements.txt
```

&nbsp;

## Operador `in` em Python

> ### O que é o operador `in`?

O **operador `in`** é uma forma simples e elegante de verificar se um elemento está presente dentro de uma **sequência** (listas, tuplas, strings, conjuntos, dicionários).

Ele retorna um valor **booleano**:

- `True` → se o elemento está presente.
- `False` → se o elemento não está presente.

Essa é uma forma muito mais **limpa, legível e eficiente** do que percorrer manualmente a sequência.

> ### Exemplo prático com listas

```python
servers = ["server1", "server2", "server3"]

if "server1" in servers:
    print("O servidor server1 foi encontrado na lista de servidores.")

```

Aqui, em apenas **uma linha**, verificamos se `"server1"` está na lista `servers`.

---

> ### Forma manual (não recomendada)

```python
servers = ["server1", "server2", "server3"]

for server in servers:
    if server == "server1":
        print("O servidor server1 foi encontrado na lista de servidores.")

```

Esse código faz a mesma coisa, mas de forma **mais verbosa** e **menos legível**.

> ### Uso em DevOps

O operador `in` é bastante útil em cenários de automação e infraestrutura. Por exemplo:

- **Verificar se um servidor está ativo em uma lista de inventário:**

```python
inventory = ["app01", "db01", "cache01"]

if "db01" in inventory:
    print("Servidor de banco de dados localizado no inventário.")

```

- **Checar se um pacote já está na lista de dependências:**

```python
requirements = ["flask", "boto3", "requests"]

if "boto3" in requirements:
    print("Dependência boto3 já está instalada.")

```

- **Monitorar serviços:**

```python
running_services = ["nginx", "redis", "docker"]

if "nginx" in running_services:
    print("O Nginx está em execução!")

```

---

> ### Boas Práticas

- Prefira usar o **`in`** ao invés de laços manuais (`for`) para verificar presença.
- Lembre-se que em **dicionários**, o `in` verifica se a **chave** existe, e não o valor:

```python
config = {"region": "us-east-1", "env": "production"}

print("region" in config)  # True
print("us-east-1" in config)  # False

```

- Para verificar valores em dicionários, use:

```python
"us-east-1" in config.values()

```

---

O operador `in` é simples, mas extremamente poderoso. Ele deixa o código mais **limpo, direto e pythonico**.