The repository is for Yandex Cup Recommender System Challenge.
--- 
## Exploratory Data Analysis
There is Exploratory Data Analysis in `eda/`.

## Models
The two methods to solve the task were probed. 

#### Alternating Least Squares (ALS)
ALS with Latent Factor Model were implemented from scratch. Original version aims to predict the rating from 1 to 5 directly. Binary version predicts binary label whether the user rated the organization 4 or 5. 

#### Factorization Machines, libFM approach
This model gives better results as it can naturally incorporate extra information such as feature description of the user/organization. 

Python package **fastFM** was used as faster and handier alternative to libFM (the algorithms are the same). fastFM works with scipy.sparse matrices, so there is notebook performing the necessary transformations.

Model hyperparameters were optimized with **optuna**.

## Metric
The used metric is Mean Normalized Average Precision (MNAP). Implementation is in `scripts/mnap.py`.

