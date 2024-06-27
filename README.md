Teste First Decision
====================

Esse é um repositório para armazenar os testes realizados para a vaga Analista Python.

## Instruções para rodar o exercício-1

1. Navegue até o diretório exercício-1: `cd exercicio-1`
2. Para gerar os dados sintéticos para a análise, execute o arquivo python "Gerando_Dados_Sinteticos.py": `python Gerando_Dados_Sinteticos.py`. O diretório "dados_vendas_sinteticos" será criado e os dados sintéticos serão armazenados nele.
3. Para realizar a análise dos dados, execute o arquivo python "Analise_Dados_Sinteticos.py" `python Analise_Dados_Sinteticos.py`. O código irá gerar 4 imagens e 2 arquivos CSV.

## Instruções para rodar o exercício-2

1. Navegue até o diretório exercício-2: `cd exercicio-2`
2. Inicie o container da aplicação: `docker compose up -d`
3. Faça uma ou mais requisições para o localhost para criar *TODO*s: `curl -X POST -H 'Content-Type: application/json' -d '{"todo": "foo bar baz"}' 127.0.0.1:5000/api/todo`
4. List os *TODO*s com: `curl -X GET -H 'Content-Type: application/json'  127.0.0.1:5000/api/todo`
5. Delete um *TODO* com: `curl -X DELETE -H 'Content-Type: application/json' 127.0.0.1:5000/api/todo/<todo-id>`

> [!INFO]
> O `-d` no comando `docker compose` cria os containers em modo *detached*, isto é, executa em background.

Execute `docker compose down` para remover os containers.

## Instruções para rodar o exercício-3

1. Navegue até o diretório exercício-3: `cd exercicio-3`
2. Torne o arquivo executável usando o comando _chmod +x_: `chmod +x linux.sh`
3. Execute o arquivo usando ./ seguido do nome do arquivo: `./linux.sh`
4. Dentro do arquivo _linux.sh_ eu mostro como faria para gerar relatórios periódicos sobre o estado dos servidores.

