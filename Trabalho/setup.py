from setuptools import setup, find_packages

setup(
    name = 'Jogo da Velha',
    version = '0.1',
    description = 'Um jogo da velha para jogadores humanos ou computador',
    install_requires = ['random'],
    packages = find_packages()
)