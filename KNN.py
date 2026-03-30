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

# choose dataset and load it with feature matrix and label
while True:  # loop till valid input (1-5)
    chosen_Dataset = input()
    if (chosen_Dataset == "1"):  # if choosing 2015
        chosen_Dataset = "WorldHappinessReport_2015.csv"  # file to open/load

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:, [
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity"
        ]]
        target_happiness = chosen_happiness_data.loc[:, "Happiness Score"]

        break

    elif (chosen_Dataset == "2"):
        chosen_Dataset = "WorldHappinessReport_2016.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:, [
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity"
        ]]
        target_happiness = chosen_happiness_data.loc[:, "Happiness Score"]

        break

    elif (chosen_Dataset == "3"):
        chosen_Dataset = "WorldHappinessReport_2017.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:, [
            "Economy..GDP.per.Capita.",
            "Family",
            "Health..Life.Expectancy.",
            "Freedom",
            "Generosity",
            "Trust..Government.Corruption."
        ]]
        target_happiness = chosen_happiness_data.loc[:, "Happiness.Score"]

        break

    elif (chosen_Dataset == "4"):
        chosen_Dataset = "WorldHappinessReport_2018.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:, [
            "GDP per capita",
            "Social support",
            "Healthy life expectancy",
            "Freedom to make life choices",
            "Generosity",
            "Perceptions of corruption"
        ]]
        target_happiness = chosen_happiness_data.loc[:, "Score"]

        break

    elif (chosen_Dataset == "5"):
        chosen_Dataset = "WorldHappinessReport_2019.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:, [
            "GDP per capita",
            "Social support",
            "Healthy life expectancy",
            "Freedom to make life choices",
            "Generosity",
            "Perceptions of corruption"
        ]]
        target_happiness = chosen_happiness_data.loc[:, "Score"]

        break

    else:
        print("Invalid input, please try again (1-5) \n")

# split data
features_train, features_test, labels_train, labels_test = train_test_split(
    feature_matrix, target_happiness, test_size=0.3, random_state=42
)

# build KNN pipeline
knn_regressor = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=5, weights="distance"))
])