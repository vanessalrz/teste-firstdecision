import numpy as np
import os
import pandas as pd

# para gerar os dados que vão para os arquivos CSV, vou criar uma função chamada "gerar_dados_sinteticos".
def gerar_dados_sinteticos(num): # num serã o nũmero de vendas ou "linhas" que será gerado em cada CSV
    regioes = ['Norte', 'Sul', 'Centro-Oeste', 'Nordeste', 'Sudeste'] # lista contendo as 5 regiões
    produtos = ['Produto_A', 'Produto_B', 'Produto_C', 'Produto_D', 'Produto_E', 'Produto_F', 'Produto_G', 'Produto_H'] # lista contendo 8 produtos
    dados = {
        'Região': np.random.choice(regioes, num), # escolhe uma das 5 regioes aleatoriamente, podendo repetir (padrão do random.choice - True)
        'Produto': np.random.choice(produtos, num), # escolhe um dos 8 produtos aleatoriamente, podendo repetir
        'Vendas': np.random.uniform(0, 500, num) # gera um valor, não inteiro, entre 0 e 500, com o tamanho de num_rows
    } # cria um dicionário com 3 colunas: Região, Produto e Vendas

    return pd.DataFrame(dados) # retorna um dataframe (organiza dados em linhas e colunas) com os dados gerados



diretorio = 'dados_vendas_sinteticos' # diretório para armazenar os arquivos CSV
os.makedirs(diretorio, exist_ok=True) # cria o diretório se ele não existir


num_arquivos = 10 # escolhi gerar 10 arquivos CSV
num_dados_por_arquivo = 100 # escolhi gerar 100 vendas por arquivo CSV

# vou iniciar um loop que vai iterar sobre uma sequência de números gerada pela função range, nesse caso de 1 a 10.
for i in range(1, num_arquivos + 1): # como range(start, stop) não inclui o stop e queremos ir até 10, usamos num_arquivos + 1 como o valor de stop
    try: # tenta executar o código abaixo
        df = gerar_dados_sinteticos(num_dados_por_arquivo) # chamo a função gerar_dados_sinteticos e passo o valor de num que é num_dados_por_arquivo
        file_name = f'{diretorio}/vendas_{i}.csv' # concateno o diretório com o nome do arquivo CSV, para que fique assim: dados_vendas_sinteticos/vendas_1.csv
        df.to_csv(file_name, index=False) # salvo o dataframe em no arquivo CSV
        print("Arquivos CSV criados com sucesso!")  # imprime na tela a mensagem: "Arquivos CSV criados com sucesso!"
    except Exception as e: # caso de erro
        print(f"Erro ao criar o arquivo {file_name}: {e}") # imprime na tela o erro: "Erro ao criar o arquivo dados_vendas_sinteticos/vendas_1.csv: "Error X" "

print("Processo concluído!") # imprime na tela a mensagem: "Processo concluído!" ao final da execução