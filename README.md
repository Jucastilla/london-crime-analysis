# London Crime Analysis

## Sobre o Projeto

Este projeto foi desenvolvido durante a formação em **Análise de Dados da EBAC**, com o objetivo de analisar a evolução e a distribuição dos crimes registrados em Londres entre **2008 e 2016**, utilizando Google BigQuery, Python, SQL e Power BI.

Os dados foram consultados no **Google BigQuery**, enquanto o Python foi utilizado para estabelecer a conexão com a plataforma e executar consultas SQL voltadas à validação e verificação da consistência da base.

O projeto também inclui um dashboard desenvolvido no **Power BI**, composto por três páginas de análise, permitindo acompanhar a evolução dos crimes ao longo do período, identificar os distritos e categorias com maior número de ocorrências e apresentar prioridades e recomendações com base nos resultados encontrados.

O projeto reúne **Python, SQL, Google BigQuery e Power BI**, contemplando procedimentos de verificação da qualidade dos dados e a construção de visualizações voltadas à análise dos registros de criminalidade em Londres.

## Objetivo

Analisar os registros de crimes de Londres entre 2008 e 2016, identificando padrões temporais, categorias de crimes mais frequentes e distritos com maior concentração de ocorrências.

O projeto também busca demonstrar a utilização de **Python, SQL, Google BigQuery e Power BI** em diferentes etapas de um projeto de análise de dados, incluindo validação, exploração, visualização e interpretação dos resultados.

## Etapas Desenvolvidas

### 1. Conexão com o Google BigQuery

Foi realizada a conexão com o **Google BigQuery** utilizando Python e a biblioteca `google.cloud.bigquery`.

O projeto utilizado para realizar as consultas foi:

`projeto-london-crime-506516`

A conexão permitiu executar consultas SQL diretamente pelo script Python e transformar os resultados das validações em DataFrames.

### 2. Fonte e Estrutura dos Dados

A análise utilizou a tabela:

`projeto-london-crime-506516.london_crime.crime_by_lsoa`

A tabela reúne registros que permitem analisar crimes por distrito, categoria e período.

Entre os campos verificados durante o projeto estão:

* `lsoa_code`
* `borough`
* `major_category`
* `minor_category`
* `value`
* `year`
* `month`

O período apresentado no dashboard compreende os anos de **2008 a 2016**.

### 3. Validação e Consistência dos Dados

Foram realizadas consultas SQL para verificar aspectos relacionados à qualidade e à consistência dos dados.

A validação contemplou:

* Quantidade total de registros;
* Valores nulos nas principais colunas;
* Menor e maior ano registrado;
* Menor e maior mês registrado;
* Menor e maior valor registrado;
* Existência de meses fora do intervalo de 1 a 12;
* Existência de valores negativos;
* Tipos de dados das colunas;
* Identificação das colunas que permitem valores nulos.

As consultas foram executadas no BigQuery por meio do script Python, e os resultados foram convertidos em DataFrames para visualização e conferência.

### 4. Desenvolvimento do Dashboard no Power BI

Foi desenvolvido um dashboard no **Power BI** para analisar a evolução e a distribuição dos crimes em Londres.

O relatório foi estruturado em **três páginas**, cada uma direcionada a uma etapa da análise.

#### Visão Geral

A primeira página apresenta os principais indicadores do conjunto de dados e a evolução dos crimes por categoria.

Entre os indicadores apresentados estão:

* Aproximadamente **6 milhões** de crimes registrados;
* **33 distritos** analisados;
* **9 categorias** de crimes;
* **Westminster** como distrito com maior volume de crimes;
* **Theft and Handling** como categoria mais frequente;
* **2008** como ano com maior número de crimes.

Também foi construída uma visualização da evolução das diferentes categorias de crimes entre 2008 e 2016.

#### Análise por Distrito

A segunda página apresenta a distribuição dos registros entre os distritos de Londres.

Foi desenvolvido um ranking dos **10 distritos com maior número de crimes**, permitindo identificar as áreas com maior concentração de ocorrências.

Também foi analisada a evolução dos crimes nos cinco principais distritos:

* Westminster;
* Lambeth;
* Southwark;
* Camden;
* Newham.

#### Prioridades e Recomendações

A terceira página apresenta a distribuição dos crimes por categoria nos cinco distritos prioritários:

* Westminster;
* Lambeth;
* Southwark;
* Camden;
* Newham.

A análise permite comparar a distribuição das categorias de crimes nesses distritos e identificar os tipos de ocorrência com maior concentração.

A página também reúne os principais resultados identificados e apresenta uma recomendação de priorização de ações de prevenção e alocação de recursos.

### 5. Análise dos Resultados

A análise identificou **Westminster** como o distrito com maior volume acumulado de crimes, com aproximadamente **455 mil registros** no período apresentado.

A categoria **Theft and Handling** apresenta a maior concentração de ocorrências entre os distritos prioritários, com destaque especialmente elevado em Westminster.

Além de Westminster, **Lambeth, Southwark, Camden e Newham** também aparecem entre os distritos com maior volume acumulado de registros.

Outro comportamento destacado no dashboard é o crescimento de **Violence Against the Person** durante o período analisado, indicando uma categoria que merece acompanhamento mesmo não apresentando o maior volume total de ocorrências.

### 6. Conclusões

O projeto permitiu analisar a evolução e a distribuição dos crimes registrados em Londres entre 2008 e 2016 utilizando diferentes ferramentas de análise de dados.

Com **Python, SQL e Google BigQuery**, foram realizadas consultas para verificar valores nulos, consistência e tipos dos dados.

No **Power BI**, os registros foram apresentados em um dashboard composto por três páginas, permitindo acompanhar a evolução dos crimes, identificar os distritos e categorias com maior número de ocorrências e comparar as áreas prioritárias.

Os resultados apresentados no dashboard destacam uma concentração relevante de ocorrências em **Westminster**, principalmente na categoria **Theft and Handling**, enquanto **Violence Against the Person** apresenta uma evolução que merece acompanhamento.

A recomendação apresentada na análise é priorizar recursos de prevenção em Westminster e nos demais distritos de maior incidência, com ações direcionadas principalmente a **Theft and Handling**, sem deixar de acompanhar o avanço de **Violence Against the Person**.

## Habilidades Demonstradas

* Análise de Dados
* Python
* SQL
* Google BigQuery
* Power BI
* DataFrames
* Integração com BigQuery
* Consultas SQL
* Validação de Dados
* Verificação de Valores Nulos
* Verificação de Consistência dos Dados
* Verificação de Tipos de Dados
* Análise Temporal
* Análise por Categoria
* Análise por Distrito
* Visualização de Dados
* Construção de Dashboards
* Indicadores e KPIs
* Análise e Interpretação de Dados
* Recomendações Baseadas em Dados
* Documentação Técnica

## Arquivos do Projeto

Os principais arquivos do projeto estão organizados entre o script utilizado para conexão e validação dos dados e os arquivos relacionados ao dashboard desenvolvido no Power BI.

### Script

🐍 [Script - Conexão e Validação no BigQuery](scripts/conexao_bigquery_london_crime%282%29.py)

Script Python contendo a conexão com o Google BigQuery e as consultas SQL utilizadas para validação de valores nulos, verificação da consistência e consulta dos tipos de dados da tabela.

### Dashboard

📊 [Dashboard - London Crime Analysis (PDF)](dashboard/london_crime_analysis%281%29.pdf)

Versão em PDF do dashboard desenvolvido no Power BI, contendo as três páginas da análise: visão geral, análise por distrito e prioridades e recomendações.

### Arquivo Power BI

📈 [Acessar arquivo do Power BI (.pbix)](COLE_AQUI_O_LINK_DO_GOOGLE_DRIVE)

Arquivo original do projeto desenvolvido no Power BI, disponibilizado externamente devido ao tamanho do arquivo.
