# Advanced Priniciple Component Analysis

### Table of Contents
1. [Project Motivation](#motivation)
2. [Usage](#usage)
4. [Installation](#installation)
3. [File Descriptions](#files)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Project Motivation<a name="motivation"></a>

Researchers use Principle Component Analysis (PCA) intending to summarize features, identify structure in data or reduce the number of features. The interpretation of principal components is challenging in most of the cases due to the high amount of cross-loadings (one feature having significant weight across many principal components). Different types of matrix rotations are used to minimize cross-loadings and make factor interpretation easier. 

The `custom_PCA` class is the child of `sklearn.decomposition.PCA` and uses varimax rotation and enables dimensionality reduction in complex pipelines with the modified `transform` method.

`custom_PCA` class implements:
 - __varimax rotation__ for better interpretation of principal components
 - dimensionality reduction based on siginificant __feature communalities__ > 0.5
 - dimensionality reduction based on __feature weights significance__ calculated based on sample size
 - __surrogate feature selection__ - only features with maximum laoding are selected instead of principal components
 
## Usage <a name="usage"></a>

### Example of using varimax rotation:
```
import pandas as pd
from sklearn.preprocessing import StandardScaler
from custom_pca import CustomPCA

X = pd.read_csv('data.txt')
X_std = StandardScaler().fit_transform(X)
pca = CustomPCA(rotation='Varimax').fit(X_std)
print(pca.components_)
```

### Example of dimensionality reduction based on features' weights and communalities significance:
```
pca = CustomPCA(feature_selection='significant').fit(X_std)
print(pca.communalities_)
print(X.columns[pca.get_support()]
print(pca.transform(X_std))
```

### Example of selection method of surrogate features:
```
pca = CustomPCA(feature_selection='surrogate').fit(X_std)
print(X.columns[pca.get_support()]
print(pca.transform(X_std))
```

## Installation <a name="installation"></a>

There are several necessary 3rd party libraries beyond the Anaconda distribution of Python which needs to be installed and imported to run code. These are:
 - [rpy2](https://pypi.org/project/rpy2/) Python interface to the R language used to calculate the varimax rotation
 
```
pip install custom-pca
```
 
## File Descriptions <a name="files"></a>

There are additional files:
 - `custom_pca.py` advanced principle component analysis class definition
 - `licence.txt` see MIT lincence to follow
 - `setup.cfg` and `setup.py` used for creating PyPi package
 
## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to [Joseph F. Hair Jr, William C. Black, Barry J. Babin, Rolph E. Anderson](https://www.amazon.com/Multivariate-Data-Analysis-Joseph-Hair/dp/0138132631).
The ones using projects shall follow [MIT lincence](https://github.com/alfredsasko/advanced-principle-component-analysis/blob/master/license.txt)
