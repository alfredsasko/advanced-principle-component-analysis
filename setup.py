import base64
import requests

from setuptools import setup
from os import path

PROJECT_URLS = {
    'Source Code': 'https://github.com/alfredsasko/' \
                   'advanced-principle-component-analysis',
    'Documentation': 'https://pypi.org/project/advanced-pca/#description'
}


# read the contents of your README file
readme_url = ('https://api.github.com/repos/alfredsasko/'
              'advanced-principle-component-analysis/contents/README.md')

req = requests.get(readme_url)
if req.status_code == requests.codes.ok:
    req = req.json()
    long_description = base64.b64decode(req['content']).decode('u8')
else:
    long_description = 'Long Description Source File Not Found'

print(type(long_description))

setup(
  name = 'advanced_pca',
  packages = ['advanced_pca'],
  version = '0.1.4',
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
