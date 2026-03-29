### Python file for KNN model
# Load in dataset
# preprocess
#   fill missing values
#
# use model
###

# importing
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# choosing dataset to use
print("Choose dataset to use: ")
print("\t1) World Happiness Report 2015\n" \
"\t2) World Happiness Report 2016\n" \
"\t3) World Happiness Report 2017\n" \
"\t4) World Happiness Report 2018\n" \
"\t5) World Happiness Report 2019\n")