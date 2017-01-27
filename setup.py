from os import path
from setuptools import setup, find_packages
import pyoptmat

here = path.abspath(path.dirname(__file__))

# Get the long description from the RpythonEADME file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='rii_pandas',
      version=pyoptmat.__version__,
      description=('Python 3 + Pandas wrapper ' +
                   'for the refractiveindex.info database.'),
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='refractive index, dielectric constant, optical material',
      author=pyoptmat.__author__,
      author_email='mnishida@hiroshima-u.ac.jp',
      url='https://github.com/mnishida/refractiveindex.info-database',
      license=pyoptmat.__license__,
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      include_package_data=True,
      test_requires=['Nose'],
      zip_safe=False,
      install_requires=[
          'setuptools',
          'numpy',
          'scipy',
          'pandas',
          'yaml'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """
      )
