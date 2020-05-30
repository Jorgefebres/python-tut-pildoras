from setuptools import setup

setup(
    name="paquete_calculos",
    version="1.0",
    description="paquete de calculos matematicos basicos",
    author="Jorge Febres",
    author_email="jorge_febres@outlook.com",
    url="citas.clinicadac.com",
    packages=["calculos_modulo", "calculos_modulo.basicos_submodulo"]
)

# PARA CREAR EL ARCHIVO DISTRIBUIBLE:
# ir a la carpeta con la consola y ejecutar : python setup.py sdist

# PARA INSTALAR: ir a la carpeta dist y ejecutar:
#  pip install .\paquete_calculos-1.0.tar.gz

# PARA DESINSTALAR EL PAQUETE DEL SISTEMA:
# pip uninstall paquete_calculos
