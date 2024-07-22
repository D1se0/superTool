# SuperTool

 <!-- Reemplaza esta URL con la URL de tu imagen -->

## Descripción

`SuperTool` es una herramienta de `hacking ético` diseñada para realizar escaneos avanzados de `red`, buscar `vulnerabilidades` en `sitios web` y gestionar `exploits`. Utiliza herramientas como `nmap` para el escaneo de redes y searchsploit para buscar exploits.

## Funciones

Escaneo de Redes: Identifica dispositivos en una red utilizando `Nmap`.

Escaneo Avanzado de Puertos: Detecta puertos abiertos y servicios asociados.

Búsqueda de Vulnerabilidades Web: Escanea sitios web en busca de `vulnerabilidades` y `exploits`.

Consulta de Servicios: Identifica el servicio asociado a un puerto específico.

Exploit de Vulnerabilidades: Busca `exploits` disponibles para servicios específicos.

## Instalación

Para instalar `SuperTool` y todas sus dependencias, ejecuta el siguiente script:

```bash
git clone https://github.com/D1se0/superTool.git
cd superTool/
```

```bash
sudo bash requirements.sh
```

o

```bash
sudo su
./requirements.sh
```

Este script instalará todas las librerías necesarias y copiará los scripts a `/usr/local/bin/superTool`. También creará un enlace simbólico para facilitar la ejecución del script principal desde cualquier ubicación.

## Uso

### Parámetros

`-r`: Buscar dispositivos en un rango de IP especificado.

`-ex`: Buscar exploits para la IP especificada.

`-s`: Realizar un escaneo avanzado de la IP especificada.

`-w`: Buscar vulnerabilidades web para la URL especificada.

`--url`: URL del sitio web a escanear y buscar exploits (requerido con -w).

`--service-port`: Consultar servicio asociado al puerto.

## Ejemplos de Uso

### Escanear un rango de IP

```bash
python3 superTool.py -r 192.168.1.0/24
```

Este comando escaneará el rango de IP `192.168.1.0/24` para encontrar dispositivos activos.

### Buscar exploits para una IP

```bash
python3 superTool.py -ex 192.168.1.10
```
Este comando buscará exploits para la IP `192.168.1.10`.

### Realizar un escaneo avanzado de una IP

```bash
python3 superTool.py -s 192.168.1.10
```

Este comando realizará un escaneo avanzado de la IP `192.168.1.10` y detectará puertos abiertos.

### Buscar vulnerabilidades web para una URL

```bash
python3 superTool.py -w --url http://example.com
```

Este comando escaneará la URL `http://example.com` para encontrar vulnerabilidades web. `Nota: El parámetro --url es obligatorio cuando se usa -w`.

### Consultar servicio asociado a un puerto

```bash
python3 superTool.py --service-port 80
```

Este comando consultará el servicio asociado al puerto `80`.

## Mantenimiento

Si encuentras algún error o tienes sugerencias, por favor, abre un problema en el repositorio de GitHub.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, consulta el `CONTRIBUTING.md` para obtener más detalles sobre cómo contribuir.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para obtener detalles.
