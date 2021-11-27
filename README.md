# Avaliacão Módulo II

## Sobre o projeto:

O projeto consiste:
 - Criar uma API
 - Onde nesta, será dado uma opção de filtragem de dados: aqui é a coluna __purpose__
 - Com dados filtrados: agregou-se os dados quantitativos da coluna __credit_amount__ agrupados pela coluna de dados qualitativos __job__ para salvar como CSV e json.
 - Também, após o filtro, será gerado um gráfico boxplot sobre os valores da coluna __credit_amount__, para cada classe da coluna __job__ e agrupados pela classe da coluna __class__(variável qualitativa).
 - Por fim, fornece os dados para leitura.

## Base de Dados

Base de dados utilizada disponível em:

https://datahub.io/machine-learning/credit-g


## Etapas para rodar o projeto (Linux)

1 - Clonar repositório

```
git clone https://github.com/EderReisS/Avaliacao-Modulo-II-Let-s-Code.git

```

2 - Mudar para diretório do projeto

```
cd Avaliacao-Modulo-II-Let-s-Code
```

3 - Criar ambiente virtual

```
virtualenv env
```

4 - Ativar ambiente virtual

```
source env/bin/activate
```

5 - Instalar bibliotecas

```
pip3 install -r requirements.txt
```

6 - Abrir jupyter notebook

```
jupyter notebook
```

7 - Abrir o arquivo `main.ipynb` ou servidor `api_credit.py` no terminal/kernel. 
