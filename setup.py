from setuptools import find_packages, setup

setup(
    name='repodeploy',
    version='1.0.0',
    author='Giacomo Di Prinzio',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)