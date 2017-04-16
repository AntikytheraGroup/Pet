#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'Pet',
    version = '0.0.1',
    url = '',
    license = 'GPLv3',
    description = 'A deep learning project managment framework.',
    author='Joshua Howard and Kevin Flansburg',
    author_email='joshthoward@gmail.com',
    packages=find_packages(),
    install_requires = ['setuptools', 'argparse'],
    entry_points={
        'console_scripts': [
            'pet = pet.main:main',
        ],
    },
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Topic :: Software Development :: Deep Learning',
    ]
)
