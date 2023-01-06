# DataPipeline

Pipeline de operações criado para gerenciar dados e gerar um arquivo.csv no final
 
## Desafio

- unificar os datasets rouanet.csv e censo_estado.csv atraves das colunas estado_ibge e código, respectivamente
- criar uma Natural Key para esse dado, usando as colunas estado_ibge e valor_em_reais
- remover as linhas duplicadas de acordo com a surrogate key
- remover linhas com valor_em_reais = 0 ou quantidade = 0
- trocar os dados da coluna estado para a sigla da UF correspondente, ex.: Rio de Janeiro vira RJ

## Como configurar o setup

Clone o projeto:
* git clone https://github.com/aninhasalesp/data_pipeline.git

Com docker:
1. [Install docker](https://docs.docker.com/get-docker/)
2. *cd data_pipeline* para encontrar o projeto
