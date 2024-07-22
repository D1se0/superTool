#!/bin/python3

import argparse
import subprocess
import sys
from termcolor import colored
from utils import validate_ip
import scanner
import scanner_advance as advanced_scanner
import exploits
import exploit_web  # Importar exploit_web
import signal
import os

def print_logo():
    logo = """
███████╗██╗   ██╗██████╗ ██╗     ███████╗
██╔════╝██║   ██║██╔══██╗██║     ██╔════╝
█████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══╝  ██║   ██║██╔═══╝ ██║     ██╔══╝  
███████╗╚██████╔╝██║     ███████╗███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝
    """
    version_info = "superTool v1.0\nBy Diseo (@d1se0)"
    print(colored(logo, "cyan"))
    print(colored(version_info, "yellow"))

def signal_handler(sig, frame):
    print("\n[+] Saliendo...")
    sys.exit(0)

def main():
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Print the logo and version info
    print_logo()

    parser = argparse.ArgumentParser(description="Herramienta de Hacking Ético")
    parser.add_argument("target", nargs='?', help="Dirección IP del objetivo")
    parser.add_argument("-ex", "--exploit", action="store_true", help="Buscar exploits para la IP")
    parser.add_argument("-s", "--scan", action="store_true", help="Realizar escaneo avanzado de la IP")
    parser.add_argument("-w", "--web-exploit", action="store_true", help="Buscar exploits para vulnerabilidades web")
    parser.add_argument("--url", help="URL del sitio web a escanear y buscar exploits (requerido con -w)")
    parser.add_argument("--service-port", type=int, help="Consultar servicio asociado al puerto")
    parser.add_argument("-r", "--range", help="Buscar dispositivos en el rango de IP especificado")
    args = parser.parse_args()

    if args.service_port:
        print(colored(f"Consultando servicio para el puerto: {args.service_port}", "blue"))
        service_lookup_cmd = f"python service_lookup.py {args.service_port}"
        subprocess.run(service_lookup_cmd, shell=True)
        return

    if args.web_exploit:
        if not args.url:
            parser.error("El parámetro --url es obligatorio cuando se usa -w/--web-exploit")
        print(colored(f"Ejecutando web_exploit.py para la URL: {args.url}", "blue"))
        exploit_web.scan_web_vulnerabilities(args.url)
        exploit_web.search_web_exploits(args.url)
        return

    if args.range:
        print(colored(f"Buscando dispositivos en el rango de IP: {args.range}", "blue"))
        ident_cmd = f"python identificated_ip.py {args.range}"
        subprocess.run(ident_cmd, shell=True)
        return

    if args.target is None:
        parser.error("El parámetro target es obligatorio a menos que se use -w/--web-exploit con --url")

    target = args.target

    if not validate_ip(target):
        print(colored("[ERROR] Dirección IP inválida. Por favor, introduce una dirección IP válida.", "red"))
        return

    if args.exploit:
        print(colored(f"Realizando escaneo de la IP: {target}", "blue"))
        service_info = scanner.scan_target(target)

        if service_info is None:
            print(colored("[ERROR] No se pudo obtener información del escaneo.", "red"))
            return

        print(colored(f"Buscando exploits para la IP: {target}", "blue"))
        exploits.exploit_vulnerabilities(target, service_info)

    if args.scan:
        print(colored(f"Realizando escaneo avanzado de la IP: {target}", "blue"))
        service_data = advanced_scanner.scan_target(target)

        if service_data is None:
            print(colored("[ERROR] No se pudo realizar el escaneo.", "red"))
            return

        open_ports = advanced_scanner.get_open_ports(service_data)
        if open_ports:
            nmap_cmd = ['nmap', '-sCV', f'-p{open_ports}', target]
            subprocess.run(nmap_cmd)
        else:
            print(colored("[ERROR] No se encontraron puertos abiertos para escanear.", "red"))

if __name__ == "__main__":
    main()
