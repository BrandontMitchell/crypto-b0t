from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crypto b0t',
    version='0.1.0',
    description='Automated Crypto Exchange System',
    long_description=readme,
    authors='Fadel Shtiui, Maksim Vengrovski, Brandon Mitchell',
    author_email='btmbaseball99@gmail.com',
    url='https://github.com/BrandontMitchell/crypto-b0t',
    license=license,
    packages=find_packages(exclude=('tests', 'crypto/bot'))
)