from setuptools import setup, find_packages

setup(name='discover-containers',
    version = '1.0',
    py_modules = ['discover_containers'],
    install_requires = ['PyYAML'],
    scripts = ['discover_containers.py'],
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'discover-containers = discover_containers:main'
        ]
    }
)
