#!/bin/bash

# Verificar si el script se está ejecutando como root
if [ "$(id -u)" -ne "0" ]; then
    echo "[ERROR] Este script debe ser ejecutado como root."
    exit 1
fi

# Instalación de las dependencias
echo "Instalando dependencias..."

# Actualizar la lista de paquetes e instalar pip y nmap
apt-get update
apt-get install -y python3-pip nmap

# Instalar las librerías necesarias
pip3 install termcolor argparse

# Crear un directorio para los scripts y módulos
echo "Creando directorio /usr/local/bin/superTool/"
mkdir -p /usr/local/bin/superTool

# Copiar todos los scripts al directorio
echo "Copiando los scripts a /usr/local/bin/superTool/"
cp superTool.py utils.py service_lookup.py scanner.py scanner_advance.py exploits.py exploit_web.py identificated_ip.py /usr/local/bin/superTool/

# Crear un enlace simbólico en /usr/bin/
echo "Creando enlace simbólico en /usr/bin/"
ln -s /usr/local/bin/superTool/superTool.py /usr/bin/superTool

# Hacer el script ejecutable
chmod +x /usr/bin/superTool

echo "Proceso completado exitosamente."
