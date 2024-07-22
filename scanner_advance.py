# scanner_advance.py

import nmap

def scan_target(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-sCV')
    
    service_data = []
    if ip_address in nm.all_hosts():
        for proto in nm[ip_address].all_protocols():
            lport = nm[ip_address][proto].keys()
            for port in lport:
                service_info = {
                    'port': port,
                    'name': nm[ip_address][proto][port]['name'],
                    'version': nm[ip_address][proto][port]['version'],
                    'state': nm[ip_address][proto][port]['state'],
                }
                service_data.append(service_info)
        return service_data
    else:
        return None

def get_open_ports(service_data):
    open_ports = []
    for service in service_data:
        if service['state'] == 'open':
            open_ports.append(service['port'])
    return ','.join(map(str, open_ports))
