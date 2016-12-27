from setuptools import setup, find_packages
import os

with open(os.path.join('version.txt')) as version_file:
    version_from_file = version_file.read().strip()

with open('requirements.txt') as f_required:
    required = f_required.read().splitlines()



setup(
    name='cloudshell-networking-huawei-vrp',
    url='http://www.qualisystems.com/',
    author='QualiSystems',
    author_email='info@qualisystems.com',
    packages=find_packages(),
	install_requires=required,
    version=version_from_file,
    description='QualiSystems networking huawei VRP specific Package',
    include_package_data = True
)