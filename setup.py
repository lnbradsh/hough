from setuptools import setup, find_packages

version = '0.1.0'

setup(name="hough",
      version=version,
      description="Implementation of the Hough algorithm",
      author="Layne Bradshaw",
      author_email="lnbradsh@asu.edu",
      packages=find_packages(),
      install_requires=['numpy>=1.6', 'scipy',
      ],
)
