import subprocess
from termcolor import colored
import re
import sys

def scan_target(ip):
    print(colored(f"Escaneando {ip}...", "green"))
    nmap_command = f"nmap -sV {ip}"
    result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
    
    service_info = []
    for line in result.stdout.splitlines():
        if re.search(r'^\d+/tcp', line) or re.search(r'^\d+/udp', line):
            parts = line.split()
            port = parts[0].split('/')[0]  # Obtener solo el número de puerto
            service_name = parts[2]  # Nombre del servicio (SSH, HTTP, etc.)
            service_version = extract_version(parts[3:], service_name)
            service = {
                'port': port,
                'name': service_name,
                'version': service_version
            }
            service_info.append(service)
    
    print(colored("[DEBUG] Información del servicio obtenida:", "cyan"))
    for service in service_info:
        print(f"  Port: {service['port']}, Name: {service['name']}, Version: {service['version']}")
    
    return service_info

def extract_version(parts, service_name=None):
    version = []
    skip_next = False
    for part in parts:
        if skip_next:
            skip_next = False
            continue
        if re.search(r'^\d+[a-zA-Z]*$', part):
            version.append(part)
            break
        elif version and re.search(r'^\d+\.\d+[a-zA-Z]*$', version[-1]):
            break
        elif '(' in part:
            break
        elif service_name == 'http' and part == 'Apache':
            continue  # Omitir la palabra 'Apache'
        elif part in ['Ubuntu', 'Debian']:
            skip_next = True
            continue
        version.append(part)
    return ' '.join(version)

def search_exploits(service_info, ip):
    print(colored("[INFO] Buscando exploits disponibles...", "blue"))
    
    for service in service_info:
        service_name = service['name']
        service_version = service['version']
        
        if service_version:
            # Construir comando para ejecutar searchsploit
            command = f"searchsploit {service_version}"
            print(colored(f"[DEBUG] Ejecutando: {command}", "cyan"))
            try:
                output = subprocess.check_output(command, shell=True, text=True)
                print(output)
            except subprocess.CalledProcessError as e:
                print(colored(f"[ERROR] Error al ejecutar searchsploit: {e}", "red"))
        else:
            print(colored(f"No se encontró versión para {service_name}. No se realizará búsqueda de exploits.", "yellow"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 scanner.py <dirección_IP>")
        sys.exit(1)
    
    ip = sys.argv[1]
    service_info = scan_target(ip)
    search_exploits(service_info, ip)
