# uchile-webscraping

Script para extraer los datos de la Universidad de Chile 2020-I 

## Instalar las librerías necesarias

```bash
pip install -r /path/to/requirements.txt
```

Si las librerías no se instalan correctamente  

```bash
pip install -r requirements.txt --no-index --find-links file://tmp/packages
```

## Datos Disponibles

Fuente 1: [ResultadosUChile20201](https://uchile.cl/transparencia/ResultadosUChile20201/index.html)
Fuente 2: [ResSimulacroPreUChile](https://uchile.cl/transparencia/ResSimulacroPreUChile/index.html)

```python
from uchile import UChile
data = UChile('ResultadosUChile20201')
data.importarTodo() # Importará todos los resultados
```
