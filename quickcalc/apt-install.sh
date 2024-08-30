#!/bin/bash

# Colores para la consola
COLOR_GREEN="\033[0;32m"
COLOR_CYAN="\033[0;36m"
COLOR_RESET="\033[0m"

# Actualizar lista de paquetes
echo -e "${COLOR_CYAN}Actualizando lista de paquetes...${COLOR_RESET}"
sudo apt-get update

# Leer paquetes desde apt-packages.txt
PACKAGES=$(cat apt-requirements.txt)

# Mostrar paquetes que se van a instalar
echo -e "\n${COLOR_GREEN}Paquetes a instalar:${COLOR_RESET}"
echo "${PACKAGES}"

# Instrucciones para ejecutar
echo -e "\n${COLOR_CYAN}Instrucciones a usar para instalar:${COLOR_RESET}"
echo "sudo apt-get install -y ${PACKAGES}"

# Instalar paquetes sin confirmación
echo -e "\n${COLOR_CYAN}Instalando paquetes...${COLOR_RESET}"
sudo apt-get install -y ${PACKAGES}
