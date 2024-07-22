# SuperTool

<p align="center">
  <img src="https://github.com/user-attachments/assets/60a13fab-2be8-4c63-9376-e1a4760ff431" alt="revShell" width="400">
</p>

## Description

`SuperTool` is an `ethical hacking` tool designed to perform advanced `network` scans, search for `vulnerabilities` in `websites` and manage `exploits`. Use tools like `nmap` for network scanning and searchsploit to look for exploits.

## Features

Network Scanning: Identify devices on a network using `Nmap`.

Advanced Port Scanning: Detects open ports and associated services.

Search for Web Vulnerabilities: Scans websites for `vulnerabilities` and `exploits`.

Service Query: Identifies the service associated with a specific port.

Exploit Vulnerabilities: Search for exploits available for specific services.

## Install

To install `SuperTool` and all its dependencies, run the following script:

```bash
git clone https://github.com/D1se0/superTool.git
cd superTool/
```

```bash
sudo bash requirements.sh
```

either

```bash
sudo su
./requirements.sh
```

This script will install all the necessary libraries and copy the scripts to `/usr/local/bin/superTool`. It will also create a symbolic link to make it easier to run the main script from any location.

## Use

### Parameters

`-r`: Search for devices in a specified IP range.

`-ex`: Search for exploits for the specified IP.

`-s`: Perform an advanced scan of the specified IP.

`-w`: Search for web vulnerabilities for the specified URL.

`--url`: URL of the website to scan for exploits (required with -w).

`--service-port`: Consult service associated with the port.

## Examples of Use

### Scan an IP range

```bash
python3 superTool.py -r 192.168.1.0/24
```

This command will scan the IP range `192.168.1.0/24` to find active devices.

### Search for exploits for an IP

```bash
python3 superTool.py -ex 192.168.1.10
```
This command will look for exploits for the IP `192.168.1.10`.

### Perform an advanced scan of an IP

```bash
python3 superTool.py -s 192.168.1.10
```

This command will perform an advanced scan of the IP `192.168.1.10` and detect open ports.

### Search for web vulnerabilities for a URL

```bash
python3 superTool.py -w --url http://example.com
```

This command will scan the URL `http://example.com` to find web vulnerabilities. `Note: The --url parameter is required when using -w`.

### Consult service associated with a port

```bash
python3 superTool.py --service-port 80
```

This command will query the service associated with port `80`.

## Maintenance

If you find any bugs or have suggestions, please open an issue in the GitHub repository.

## Contributions

Contributions are welcome! Please see the `CONTRIBUTING.md` for more details on how to contribute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
