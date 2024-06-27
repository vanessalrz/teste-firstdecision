import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
from babel.numbers import format_currency


# Esse código foi desenvolvido para automatizar a extração e análise de dados de um conjunto de arquivos CSV.

def grafico_barras(df, x, y, xlabel, ylabel, title, color, formato_moeda=False, figsize=(12, 6)):
    """
       Gera um gráfico de barras horizontais a partir de um DataFrame e salva a imagem como um arquivo PNG.

       Args:
           df (pd.DataFrame): DataFrame contendo os dados para o gráfico.
           x (str): Nome da coluna para o eixo x.
           y (str): Nome da coluna para o eixo y.
           xlabel (str): Rótulo do eixo x.
           ylabel (str): Rótulo do eixo y.
           title (str): Título do gráfico.
           color (list): Lista de cores para as barras.
           formato_moeda (bool, optional): Se True, formata os rótulos das barras como moeda (BRL). Default é False.
           figsize (tuple, optional): Tamanho da figura do gráfico. Default é (12, 6).

       Returns:
           None
       """
    # Criando o gráfico de barras usando o seaborn
    plt.figure(figsize=figsize)
    ax = sns.barplot(data=df, x=x, y=y, palette=color, orient='h')

    # Adicionando o rótulo nas barras
    for p in ax.patches:
        width = p.get_width() # "pega" a largura da barra
        label = format_currency(width, 'BRL', locale='pt_BR') if formato_moeda else f'{int(width)} unidades'
        ax.text(width * 0.95, p.get_y() + p.get_height() / 2, label, ha='right', va='center')

    # Removendo as bordas da direita e do topo
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Configurando o título, e os labels do eixo x e o eixo y do gráfico
    plt.title(title, fontsize='16')
    plt.xlabel(xlabel, fontsize='14')
    plt.ylabel(ylabel, fontsize='14')

    # Salvando o gráfico como um arquivo PNG
    plt.savefig(f'Total_{x}_{y}.png', dpi=300, bbox_inches='tight')

    # Fechando o gráfico
    plt.close()


def grafico_pizza(df, x, y, title, color, formato_moeda=False, figsize=(10, 6)):
    """
    Gera um gráfico de pizza a partir de um DataFrame e salva a imagem como um arquivo PNG.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados para o gráfico.
        x (str): Nome da coluna para os rótulos das fatias.
        y (str): Nome da coluna para os valores das fatias.
        title (str): Título do gráfico.
        color (list): Lista de cores para as fatias.
        formato_moeda (bool, optional): Se True, formata o rótulo central como moeda (BRL). Default é False.
        figsize (tuple, optional): Tamanho da figura do gráfico. Default é (10, 6).

    Returns:
        None
    """

    # Criando o gráfico de pizza usando o matplotlib
    plt.figure(figsize=figsize)
    plt.pie(df[y], labels=df[x], autopct='%1.1f%%', pctdistance=0.75, colors=color)

    # Criando e adicionando um circulo no meio do gráfico de raio 0.5
    circle = plt.Circle((0, 0), 0.5, color='white')
    plt.gca().add_artist(circle)

    # Calculando o valor total e adicionando o rótulo no centro do gráfico
    total = df[y].sum()
    label = format_currency(total, 'BRL', locale='pt_BR') if formato_moeda else f'{int(total)} unidades'
    plt.text(0, 0, f'Total:\n{label}', ha='center', va='center', fontsize=12)

    # Adicionando o título e salvando o gráfico como um arquivo PNG
    plt.title(title)
    plt.savefig(f'Distribuicao_{x}_{y}.png', dpi=300, bbox_inches='tight')

    # Fechando o gráfico
    plt.close()

# Configurando o estilo do gráfico
plt.rc('font', family='serif')

# Diretório para armazenar os arquivos CSV
diretorio = 'dados_vendas_sinteticos'
dfs = []

# Lendo os arquivos CSV
for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        try:
            dfs.append(pd.read_csv(caminho_arquivo))
        except pd.errors.EmptyDataError:  # verificando se o arquivo é vazio e se for, ignora o arquivo
            print(f"O arquivo {arquivo} está vazio e será ignorado.")
        except Exception as e:  # caso de erro, imprime o erro
            print(f"Erro ao ler o arquivo {arquivo}: {e}")

# Verificando se os arquivos foram carregados corretamente
if not dfs:
    raise ValueError("Nenhum dado CSV foi carregado.")

# Concatenando os dataframes
df_completo = pd.concat(dfs, ignore_index=True)

# Verificando se o dataframe contém as colunas 'Região', 'Vendas' e 'Produto'
if 'Região' not in df_completo.columns or 'Vendas' not in df_completo.columns or 'Produto' not in df_completo.columns:
    raise ValueError("O dataframe não contém as colunas 'Região', 'Vendas' ou 'Produto'.")

# Analise dos dados
# Total de vendas por região
total_vendas_por_regiao = df_completo.groupby('Região')['Vendas'].sum().reset_index() # Agrupando por região e somando
# as vendas, criando um novo dataframe e resetando o index

# Identificação dos produtos mais vendidos
produtos_mais_vendidos = df_completo['Produto'].value_counts().reset_index()
produtos_mais_vendidos.columns = ['Produto', 'Quantidade']
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='Quantidade', ascending=False)

# Criando os graficos de barras
grafico_barras(total_vendas_por_regiao, 'Vendas', 'Região', 'Vendas (R$)', 'Região',
               'Total de Vendas por Região', plt.cm.Set3.colors, formato_moeda=True)
grafico_barras(produtos_mais_vendidos, 'Quantidade', 'Produto', 'Quantidade', 'Produtos',
               'Produtos mais Vendidos - Quantidade', plt.cm.Set2.colors, formato_moeda=False)

# Criando os graficos de pizza
grafico_pizza(total_vendas_por_regiao, 'Região', 'Vendas', 'Distribuição do Total de Vendas por Região',
              plt.cm.Set3.colors, formato_moeda=True)
grafico_pizza(produtos_mais_vendidos, 'Produto', 'Quantidade', 'Distribuição dos Produtos mais Vendidos',
              plt.cm.Set2.colors, formato_moeda=False)

# Salvando os dados em arquivos CSV
total_vendas_por_regiao.round(2).to_csv('Total_Vendas_por_Regiao.csv', index=False)
produtos_mais_vendidos.round(2).to_csv('Produtos_Mais_Vendidos.csv', index=False)
