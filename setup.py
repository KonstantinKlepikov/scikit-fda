# encoding: utf-8

"""
Functional Data Analysis Python package.

Functional Data Analysis, or FDA, is the field of Statistics that analyses
data that depend on a continuous parameter.

This package offers classes, methods and functions to give support to FDA
in Python. Includes a wide range of utils to work with functional data, and its
representation, exploratory analysis, or preprocessing, among other tasks
such as inference, classification, regression or clustering of functional data.
See documentation or visit the
`github page <https://github.com/GAA-UAM/scikit-fda>`_ of the project for
further information on the features included in the package.

The documentation is available at
`fda.readthedocs.io/en/stable/ <https://fda.readthedocs.io/en/stable/>`_, which
includes detailed information of the different modules, classes and methods of
the package, along with several examples showing different funcionalities.
"""

import os
import sys

from Cython.Build import cythonize
from setuptools import setup, find_packages
from setuptools.extension import Extension

import numpy as np


needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

DOCLINES = (__doc__ or '').split("\n")

with open(os.path.join(os.path.dirname(__file__),
                       'VERSION'), 'r') as version_file:
    version = version_file.read().strip()

deps_path = 'deps'
fdasrsf_path = os.path.join(deps_path, 'fdasrsf')


extensions = [
    Extension(name='optimum_reparam',
              sources=[
                  os.path.join(fdasrsf_path, 'optimum_reparam.pyx'),
                  os.path.join(fdasrsf_path, 'dp_grid.c')
              ],
              include_dirs=[np.get_include()],
              language='c',
              ),
]

setup(name='scikit-fda',
      version=version,
      description=DOCLINES[1],
      long_description="\n".join(DOCLINES[3:]),
      url='https://fda.readthedocs.io',
      maintainer='Carlos Ramos Carreño',
      maintainer_email='vnmabus@gmail.com',
      ext_modules=cythonize(extensions),
      include_package_data=True,
      platforms=['any'],
      license='BSD',
      packages=find_packages(),
      python_requires='>=3.6, <4',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['numpy>=1.16',
                        'scipy>=1.3.0',
                        'scikit-learn>=0.20',
                        'pandas',
                        'matplotlib',
                        'scikit-datasets[cran]>=0.1.24',
                        'rdata',
                        'cython',
                        'mpldatacursor',
                        'multimethod>=1.2',
                        'findiff'],
      setup_requires=pytest_runner,
      tests_require=['pytest'],
      test_suite='tests',
      zip_safe=False)
