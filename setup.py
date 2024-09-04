from setuptools import setup

setup(
    name='luisasr',
    version='0.1',
    packages=['dev_aberto'],
    install_requires=[
        'requests',
    ],
    scripts=['dev_aberto/scripts/hello.py'],
)