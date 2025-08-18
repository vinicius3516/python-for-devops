# Guia de Sobrevivência - Python

&nbsp;
<details>
<summary class="summary">Sumário</summary>

- [Linguagem Interpretada vs Linguagem Compilada](#linguagem-interpretada-vs-linguagem-compilada)
- [Shebang](#shebang)
- [Variáveis no Python](#variáveis-no-python)
- [f-strings no Python](#f-strings-no-python)
- [Listas em Python](#listas-em-python)
- [Tuplas e Sets no Python](#tuplas-e-sets-no-python)
- [Dicionários no Python](#dicionários-no-python)
- [Condicionais em Python](#condicionais-em-python)
- [Loops no Python](#loops-no-python)
- [List Comprehensions no Python](#list-comprehensions-no-python)
- [Unpacking no Python](#unpacking-no-python)
- [Funções no Python](#funções-no-python)
</details>


## Linguagem Interpretada vs Linguagem Compilada

> ### O que foi feito nessa aula

Nesta aula, exploramos de forma prática e conceitual a diferença fundamental entre linguagens compiladas e linguagens interpretadas. O foco foi entender como o código é processado, qual o impacto na performance, e como isso influencia no desenvolvimento e deploy em ambientes como containers Docker.

> ### O fluxo de execução para cada tipo ficou claro:

Tipo	Fluxo de Execução
Linguagem Compilada	Código-fonte → Compilador → Binário → Execução
Linguagem Interpretada	Código-fonte → Interpretador → Execução imediata

> ### Fluxo detalhado

#### Compiladas

- Você escreve o código.

- Executa um comando para compilar.

- O compilador gera um binário executável.

- Este binário é então executado, sem necessidade do código-fonte ou interpretador no ambiente final.

#### Interpretadas

- Você escreve o código.

- Executa diretamente, sem passo explícito de compilação.

- O interpretador lê e processa o código linha a linha, retornando a saída em tempo real.

> ### Vantagens e melhores práticas

| Tipo              | Vantagens                                                                             | Pontos de Atenção                                                           |
| ----------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Compiladas**    | Alta performance<br>Binários leves<br>Código protegido (difícil de reverter) | Maior tempo de build<br>Complexidade na configuração de compiladores |
| **Interpretadas** | Desenvolvimento rápido<br>Fácil aprendizado<br>Portabilidade                 | Performance menor<br>Dependências e interpretador no ambiente final   |

&nbsp;

## Shebang

> ### O que foi feito nessa aula

Nesta aula, aprendemos sobre o **Shebang** — uma linha especial no início de scripts que informa ao sistema qual **interpretador** deve ser usado para executá-lo.

O objetivo é garantir que o script seja executado corretamente **independente da sessão atual** ou do terminal em uso.

> ### O que é o Shebang?

O Shebang é uma linha iniciada por `#!` seguida do caminho do interpretador.

Ele **não é uma funcionalidade da linguagem**, mas sim do sistema operacional, geralmente interpretado pelo kernel Unix/Linux.

#### Por que usar?

- Evita que scripts sejam interpretados pelo shell incorreto (por exemplo, Bash tentando interpretar Python).
- Permite executar o script diretamente com `./meuscript` sem precisar chamar o interpretador manualmente.
- Torna o código mais **portável** entre sistemas diferentes.

> ### Exemplo prático

#### Sem Shebang (execução manual):

```bash
python3 script.py
```

#### Com Shebang (execução direta):

```python
#!/usr/bin/env python3
print("teste")
```

```bash
chmod +x script.py  # Permite execução
./script.py
```

O sistema detecta o Shebang e usa automaticamente o `python3`.

> ### Variações comuns de Shebang

| Linguagem | Shebang recomendado | Observação |
| --- | --- | --- |
| Python 3 | `#!/usr/bin/env python3` | Portável, encontra `python3` no PATH |
| Bash | `#!/usr/bin/env bash` | Melhor que `/bin/bash` para compatibilidade |
| Node.js | `#!/usr/bin/env node` | Usado em scripts JS executáveis |
| Perl | `#!/usr/bin/env perl` | Scripts legados e automações |

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar `env` no Shebang | Portabilidade, evita hardcode de caminho fixo |
| Colocar o Shebang na **primeira linha** | Necessário para ser reconhecido pelo sistema |
| Conceder permissão de execução (`chmod +x`) | Permite rodar com `./` |
| Usar interpretador explícito (ex.: `python3`) | Evita problemas com versões diferentes |
| Evitar Shebang desnecessário em módulos Python | Módulos importados não precisam de Shebang |

&nbsp;

## Variáveis no Python

> ### O que foi feito nessa aula

Nesta aula, entendemos **o que são variáveis no Python**, como usá-las para armazenar valores e como o Python trata seus tipos de forma dinâmica.

Em Python, uma variável é um **identificador** que aponta para um valor armazenado na memória. Ao contrário de linguagens tipadas estaticamente, **não precisamos declarar o tipo**: o Python **infere automaticamente** com base no valor atribuído.

> ### Definição básica

```python
nome = "Vinicius"  # String
idade = 26         # Inteiro
altura = 1.82      # Float
```

- **Atribuição:** feita com o operador `=`.
- **Identificador:** o nome da variável.
- **Valor:** o dado armazenado.

> ### Verificando o tipo da variável

Mesmo com tipagem dinâmica, podemos inspecionar o tipo usando a função `type()`:

```python
print(type(nome))   # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura)) # <class 'float'>
```

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar nomes descritivos (`idade_usuario` ao invés de `x`) | Facilita leitura e manutenção |
| Evitar sobrescrever variáveis com outros tipos sem necessidade | Previne erros difíceis de rastrear |
| Centralizar valores configuráveis em constantes ou arquivos de config | Facilita ajustes sem alterar lógica |
| Usar `type()` para depuração | Ajuda a identificar tipos inesperados |
| Seguir convenções de nomenclatura (`snake_case`) | Mantém padrão e legibilidade no time |

&nbsp;

## f-strings no Python

> ### O que foi feito nessa aula

Nesta aula aprendemos sobre **f-strings**, um recurso introduzido no Python 3.6 que permite **interpolação de strings** de forma mais **clara, legível e performática**.

Interpolação significa inserir valores de variáveis ou expressões diretamente dentro de uma string. Antes das f-strings, uma forma comum de fazer isso era com o método `.format()`, mas com f-strings conseguimos o mesmo resultado **com menos código e mais clareza**.

> ### Exemplo de comparação

Usando `.format()`

```python
nome = "Vinicius"
idade = 26
altura = 1.82

print("Hello, my name is {} and I am {} years old. My height is {:.2f} meters."
      .format(nome, idade, altura))
```

Usando `f-strings`

```python
print(f"Hello, my name is {nome} and I am {idade} years old. My height is {altura:.2f} meters.")
```

Mais limpo, direto e fácil de ler.

> ### Recursos das f-strings

- **Interpolar variáveis:** `{variavel}`
- **Formatar números:** `{valor:.2f}` → duas casas decimais
- **Executar expressões:** `{2 + 2}` → `4`
- **Usar métodos:** `{nome.upper()}` → texto em maiúsculas
- **Datas formatadas:** usando `strftime` dentro da f-string

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Preferir f-strings ao `.format()` e concatenação | Código mais legível |
| Usar formatação explícita para números e datas | Saída mais profissional |
| Aproveitar expressões dentro de chaves | Menos variáveis temporárias |
| Evitar f-strings para strings estáticas | Mantém clareza e evita processamento desnecessário |
| Seguir padrões de formatação consistentes no time | Padroniza estilo e legibilidade |

> ### Exemplo realista

**Cenário:** Gerar mensagem personalizada para cliente de e-commerce.

```python
cliente = "Mariana"
pedido = 4523
valor_total = 1299.99
desconto = 0.15

print(f"Olá {cliente}, seu pedido #{pedido} foi confirmado!")
print(f"Valor total com desconto: R$ {valor_total * (1 - desconto):.2f}")
```

Resultado:

```bash
Olá Mariana, seu pedido #4523 foi confirmado!
Valor total com desconto: R$ 1104.99
```

> ### Dicas DevOps

- **Em scripts de automação**, use f-strings para mensagens claras no terminal.
- **Para debug**, insira variáveis e expressões diretamente na saída (`print(f"Debug: {variavel=}")` no Python 3.8+).
- **Padronize logs** com f-strings para evitar concatenação caótica.
- **Em relatórios**, combine f-strings com formatações como `.2f` para números e `%Y-%m-%d` para datas.
- **Performance:** f-strings são mais rápidas que `.format()` e concatenar com `+`.

&nbsp;

## Listas em Python

> ### O que foi feito nessa aula

Nesta aula aprendemos sobre **listas no Python**, que são **estruturas de dados ordenadas e mutáveis**.

Isso significa que:

- **Ordenadas:** os elementos têm uma posição definida (índice), e essa ordem é preservada.
- **Mutáveis:** podemos **adicionar**, **remover** ou **alterar** itens após a criação da lista.

As listas são ideais quando a **ordem dos elementos importa** e precisamos de flexibilidade para modificá-las.

> ### Sintaxe básica

```python
name_list = ['Alice', 'Bob', 'Charlie', 'David']
```

> ### Operações comuns com listas

```python
name_list = ['Alice', 'Bob', 'Charlie', 'David']

print(name_list)        # Exibe toda a lista
print(name_list[0])     # Acessa o primeiro elemento
print(len(name_list))   # Retorna o tamanho da lista
print(name_list[-1])    # Acessa o último elemento
print(name_list[1:3])   # Fatiamento (índice 1 até antes do 3)

name_list.append('Eve')         # Adiciona elemento no final
name_list.remove('Charlie')     # Remove elemento pelo valor
name_list.sort()                # Ordena em ordem alfabética
name_list.reverse()             # Inverte a ordem
name_list.pop(2)                # Remove elemento pelo índice
name_list.insert(0, 'Zara')     # Insere no índice especificado

# --- Mais operações interessantes ---
print("Bob" in name_list)               # Verifica se existe na lista
print(name_list.index("Bob"))           # Retorna o índice do elemento
name_list.extend(['Frank', 'Grace'])    # Adiciona vários elementos
print(name_list.count("Bob"))           # Conta quantas vezes o valor aparece
name_list_copy = name_list.copy()       # Cria uma cópia da lista
del name_list[1]                        # Remove elemento pelo índice usando 'del'

# Lista de números para exemplos numéricos
numbers = [5, 2, 9, 1, 7]
print(min(numbers))   # Menor valor
print(max(numbers))   # Maior valor
print(sum(numbers))   # Soma de todos os elementos
```

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar listas quando a **ordem dos elementos importa** | Garante previsibilidade |
| Preferir métodos embutidos como `.append()`, `.remove()`, `.pop()` | Manipulação simples e direta |
| Usar fatiamento (`lista[inicio:fim]`) para extrair subconjuntos | Código mais limpo |
| Evitar listas gigantes em memória | Previne consumo excessivo de recursos |
| Iterar com `for` para processar elementos | Mais legibilidade e menos erros |

> ### Exemplo realista

**Cenário:** Lista de tarefas com adição, remoção e exibição de tarefas pendentes.

```python
tarefas = ["Backup do servidor", "Atualizar dependências", "Deploy da API"]

# Adicionando nova tarefa
tarefas.append("Verificar logs")

# Removendo tarefa concluída
tarefas.remove("Backup do servidor")

# Exibindo todas as tarefas restantes
print("Tarefas pendentes:")
for t in tarefas:
    print("-", t)

# Mostrando a próxima tarefa (primeira da lista)
print("\nPróxima tarefa:", tarefas[0])

```

Resultado:

```
Tarefas pendentes:
- Atualizar dependências
- Deploy da API
- Verificar logs

Próxima tarefa: Atualizar dependências
```

> ### Dicas DevOps

- **Em scripts de automação**, use listas para guardar caminhos de arquivos a serem processados.
- **Em pipelines CI/CD**, listas podem armazenar etapas dinâmicas de execução.
- **Para manipulação de dados**, combine listas com `for` e `if` para filtros rápidos.
- **Remova elementos com `.remove()` (por valor) ou `.pop()` (por índice)** conforme a necessidade.
- **Para grandes volumes de dados**, considere `deque` do módulo `collections` para performance otimizada.

&nbsp;

## Tuplas e Sets no Python

> ### O que foi feito nessa aula

Nesta aula exploramos **duas estruturas de dados importantes no Python**:

- **Tuplas:** ordenadas e **imutáveis** — ideais para representar dados que não devem ser alterados.
- **Sets (conjuntos):** não ordenados, **sem elementos duplicados** e **mutáveis** (permitem adicionar e remover itens).

> ### Definições

#### **Tupla**

```python
tupla = ("Python", 3.10, True)  # Imutável
print(tupla)
```

- Ordenada
- Não permite alteração de elementos após a criação
- Mais rápida que listas para leitura de dados

#### **Set**

```python
meu_set = {"Python", 3.10, True}  # Sem ordem e sem duplicatas
print(meu_set)
```

- Não ordenado
- Não permite elementos duplicados
- Útil para operações matemáticas de conjuntos

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar **tuplas** para dados fixos | Mantém integridade dos dados |
| Usar **sets** para garantir valores únicos | Evita duplicatas automaticamente |
| Lembrar que **sets não preservam ordem** | Importante ao trabalhar com ordenação |
| Usar `.add()` e `.remove()` para manipular sets | Operações rápidas e eficientes |
| Para verificar existência, use `in` (tanto em tuplas quanto sets) | Operação muito performática |

> ### Exemplo realista

**Cenário:** Controle de tecnologias usadas em um projeto

```python
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
```

Saída exemplo:

```
('Python', 'PostgreSQL', 'Docker')
True
{'Python', 'AWS', 'Linux', 'Kubernetes', 'Docker'}
{'Python', 'AWS', 'Kubernetes', 'Docker'}
```

 >### Dicas DevOps

- **Tuplas** são ótimas para **configurações fixas** de pipelines e ambientes.
- **Sets** são ideais para listas de servidores, usuários ou permissões sem repetição.
- Usar `in` em sets é **mais rápido** que em listas quando há muitos elementos.
- Sets são perfeitos para **operações matemáticas** como união (`|`), interseção (`&`) e diferença ().
- Para converter listas em sets e remover duplicatas: `set(lista)` — mas lembre-se que isso **perde a ordem**.

&nbsp;

## Dicionários no Python

> ### O que foi feito nessa aula

Nesta aula conhecemos os **dicionários**, uma das estruturas de dados mais poderosas do Python.

Um dicionário é uma **coleção não ordenada** de pares **chave:valor**, definidos entre chaves `{}`.

- **Chave:** identificador único (não pode se repetir).
- **Valor:** informação associada a essa chave.
- Permitem acesso rápido aos dados através da chave, sem precisar percorrer toda a estrutura.

> ### Exemplo inicial

```python
pessoa = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(pessoa)          # Exibe todo o dicionário
print(pessoa['nome'])  # Acessa valor pela chave
```

> ### Operações comuns

```python
# Adicionar ou atualizar chave
pessoa.update({'cidade': 'São Paulo'})
print(pessoa)

# Exibir chaves, valores e pares
print(pessoa.keys())    # dict_keys(['nome', 'sexo', 'idade', 'cidade'])
print(pessoa.values())  # dict_values(['Gustavo', 'M', 22, 'São Paulo'])
print(pessoa.items())   # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ...])

# Remover elementos
del pessoa['sexo']      # Remove a chave 'sexo'
idade = pessoa.pop('idade')  # Remove e retorna o valor da chave 'idade'
print(pessoa)

#Acessando valores no dicionário com .get()
print(pessoa.get('nome'))  # Acessa o valor associado à chave 'nome'
print(pessoa.get('cidade', 'Não encontrada'))  # Tenta acessar 'cidade', retorna 'Não encontrada' se não existir
print(pessoa.get('idade', 0))   # Tenta acessar 'idade', retorna '0' se não existir
```

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar chaves descritivas (`"nome"`, `"idade"`) | Melhora clareza e manutenção |
| Acessar valores com `.get("chave")` quando não há certeza se existe | Evita `KeyError` |
| Utilizar dicionários aninhados para dados complexos | Estrutura dados hierárquicos |
| Iterar com `.items()` quando precisa de chave e valor juntos | Código mais limpo |
| Usar dicionários para transformar listas em mappings (`dict(zip(...))`) | Criação rápida de mapeamentos |

> ### Dicas DevOps

- **JSON ↔ Dicionário:** dados em JSON de APIs são facilmente convertidos para dicionários com `json.loads()`.
- **Evite sobrescrever chaves:** sempre valide se uma chave já existe antes de atualizar.
- **Use `.get()`** para evitar erros ao acessar chaves que podem não existir.
- **Iteração eficiente:** use `.items()` em loops para trabalhar com chave e valor ao mesmo tempo.
- **Configurações centralizadas:** mantenha variáveis de ambiente e configs em dicionários, o que facilita ajustes sem alterar a lógica.

&nbsp;

## Condicionais em Python

> ### O que foi feito nessa aula

Nesta aula estudamos as **estruturas condicionais** no Python, que permitem executar diferentes blocos de código com base em **condições específicas**.

A estrutura básica de uma condicional é composta pelos blocos:

- **`if`** → executa caso a condição seja verdadeira.
- **`elif`** → alternativa intermediária caso o `if` seja falso.
- **`else`** → executa caso todas as condições anteriores sejam falsas.

> ### Sintaxe básica

```python
if <condição>:
    # bloco executado se a condição for verdadeira
elif <outra condição>:
    # executado se a primeira for falsa e essa verdadeira
else:
    # executado se todas forem falsas
```

> ### Exemplo prático

```python
status = "erro"

if status == "sucesso":
    print("A operação foi bem-sucedida.")
elif status == "aviso":
    print("A operação foi concluída com um aviso.")
else:
    print("A operação falhou. Verifique os logs para mais detalhes.")
```

Saída:

```
A operação falhou. Verifique os logs para mais detalhes.
```

> ### Operadores de comparação

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `==` | Igualdade | `x == 10` |
| `!=` | Diferença | `x != 10` |
| `<` | Menor que | `x < 10` |
| `>` | Maior que | `x > 10` |
| `<=` | Menor ou igual | `x <= 10` |
| `>=` | Maior ou igual | `x >= 10` |

> ### Operadores lógicos

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `and` | Verdadeiro se **todas** condições forem verdadeiras | `x > 10 and y < 5` |
| `or` | Verdadeiro se **pelo menos uma** for verdadeira | `x > 10 or y < 5` |
| `not` | Inverte o valor lógico | `not x > 10` |

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Usar condições claras e legíveis | Facilita manutenção do código |
| Evitar condicionais muito aninhadas | Melhora legibilidade |
| Preferir operadores lógicos bem usados | Reduz redundância |
| Documentar regras de negócio aplicadas nas condições | Evita ambiguidades |
| Testar cenários críticos (falha, sucesso, exceções) | Garante robustez em sistemas DevOps |

> ### Exemplo realista

**Cenário:** Script para monitorar uso de CPU em um servidor.

```python
cpu_usage = 75

if cpu_usage > 80:
    print("Uso de CPU alto. Considere otimizar a aplicação.")
elif cpu_usage < 20:
    print("Uso de CPU baixo. A aplicação pode estar ociosa.")
elif cpu_usage == 50:
    print("Uso de CPU estável. A aplicação está funcionando normalmente.")
else:
    print("Uso de CPU moderado.")
```

Saída:

```
Uso de CPU moderado.
```

> ### 5. Dicas DevOps

- **Defina limites claros (thresholds)** em métricas de monitoramento para evitar falsos positivos.
- **Combine condicionais com automação:** ex.: disparar rollback quando `status == "erro"`.
- **Prefira funções para encapsular regras complexas** ao invés de condicionais muito longas.
- **Sempre trate o “else”**: em produção, é melhor prever cenários inesperados do que deixar o script falhar.
- **Use operadores lógicos para múltiplos critérios** (ex.: CPU, memória, disco) em monitoramento avançado.

&nbsp;

## Loops no Python

> ### O que foi feito nessa aula

Nesta aula estudamos os **loops no Python**, estruturas fundamentais para **repetição de código** até que uma condição seja satisfeita.

Existem dois tipos principais:

- **`for`** → O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outros objetos iteráveis.
- **`while`** → O loop while é usado para executar um bloco de código enquanto uma condição for verdadeira.

> ### Loop `for`

A sintaxe básica do loop for é a seguinte:

```python
for item in sequencia:
   # faça algo com o item
```

Útil quando sabemos **quantas vezes** queremos repetir ou quando precisamos percorrer elementos de uma coleção.

Exemplo de uso de loop for em DevOps:

```python
for i in range(5):
    print(i)    # Imprime os números de 0 a 4
```

> ### Loop `while`

Executa repetidamente enquanto a condição for verdadeira.

A sintaxe básica do loop while é a seguinte:

```python
while condicao:
    # faça algo
    # se a condição for verdadeira, o bloco de código será executado novamente
```

Exemplo de uso de loop while em DevOps:

```python
i = 0
while i < 5:   # Aqui estamos dizendo, 'enquanto i for menor que 5'.
    print(i)  # Imprime de 0 a 4
    i += 1
```

Mais indicado quando **não sabemos o número exato de repetições** de antemão.

> ### Contadores

Um contador é uma variável usada para rastrear o número de iterações:

```python
for i in range(5):    # 'i' é o contador que começa em 0 e vai até 4
    print(f"Iteração número {i}")

contador = 0
while contador < 5:
    print(f"Iteração número {contador}")
    contador += 1     # Incrementa o contador em 1 a cada iteração do loop, que seria a mesma coisa que contador = contador + 1
```

## Comandos úteis dentro de loops

> ### `break`

Encerra o loop imediatamente, mesmo que a condição ainda seja verdadeira.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Saída:

```
0
1
2
3
4
```

> ### `continue`

Pula a iteração atual e vai direto para a próxima.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Saída:

```
0
1
3
4
```

> ### `pass`

Usado como um “placeholder” → não faz nada, mas evita erro de sintaxe quando ainda não há código implementado.

```python
for i in range(3):
    if i == 1:
        pass  # Lugar reservado para código futuro
    else:
        print(i)
```

Saída:

```
0
2
```

> ### `enumerate()`

Permite iterar obtendo **índice + valor** ao mesmo tempo.

```python
servidores = ['server1', 'server2', 'server3']

for i, servidor in enumerate(servidores):
    print(f"{i}: {servidor}")
```

Saída:

```
0: server1
1: server2
2: server3
```

> ### `zip()`

Permite iterar em paralelo sobre duas (ou mais) listas.

```python
servidores = ['server1', 'server2', 'server3']
status = ['ativo', 'inativo', 'ativo']

for servidor, estado in zip(servidores, status):
    print(f'Servidor: {servidor}, Estado: {estado}')
```

Saída:

```
Servidor: server1, Estado: ativo
Servidor: server2, Estado: inativo
Servidor: server3, Estado: ativo
```

> ### Dicas DevOps

- **Evite loops infinitos** → sempre defina uma condição de saída.
- **Use logs dentro de loops longos** para facilitar o monitoramento em produção.
- **Adicione `sleep()`** em loops contínuos para não sobrecarregar o sistema.
- **Prefira `for` quando souber o número de elementos**, para evitar complexidade desnecessária.
- **Combine loops com condicionais** (`if`) para automações inteligentes (ex.: só agir se uso de CPU > 80%).
- Use `break` em **loops de monitoramento** para encerrar quando uma condição crítica for atingida.
- Combine `continue` com **filtros de servidores** (ex.: pular os que estão desativados).
- Use `enumerate` em logs para **registrar posição da iteração** junto ao valor.
- `zip` é útil em **deploys paralelos**, quando relacionamos **lista de servidores** e **versões de software**.

&nbsp;

## List Comprehensions no Python

> ### O que foi feito nessa aula

Nesta aula estudamos **List Comprehensions**, uma forma **concisa e poderosa** de criar listas em Python.

Elas permitem gerar listas a partir de **outras listas, tuplas ou iteráveis**, podendo incluir **condições e transformações** de dados.

A sintaxe geral é:

```python
[expressao for item in iteravel if condicao]
```

> ### Exemplos práticos

**Criando lista de nomes de containers**

```python
containers = [
    {"name": "web", "status": "running"},
    {"name": "db", "status": "stopped"},
    {"name": "cache", "status": "running"},
]

names = [container["name"] for container in containers]
print(names)  # Saida: ['web', 'db', 'cache']
```

**Com condicional (filtragem)**

```python
running_containers = [c["name"] for c in containers if c["status"] == "running"]
print(running_containers)  # Saida: ['web', 'cache']
```

**Manipulação de strings**

```python
uppercase_names = [c["name"].upper() for c in containers]
print(uppercase_names)  # Saida: ['WEB', 'DB', 'CACHE']
```

**Números**

```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # Saida: [1, 4, 9, 16, 25]
```

**Tuplas**

```python
container_tuples = [(c["name"], c["status"]) for c in containers]
print(container_tuples)
# Saida: [('web', 'running'), ('db', 'stopped'), ('cache', 'running')]
```

> ### Vantagens e melhores práticas

| Prática | Impacto |
| --- | --- |
| Preferir List Comprehensions a loops simples | Código mais limpo e legível |
| Incluir `if` dentro da expressão para filtragem | Facilita seleção de elementos |
| Usar transformações diretas na expressão | Menos variáveis temporárias |
| Evitar expressões muito complexas | Se ficar longo demais, prefira `for` normal |
| Combinar com funções (`upper()`, `len()`, etc.) | Permite transformação inline |

> ### Exemplo realista

**Cenário:** Lista de instâncias em nuvem com status variado.

Queremos listar apenas as instâncias em execução e em letras maiúsculas.

```python
instancias = [
    {"id": "srv1", "status": "running"},
    {"id": "srv2", "status": "stopped"},
    {"id": "srv3", "status": "running"},
]

ativas = [srv["id"].upper() for srv in instancias if srv["status"] == "running"]

print(ativas)  # Saída: ['SRV1', 'SRV3']
```

> ### Dicas DevOps

- **Substitua loops tradicionais simples** por List Comprehensions para deixar o código mais direto.
- **Use filtros condicionais** para selecionar apenas elementos relevantes (ex.: containers ativos, usuários válidos).
- **Transforme dados inline** (strings em maiúsculas, métricas ao quadrado, etc.).
- **Cuidado com a complexidade:** se a lógica exigir múltiplos `if` e operações aninhadas, prefira um loop tradicional.
- **Combine com dicionários e sets comprehensions** (`{}`, `set()`) para transformar ou filtrar em outros formatos de estrutura.

&nbsp;

## Unpacking no Python

> ### O que foi visto nessa aula

Nesta aula estudamos o conceito de **Unpacking** (ou desempacotamento), que é um recurso do Python para **atribuir valores de listas, tuplas, dicionários e outros iteráveis diretamente a variáveis** de forma clara e legível.

O Unpacking deixa o código mais **curto, expressivo e intuitivo**, algo muito útil em automações e scripts de DevOps onde manipulamos listas de servidores, ambientes ou configurações.

> ### Exemplos práticos

**Unpacking em listas**

```python
environment_list = ["development", "staging", "production"]
dev, stg, prod = environment_list

print(f"Siglas para os ambientes: dev = {dev}, stg = {stg}, prod = {prod}")
```

Resultado:

`Siglas para os ambientes: dev = development, stg = staging, prod = production`

**Unpacking em tuplas**

```python
servers = (
    {"name": "server1", "ip": "192.168.1.1"},
    {"name": "server2", "ip": "192.168.1.2"},
    {"name": "server3", "ip": "192.168.1.3"}
)

for server in servers:
    name, ip = server.values()
    print(f"Server: {name}, IP: {ip}")
```

**Ignorando valores com `_`**

```python
for server in servers:
    # Em casos onde tempos apenas dois valores, o underscore (_) é usado para indicar que não precisamos do segundo valor.
    name, _ = server.values()
    print(f"Server: {name}")
```

**Ignorando múltiplos valores com**

```python
itens, *rest = servers
print(f"Primeiro item: {itens}, Restante: {rest}")

first, *_, last = servers
print(f"Primeiro item: {first}, Último item: {last}")
```


**Unpacking em funções com `*`**

```python
def print_server_info(name, ip):
    print(f"Server Name: {name}, IP Address: {ip}")

for server in servers: # Lembrando que 'server' esta retornando um dicionário.
    print_server_info(**server)

    # O operador ** desempacota o dicionário, passando as chaves como nomes de parâmetros e os valores como argumentos.
```

Aqui o operador `**` desempacota um **dicionário**, passando suas **chaves como nomes de parâmetros** e os **valores como argumentos**.

> ### Vantagens e boas práticas

| Prática | Impacto |
| --- | --- |
| Usar `_` para ignorar valores | Código mais limpo e explícito |
| Utilizar `*` para capturar listas de valores | Mais flexibilidade em iterações |
| Combinar com funções (`*args`, `**kwargs`) | Torna funções mais reutilizáveis |
| Usar unpacking em dicionários | Simplifica passagem de configs e parâmetros |
| Evitar excessos | Se houver muitos `*` e `_`, pode perder clareza |

> ### Exemplo realista

**Cenário:** Queremos iterar sobre servidores de produção e passar seus dados direto para uma função de monitoramento.

```python
def monitor_server(name, ip):
    print(f"Monitorando {name} ({ip})...")

servers = [
    {"name": "app-server", "ip": "10.0.0.1"},
    {"name": "db-server", "ip": "10.0.0.2"}
]

for srv in servers:
    monitor_server(**srv)
```

Saída:

```
Monitorando app-server (10.0.0.1)...
Monitorando db-server (10.0.0.2)...
```

> ### Dicas DevOps

- Use unpacking para **atribuir variáveis rapidamente** a partir de listas ou tuplas de configs.
- Utilize  e `*` em funções para **receber e passar parâmetros de forma dinâmica**.
- Sempre que possível, ignore valores desnecessários com `_`, evitando poluir o código.
- Em scripts de automação, unpacking torna fácil manipular **dados de APIs, JSONs e arquivos YAML**.
- Mantenha a legibilidade: unpacking deve **simplificar**, não complicar o código.


&nbsp;

## Funções no Python

> ### O que aprendemos nessa aula

Aqui, você conheceu o **poder das funções** no Python:

🔹 Um jeito de **modularizar** seu código — quebrando em pedaços menores e reutilizáveis.

🔹 Funções ajudam na **organização**, **clareza** e **reuso**, evitando repetição de lógica.

🔹 Elas podem receber **parâmetros** (entradas) e retornar **valores** (saídas).

🔹 Você pode definir **valores padrão** para parâmetros, tornando a função mais flexível.

> ### Estrutura básica de uma função

```python
def nome_da_funcao(parametros):
    # bloco de código
    return resultado
```

- `def`: palavra-chave para declarar funções.
- `parametros`: variáveis que a função recebe como entrada.
- `return`: define o valor de saída (se não houver, a função retorna `None`).

> ### Exemplos estudados

**Função simples**

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

Chamando a função:

```python
print(saudacao("Vinicius"))
```

Saída:

```
Olá, Vinicius!
```


**Função com múltiplos parâmetros**

```python
def soma(a, b):
    return a + b

print(soma(5, 3))  # Saída: 8
```


**Função com parâmetros padrão**

```python
def potencia(base, expoente=2): # Aqui, o parametro 'expoente' tem um valor padrão de 2. Se não for fornecido, ele será 2.
    return base ** expoente

print(potencia(4))     # Usa expoente padrão 2 → 16
print(potencia(4, 3))  # Usa expoente fornecido 3 → 64
```

Isso é útil quando você quer definir um **comportamento comum**, mas ainda assim permitir flexibilidade.

> ### Como funções são usadas em DevOps

Funções são fundamentais para **automação** e **scripts reutilizáveis**.

Veja exemplos práticos no dia a dia de quem trabalha com infraestrutura:

| Cenário | Exemplo de Função | Benefício |
| --- | --- | --- |
| **Deploy** | `def deploy_app(env): ...` | Reutiliza mesma lógica em diferentes ambientes (dev, stg, prod) |
| **Monitoramento** | `def check_cpu(threshold=80): ...` | Monitora métricas com alerta configurável |
| **Manipulação de Logs** | `def parse_log(file): ...` | Centraliza lógica de parsing em um único lugar |
| **Infraestrutura como Código** | `def create_instance(type, region): ...` | Facilita criação de instâncias com diferentes parâmetros |

> ### Vantagens e boas práticas

- **Organização** → separa responsabilidades em blocos.
- **Reuso** → evita duplicar código.
- **Clareza** → cada função deve ter uma única responsabilidade (princípio SRP).
- **Flexibilidade** → com parâmetros padrão e múltiplos.
- **Testabilidade** → funções pequenas são mais fáceis de testar.

---

> ### Exemplo realista em DevOps

**Cenario:** Imagine que você precisa **checar se servidores estão online**:

```python
def check_server_status(name, ip):
    # Aqui você poderia usar ping ou uma lib de requests
    print(f"Verificando servidor {name} no IP {ip}...")
    return True  # Supondo que está online

servers = [
    {"name": "app-server", "ip": "10.0.0.1"},
    {"name": "db-server", "ip": "10.0.0.2"}
]

for server in servers:
    status = check_server_status(server["name"], server["ip"])
    if status:
        print(f"{server['name']} está online ✅")
    else:
        print(f"{server['name']} está offline ❌")
```

---

> ### Dicas finais

- Nomeie funções de forma **descritiva** (ex.: `calcular_media`, `verificar_status`).
- Prefira funções **curtas e focadas em uma única tarefa**.
- Use parâmetros padrão para **flexibilidade sem complicação**.
- Use `return` para deixar claro o que sua função devolve.
- Documente com **docstrings** para explicar propósito e uso da função.