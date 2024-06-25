#!/bin/bash

# Função para verificar o status de serviços específicos.
# Esta função verifica se os serviços Apache2 e MySQL estão em execução.

check_services() {
  services=("apache2" "mysql")

  for service in "${services[@]}"; do
    if systemctl is-active --quiet $service; then
      echo "$service está em execução."
    else
      echo "$service não está em execução."
    fi
  done
}

# Chama a função para verificar os servicos
check_services

# Função para realizar backups do diretório dados_vendas_sinteticos e salvar no diretório backup.
backup_files() {
  tar -czf backup/dados_vendas_sinteticos_$(date +%F).tar.gz ../dados_vendas_sinteticos
  # enviar para object storage para armazenamento de longa data (cold storage), como S3 da amazon.
  # remover o .tar.gz após backup bem sucedido
}

# Chama a função para realizar backups
backup_files

# Função para monitorar o uso de recursos (CPU, memória, espaço em disco).
# Esta função imprime as informações de CPU, memória, espacamento em disco e uso de memória.
monitor_resources() {
  echo "Uso de CPU e memória:"
  top -b -n1 | head -n 10

  echo "Espaço em disco:"
  df -h

  echo "Uso de memória:"
  free -h
}

# Chama a função para monitorar os recursos
monitor_resources

# Função para verificar e instalar atualizações de segurança
# Pode usar sem o sudo caso voce seja root, o sudo permite executar com privilegios de superusuario,
update_system() {
  sudo apt update && apt list --upgradable
  sudo apt upgrade -y
}

