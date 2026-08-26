from google.cloud import bigquery


# ============================================================
# 1. CONEXÃO COM O BIGQUERY
# ============================================================

project_id = "projeto-london-crime-506516"

client = bigquery.Client(project=project_id)

print("Conexão com o BigQuery realizada com sucesso!")


# ============================================================
# 2. VALIDAÇÃO DE VALORES NULOS
# ============================================================

query_validacao = """
SELECT
    COUNT(*) AS total_registros,
    COUNTIF(lsoa_code IS NULL) AS nulos_lsoa_code,
    COUNTIF(borough IS NULL) AS nulos_borough,
    COUNTIF(major_category IS NULL) AS nulos_major_category,
    COUNTIF(minor_category IS NULL) AS nulos_minor_category,
    COUNTIF(value IS NULL) AS nulos_value,
    COUNTIF(year IS NULL) AS nulos_year,
    COUNTIF(month IS NULL) AS nulos_month
FROM
    `projeto-london-crime-506516.london_crime.crime_by_lsoa`
"""

resultado_validacao = client.query(query_validacao).to_dataframe()

print("\nValidação de valores nulos:")
print(resultado_validacao)


# ============================================================
# 3. VERIFICAÇÃO DE CONSISTÊNCIA DOS DADOS
# ============================================================

query_consistencia = """
SELECT
    MIN(year) AS menor_ano,
    MAX(year) AS maior_ano,
    MIN(month) AS menor_mes,
    MAX(month) AS maior_mes,
    MIN(value) AS menor_valor,
    MAX(value) AS maior_valor,
    COUNTIF(month < 1 OR month > 12) AS meses_invalidos,
    COUNTIF(value < 0) AS valores_negativos
FROM
    `projeto-london-crime-506516.london_crime.crime_by_lsoa`
"""

resultado_consistencia = client.query(query_consistencia).to_dataframe()

print("\nVerificação de consistência dos dados:")
print(resultado_consistencia)


# ============================================================
# 4. VERIFICAÇÃO DOS TIPOS DE DADOS
# ============================================================

query_tipos = """
SELECT
    column_name,
    data_type,
    is_nullable
FROM
    `projeto-london-crime-506516.london_crime.INFORMATION_SCHEMA.COLUMNS`
WHERE
    table_name = 'crime_by_lsoa'
ORDER BY
    ordinal_position
"""

resultado_tipos = client.query(query_tipos).to_dataframe()

print("\nTipos de dados da tabela:")
print(resultado_tipos)
