# Crear y activar el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

# Instalar paquetes y agregarlos a requirements.txt:
```bash
pip install pip-tools
cd software
pip freeze > requirements.txt
```

# Instalar los paquetes de requirements.txt
```bash
source venv/bin/activate
cd software
pip install -r requirements.txt
```

# Ejecutar el proyecto
```bash
python -m software.src.main
```