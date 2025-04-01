from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    packages=find_packages(),
    description='A description of your project',
    install_requires=[
        'qsharp',
        'tensorflow'
    ],
)
