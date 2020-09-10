from distutils.core import setup
from setuptools import find_packages


VERSION = '0.1.0'

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Environment :: Web Environment',
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

with open('README.rst', 'r') as f:
    long_desc = f.read()

setup(
    name='django-token-log',
    description='Log csrfmiddlewaretoken on POST to avoid reuse (double-commit, etc.)',
    long_description=long_desc,
    version=VERSION,
    author='Microdisseny',
    author_email='tech@microdisseny.com',
    license='BSD License',
    platforms=['OS Independent'],
    url='http://github.com/microdisseny/django-token-log',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
