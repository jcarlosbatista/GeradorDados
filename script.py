import pandas as pd

# Dados de exemplo
data = {
    'data_venda': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
    'produto': ['A', 'B', 'A', 'B'],
    'categoria': ['X', 'Y', 'X', 'Y'],
    'valor': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Ajuste de dados
# Convertendo a coluna 'data_venda' para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Transformação de dados
# Tratamento de valores nulos
df.fillna(0, inplace=True)

# Coluna calculada
# Calculando o valor total de cada transação
df['valor_total'] = df['valor']

# Agregação de dados
# Estatísticas de vendas por produto
total_vendas_por_produto = df.groupby('produto')['valor_total'].sum()

# Estatísticas de vendas por categoria
total_vendas_por_categoria = df.groupby('categoria')['valor_total'].sum()

print("Total de vendas por produto:")
print(total_vendas_por_produto)
print("\nTotal de vendas por categoria:")
print(total_vendas_por_categoria)
