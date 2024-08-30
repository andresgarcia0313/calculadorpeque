# setup.py

from setuptools import setup, find_packages

setup(
    name="quickcalc",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tk",  # Esta es la forma de especificar la dependencia para python3-tk
    ],
    entry_points={
        "console_scripts": [
            "quickcalc=main:main",
        ],
    },
)
