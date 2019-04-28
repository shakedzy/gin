from pkg_resources import DistributionNotFound, get_distribution
from setuptools import setup, find_packages

VERSION = 'alpha'


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


install_deps = ['numpy', 'tensorflow']
if get_dist('tensorflow') is None and get_dist('tensorflow-gpu') is not None:
    install_deps.remove('tensorflow')

setup(name='gin',
      version=VERSION,
      description='Reinforcement Learning Models Library',
      author='Shaked Zychlinski',
      author_email='shakedzy@gmail.com',
      url='https://github.com/shakedzy/gin',
      packages=find_packages(),
      install_requires=install_deps)
