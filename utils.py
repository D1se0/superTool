import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port):
    try:
        port = int(port)
        return 0 < port <= 65535
    except ValueError:
        return False
