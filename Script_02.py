import pandas as pd

# Dados de exemplo
data = {
    'data_venda': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03'],
    'produto': ['A', 'B', 'A', 'B', 'A', 'B'],
    'categoria': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'valor': [100, 200, 150, 250, 120, 220]
}
df = pd.DataFrame(data)

# Ajuste de dados
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Compra ao longo do tempo
# Adicionando uma coluna de mês para análise temporal
df['mes_venda'] = df['data_venda'].dt.month

# Criar categorias personalizadas de produtos
# Definindo uma função para categorizar os produtos
def categorizar_produto(produto):
    if produto == 'A':
        return 'Produto A'
    elif produto == 'B':
        return 'Produto B'
    else:
        return 'Outros'

# Aplicando a função para criar a nova coluna de categoria de produto
df['categoria_produto'] = df['produto'].apply(categorizar_produto)

# Agregando dados para análise
# Total de vendas por categoria de produto ao longo do tempo
total_vendas_por_categoria_produto = df.groupby(['categoria_produto', 'mes_venda'])['valor'].sum()

print("Total de vendas por categoria de produto ao longo do tempo:")
print(total_vendas_por_categoria_produto)
