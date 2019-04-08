from pkg_resources import DistributionNotFound, get_distribution
from setuptools import setup, find_packages

VERSION = 'alpha'


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


install_deps = ['numpy']
if get_dist('tensorflow') is None and get_dist('tensorflow-gpu') is None:
    install_deps.append('tensorflow')

setup(name='warehouse',
    version=VERSION,
    description='Models Warehouse',
    author='Shaked Zychlinski',
    author_email='shakedzy@gmail.com',
    url='https://github.com/shakedzy/warehouse',
    packages=find_packages(),
    install_requires=install_deps)
