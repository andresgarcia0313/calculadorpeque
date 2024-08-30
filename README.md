# Crear y activar el entorno virtual

python3 -m venv venv
source venv/bin/activate

# Instalar paquetes y agregarlos a requirements.txt:

pip install pip-tools
cd software
pip freeze > requirements.txt

# Instalar los paquetes de requirements.txt

source venv/bin/activate
cd software
pip install -r requirements.txt

# Ejecutar el proyecto

python -m software.src.main
