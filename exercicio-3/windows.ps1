
# Define os serviços a serem monitorados
$services = @("W3SVC", "MSSQLSERVER", "MySQL")

# Define os diretórios e arquivos importantes para backup
$backupItems = @("../dados_vendas_sinteticos")

# Diretório de destino para os backups
$backupDestination = "backup/"
