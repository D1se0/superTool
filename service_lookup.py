# service_lookup.py

import argparse

# Definir un diccionario de puertos conocidos y servicios asociados
SERVICE_PORTS = {
    20: "FTP (File Transfer Protocol)",
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Hypertext Transfer Protocol)",
    443: "HTTPS (HTTP Secure)",
    3306: "MySQL Database",
    5432: "PostgreSQL Database",
    # Puedes agregar más puertos y servicios según sea necesario
}

def get_service_by_port(port):
    try:
        port = int(port)
        if port in SERVICE_PORTS:
            return SERVICE_PORTS[port]
        else:
            return "Servicio desconocido"
    except ValueError:
        return "Puerto inválido"

def main():
    parser = argparse.ArgumentParser(description="Identificar servicio por número de puerto")
    parser.add_argument("port", type=int, help="Número de puerto a consultar")
    args = parser.parse_args()

    port = args.port
    service = get_service_by_port(port)
    print(f"El puerto {port} está asociado al servicio: {service}")

if __name__ == "__main__":
    main()
