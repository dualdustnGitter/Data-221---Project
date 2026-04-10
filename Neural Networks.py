#importing
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import math

#read files
happiness_2015_data = pd.read_csv("WorldHappinessReport_2015.csv")
happiness_2016_data = pd.read_csv("WorldHappinessReport_2016.csv")
happiness_2017_data = pd.read_csv("WorldHappinessReport_2017.csv")
happiness_2018_data = pd.read_csv("WorldHappinessReport_2018.csv")
happiness_2019_data = pd.read_csv("WorldHappinessReport_2019.csv")

# User chooses which dataset to predict
print("Choose dataset to use: ")
print("\t1) World Happiness Report 2015\n" \
"\t2) World Happiness Report 2016\n" \
"\t3) World Happiness Report 2017\n" \
"\t4) World Happiness Report 2018\n" \
"\t5) World Happiness Report 2019\n")


# Choose dataset and load it with feature matrix and label
while True: # loop till valid input (1-5)
    chosen_Dataset = input("Enter Number (1-5): ")
    if (chosen_Dataset == "1"): # if choosing 2015
        chosen_Dataset = "WorldHappinessReport_2015.csv" # file to open/load

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,[ # feature matrix has features that actually matter
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        y = chosen_happiness_data["Happiness Score"] # label

        break # break of loop
    elif (chosen_Dataset == "2"): # if choosing 2016
        chosen_Dataset = "WorldHappinessReport_2016.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,[
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        y = chosen_happiness_data["Happiness Score"]

        break
    elif (chosen_Dataset == "3"): # if choosing 2017
        chosen_Dataset = "WorldHappinessReport_2017.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        #print("\"Country\"")
        X = chosen_happiness_data.loc[:,["Economy..GDP.per.Capita.",
                                               "Family","Health..Life.Expectancy.",
                                               "Freedom",
                                               "Generosity",
                                               "Trust..Government.Corruption.",
                                               "Dystopia.Residual"]]
        y = chosen_happiness_data["Happiness.Score"]

        break
    elif (chosen_Dataset == "4"): # if choosing 2018
        chosen_Dataset = "WorldHappinessReport_2018.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,[
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        y = chosen_happiness_data["Score"]

        break
    elif (chosen_Dataset == "5"): # if choosing 2019
        chosen_Dataset = "WorldHappinessReport_2019.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pd.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,[
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        y = chosen_happiness_data["Score"]

        break
    else:
        print("Invalid input, please try again (1-5) \n") # if invalid input restart loop, ask for input again

#split data,scale features
X = X.select_dtypes(include=[np.number]) # keep only numbers
X = X.fillna(X.mean()) #fill missing blanks
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = MLPRegressor(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=2000, random_state=42)
model.fit(X_train, y_train)
y_pre = model.predict(X_test)

print(f"R2 score:{r2_score(y_test, y_pre)}")
print(f"MAE:{mean_absolute_error(y_test, y_pre)}")
print(f"MSE:{mean_squared_error(y_test, y_pre)}")

#graph: actual vs predicted
plt.figure(figsize=(8,6))
plt.plot(range(len(y_test)), y_test.values, marker='o', color='blue', label="actual")
plt.plot(range(len(y_pre)), y_pre, marker='o', color='red', label="predicted")
plt.xlabel("Test Data Index")
plt.ylabel("Happiness Score")
plt.title("Actual vs Predicted Happiness Score")
plt.legend()
plt.show()