from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requrements = f.read().splitlines()

setup(
    name = "MLOPS-Project-1", 
    version="0.1", 
    author="Mausham Kumar", 
    packages = find_packages(), 
    install_requires = requrements
    
)