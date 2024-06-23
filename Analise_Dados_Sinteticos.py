import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
from babel.numbers import format_currency

#
def grafico_barras(df, x, y, xlabel, ylabel, title, color, formato_moeda=False, figsize=(12, 6)):
    plt.figure(figsize=figsize)
    ax = sns.barplot(data=df, x=x, y=y, palette=color, orient='h')
    for p in ax.patches:
        width = p.get_width()
        label = format_currency(width, 'BRL', locale='pt_BR') if formato_moeda else f'{int(width)} unidades'
        ax.text(width * 0.95, p.get_y() + p.get_height() / 2, label, ha='right', va='center')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.title(title, fontsize='16')
    plt.xlabel(xlabel, fontsize='14')
    plt.ylabel(ylabel, fontsize='14')
    plt.savefig(f'{x}_{y}.png', dpi=300, bbox_inches='tight')
    plt.close()

def grafico_pizza(df, x, y, title, color, formato_moeda=False, figsize=(10, 6)):
    plt.figure(figsize=figsize)
    plt.pie(df[y], labels=df[x], autopct='%1.1f%%', pctdistance=0.75, colors=color)
    circle = plt.Circle((0, 0), 0.5, color='white')
    plt.gca().add_artist(circle)
    total = df[y].sum()
    label = format_currency(total, 'BRL', locale='pt_BR') if formato_moeda else f'{int(total)} unidades'
    plt.text(0, 0, f'Total:\n{label}', ha='center', va='center', fontsize=12)
    plt.title(title)
    plt.savefig(f'distribuicao_{x}_{y}.png', dpi=300, bbox_inches='tight')
    plt.close()

plt.rc('font', family='serif')

diretorio = 'dados_vendas_sinteticos' # Diretório para armazenar os arquivos CSV
dfs = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        try:
            dfs.append(pd.read_csv(caminho_arquivo))
        except pd.errors.EmptyDataError: # verificando se o arquivo é vazio e se for, ignora o arquivo
            print(f"O arquivo {arquivo} está vazio e será ignorado.")
        except Exception as e: # caso de erro, imprime o erro
            print(f"Erro ao ler o arquivo {arquivo}: {e}")

# Verificando se os arquivos foram carregados corretamente
if not dfs:
    raise ValueError("Nenhum dado CSV foi carregado.")

# Concatenando os dataframes
df_completo = pd.concat(dfs, ignore_index=True)

# Verificando se o dataframe contém as colunas 'Região', 'Vendas' e 'Produto'
if 'Região' not in df_completo.columns or 'Vendas' not in df_completo.columns or 'Produto' not in df_completo.columns:
    raise ValueError("O dataframe não contém as colunas 'Região', 'Vendas' ou 'Produto'.")

# Total de vendas por região
total_vendas_por_regiao = df_completo.groupby('Região')['Vendas'].sum().reset_index() # Agrupando por região e somando as vendas, criando um novo dataframe e resetando o index

# Identificação dos produtos mais vendidos
produtos_mais_vendidos = df_completo['Produto'].value_counts().reset_index()
produtos_mais_vendidos.columns = ['Produto', 'Quantidade']
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='Quantidade', ascending=False)
produtos_mais_vendidos_valor = df_completo.groupby('Produto')['Vendas'].sum().reset_index().sort_values(by='Vendas', ascending=False)

# Criando os graficos de barras
grafico_barras(total_vendas_por_regiao, 'Vendas', 'Região', 'Vendas (R$)', 'Região', 'Total de Vendas por Região', plt.cm.Set3.colors, formato_moeda=True)
grafico_barras(produtos_mais_vendidos, 'Quantidade', 'Produto', 'Quantidade', 'Produtos', 'Produtos mais Vendidos - Quantidade', plt.cm.Set2.colors, formato_moeda=False)
grafico_barras(produtos_mais_vendidos_valor, 'Vendas', 'Produto', 'Vendas (R$)', 'Produtos', 'Produtos mais Vendidos - Valor', plt.cm.Set2.colors, formato_moeda=True)

# Criando os graficos de pizza
grafico_pizza(total_vendas_por_regiao, 'Região', 'Vendas', 'Distribuição do Total de Vendas por Região', plt.cm.Set3.colors, formato_moeda=True)
grafico_pizza(produtos_mais_vendidos, 'Produto', 'Quantidade', 'Distribuição dos Produtos mais Vendidos', plt.cm.Set2.colors, formato_moeda=False)

# Exportar os dataframes para arquivos CSV
total_vendas_por_regiao.round(2).to_csv('total_vendas_por_regiao.csv', index=False)
produtos_mais_vendidos.round(2).to_csv('produtos_mais_vendidos.csv', index=False)
