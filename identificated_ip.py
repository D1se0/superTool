# identificated_ip.py

import sys
import subprocess
from termcolor import colored

def scan_network(ip_range):
    print(colored(f"Escaneando la red: {ip_range}", "blue"))
    nmap_cmd = f"nmap -sn {ip_range}"
    subprocess.run(nmap_cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(colored("[ERROR] Uso incorrecto. Uso: python identificated_ip.py <IP_RANGE>", "red"))
        sys.exit(1)

    ip_range = sys.argv[1]
    scan_network(ip_range)
