# DataPipeline

Pipeline de operações criado para gerenciar dados e gerar um arquivo.csv no final
 
## Desafio

- unificar os datasets rouanet.csv e censo_estado.csv atraves das colunas estado_ibge e código, respectivamente
- criar uma Natural Key para esse dado, usando as colunas estado_ibge e valor_em_reais
- remover as linhas duplicadas de acordo com a natural key
- remover linhas com valor_em_reais = 0 ou quantidade = 0
- trocar os dados da coluna estado para a sigla da UF correspondente, ex.: Rio de Janeiro vira RJ

## Como executar
### Clone o projeto:
- git clone https://github.com/aninhasalesp/data_pipeline.git
- `cd data_pipeline` para entrar na pasta do projeto

### Com docker:
1. [Instalar o docker](https://docs.docker.com/get-docker/)
2. `docker build -t trata_dados:v1 .`
3. Para imprimir o resultado na tela: 
    ```
    docker run -it --rm \
     -v /caminho/na/sua/maquina/censo_estado.csv:/censo.csv \
     -v /caminho/na/sua/maquina/rouanet.csv:/rouanet.csv \
     trata_dados:v1

    ```
4. Para gravar o resultado em um arquivo:
    ```
    docker run -it --rm \
     -v /caminho/na/sua/maquina/censo_estado.csv:/censo.csv \
     -v /caminho/na/sua/maquina/rouanet.csv:/rouanet.csv \
     trata_dados:v1 > /caminho/do/arquivo/na/sua/maquina.csv

    ```

### Com poetry/virtualenv:
1. Instalar o [poetry](https://python-poetry.org/docs/#installation): `pip install poetry`
2. `poetry shell`
3. `poetry install`
4. Para ver a documentação: `python pipeline.py --help`
5. Exemplos: 
    ```
    python pipeline.py /caminha/da/sua/maquina/censo_estado.csv /caminho/da/sua/maquina/rouanet.csv

    python pipeline.py /caminha/da/sua/maquina/censo_estado.csv /caminho/da/sua/maquina/rouanet.csv -o algumapasta/arquivo.csv
    
    python pipeline.py /caminha/da/sua/maquina/censo_estado.csv /caminho/da/sua/maquina/rouanet.csv > algumapasta/arquivo.csv

    ```

