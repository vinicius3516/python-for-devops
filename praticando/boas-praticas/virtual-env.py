# Estudando sobre virtual env
# Um virtual env permite que voce crie ambientes isolados para sua aplicação, onde vocé pode instalar e gerenciar suas dependências sem afetar o ambiente principal do seu sistema.

# Exemplo de uso de virtual env em DevOps:

# Criação de um ambiente virtual
# Para criar um ambiente virtual, use o comando python3 -m venv nome_do_ambiente, na maioria das vezes o nome do ambiente virtual eh o mesmo nome da pasta onde ele será criado.
python3 -m venv venv


# Ativação do ambiente virtual
# Para ativar o ambiente virtual, use o comando source nome_do_ambiente/bin/activate. Assim que estiver ativo, voce vera o prompt do ambiente virtual, indicando que voce esta trabalhando nele.
source .venv/bin/activate


# Desativação do ambiente virtual
# Para desativar o ambiente virtual, use o comando deactivate.
deactivate


