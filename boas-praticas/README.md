# Boas praticas em Python

&nbsp;
<details>
<summary class="summary">Sumário</summary>

- [Virtual Environment (venv)](#virtual-environment-venv)
- [Operador `in` em Python](#operador-in-em-python)
- [Ordem dos Imports em Python](#ordem-dos-imports-em-python)
- [Tratamento de Erros em Python](#tratamento-de-erros-em-python)
- [Type Hints em Python](#type-hints-em-python)
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

&nbsp;

## Ordem dos Imports em Python

> ### Por que a ordem dos imports importa?

A ordem em que você organiza seus **imports** no Python pode parecer detalhe, mas na prática:

- **Melhora a legibilidade** do código.
- **Facilita a manutenção** e revisão por outros desenvolvedores.
- Evita **conflitos** ou confusões entre bibliotecas internas, externas e módulos locais.
- Segue padrões reconhecidos pela comunidade, como o **PEP 8**.

---

> ### Ordem recomendada

A ordem geralmente usada (e recomendada pelo **PEP 8**) é:

1. **Módulos da biblioteca padrão (Python nativo)**
    
    Importados primeiro.
    
    ```python
    import sys
    import os
    import math
    import random
    import datetime
    import time
    ```
    
2. **Módulos de terceiros (instalados via pip, conda, etc.)**
    
    Importados depois.
    
    ```python
    import requests
    import numpy
    import pandas
    import matplotlib
    import seaborn
    import scipy
    ```
    
3. **Módulos locais (código do próprio projeto)**
    
    Importados por último.
    
    ```python
    import utils
    import models
    ```
    

---

> ### Ordem alfabética

Além dessa separação por **categoria**, é boa prática organizar os imports de cada grupo em **ordem alfabética**.

Isso facilita localizar rapidamente um módulo, evita duplicidade e melhora a consistência.

Exemplo:

```python
# Correto
import datetime
import math
import os
import random
import sys
import time
```

---

> ### O que evitar

- Imports desorganizados ou misturados:
    
    ```python
    import requests
    import os
    import pandas
    import math
    import utils
    import numpy
    ```
    
- Imports duplicados.
- Imports desnecessários (importar algo que não é usado no código).

---

> ### Dicas práticas

- Use ferramentas como **isort** ou **black** para formatar automaticamente os imports.
    
    ```bash
    pip install isort black
    isort meu_arquivo.py
    black meu_arquivo.py
    ```
    
- Isso garante que a equipe mantenha um padrão consistente.

---

> ### Resumindo

1. Primeiro **biblioteca padrão**.
2. Depois **módulos de terceiros**.
3. Por último, **módulos locais**.
4. Sempre em **ordem alfabética dentro de cada grupo**.

Assim, seu código fica **mais limpo, legível e pythonico** .

&nbsp;

## Tratamento de Erros em Python

> ### O que é tratamento de erros?

Em Python, o tratamento de erros é feito com a estrutura **try-except**.

Ela permite capturar exceções (erros que ocorrem durante a execução) e tratá-las de forma controlada, evitando que o programa quebre inesperadamente.

Isso é essencial em ambientes DevOps, onde scripts e automações precisam ser resilientes, mesmo quando encontram problemas.

---

> ### Estrutura básica

```python
try:
    # Código que pode gerar erro
except TipoDeErro:
    # Código a executar se o erro ocorrer
```

Podemos ter vários `except` para tratar diferentes tipos de erro.

---

> ### Exemplo prático (DevOps)

```python
try:
    with open('arquivo.txt', 'r') as f:
        conteudo = f.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo nao encontrado.")
```

> ### Explicação passo a passo

1. **try** → executa o código que pode falhar (abrir o arquivo).
2. **with open('arquivo.txt', 'r') as f** → tenta abrir o arquivo no modo leitura (`'r'`).
3. **conteudo = f.read()** → lê o conteúdo do arquivo.
4. **except FileNotFoundError** → se o arquivo não existir, o erro é capturado.
5. **print("Arquivo nao encontrado.")** → mensagem amigável para o usuário.

Sem o `try-except`, esse código quebraria e interromperia a execução do script.

---

> ### Outros exemplos úteis

1. Tratando múltiplos erros

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
```

2. Uso com rede (DevOps real)

```python
import requests

try:
    resposta = requests.get("https://meu-servidor.dev/health")
    print("Status:", resposta.status_code)
except requests.ConnectionError:
    print("Erro: Não foi possível conectar ao servidor.")
```

---

> ### O que evitar

- Usar `except:` sem especificar o tipo de erro → captura tudo e pode esconder problemas graves.
- Não tratar exceções → o programa quebra e impacta pipelines, automações ou serviços.

---

> ### Dicas práticas

- Sempre trate exceções específicas primeiro (ex.: `FileNotFoundError`, `ZeroDivisionError`).
- Use `Exception as e` apenas para capturar erros genéricos e logar a causa.
- Em scripts DevOps, combine `try-except` com logs para facilitar troubleshooting.

---

> ### Resumindo

1. **try-except** permite capturar e tratar erros.
2. Evita que o programa quebre inesperadamente.
3. Use exceções específicas sempre que possível.
4. É fundamental em automações DevOps para criar scripts mais **seguros e resilientes**.

&nbsp;

## Type Hints em Python


> ### O que são Type Hints?

**Type Hints** (anotações de tipo) são uma forma de indicar, de maneira explícita, quais tipos de dados uma função **espera receber** e **retorna**.

Eles não mudam a execução do Python (que é uma linguagem dinamicamente tipada), mas ajudam na **legibilidade, manutenção e qualidade do código**.

Além disso, são extremamente úteis em **IDEs** (como VSCode, PyCharm) e em ferramentas de análise estática (como `mypy`), que conseguem detectar erros antes mesmo da execução.

---

> ### Sintaxe básica

```python
def nome_funcao(parametro: tipo) -> tipo_retorno:
    ...
```

- `parametro: tipo` → define o tipo esperado do parâmetro.
- `> tipo_retorno` → define o tipo de dado que será retornado pela função.

---

> ### Exemplo prático (DevOps)

```python
def servidor_ativo(nome: str) -> bool:
    servidores_ativos = ["web01", "db01", "cache01"]
    return nome in servidores_ativos

print(servidor_ativo("web01"))   # True
print(servidor_ativo("worker"))  # False
```

Explicação

- `nome: str` → o parâmetro `nome` deve ser uma string.
- `> bool` → a função sempre retorna um valor booleano (`True` ou `False`).
- Isso deixa claro o contrato da função: **entrada string → saída booleano**.

---

> ### Exemplos variados

### 1. Função com múltiplos parâmetros

```python
def soma(a: int, b: int) -> int:
    return a + b
```

### 2. Função que retorna nada (`None`)

```python
def log_evento(evento: str) -> None:
    print(f"Evento registrado: {evento}")
```

### 3. Uso com listas e dicionários

```python
from typing import List, Dict

def listar_containers(containers: List[Dict[str, str]]) -> List[str]:
    return [c["name"] for c in containers]
```

---

> ### O que evitar

- Não usar **type hints inconsistentes** (ex.: declarar `int` mas retornar `str`).
- Usar type hints apenas "por obrigação" sem seguir padrões.

---

> ### Dicas práticas

- Sempre use **type hints** em funções públicas (expostas em libs, APIs ou automações).
- Combine type hints com ferramentas de análise estática como `mypy`.
- Prefira `Optional[tipo]` quando o parâmetro pode ser `None`.
- Em projetos grandes de DevOps, ajuda a reduzir erros em automações complexas.

---

> ### Resumindo

1. **Type Hints** tornam o código mais claro, legível e confiável.
2. São úteis para IDEs, linters e análise estática.
3. Boas práticas → use em funções públicas, declare entrada e saída.
4. Muito valioso em projetos DevOps que envolvem automações críticas.