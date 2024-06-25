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

check_services

# Função para realizar backups do diretório dados_vendas_sinteticos e salvar no diretório backup.
backup_files() {
  tar -czf backup/dados_vendas_sinteticos_$(date +%F).tar.gz ../dados_vendas_sinteticos
}

backup_files