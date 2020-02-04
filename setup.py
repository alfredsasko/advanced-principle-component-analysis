from setuptools import setup
from os import path

PROJECT_URLS = {
    'Source Code': 'https://github.com/scikit-learn/scikit-learn'
}


# read the contents of your README file
__file__ = 'C:/Users/Fredo/Google Drive/Knowledge Center/' \
           'Data Scientist Nanodegree/pr-pypi-package/README.md'
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'advanced_pca',
  packages = ['advanced_pca'],
  version = '0.1.0',
  license='MIT',
  description = 'PCA with varimax rotation and feature selection '  \
                'compatible with scikit-learn',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alfred Sasko',
  author_email = 'alfred.sasko@gmail.com',
  url = 'https://github.com/alfredsasko',
  project_urls=PROJECT_URLS,
  keywords = ['Principle Component Analysis',
              'Matrix rotation',
              'Feature selection',
              'PCA',
              'scikit-learn'],
  install_requires=['rpy2'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  zip_safe=False,
)
