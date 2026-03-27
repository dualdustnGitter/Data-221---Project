### Python file for Decision Tree model
# Load in dataset
# preprocess
#   fill missing values
# 
# use model
###

# importing
import pandas

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error, root_mean_squared_error

# from tensorflow.keras.utils import to_categorical


# happiness_2015_data = pandas.read_csv("WorldHappinessReport_2015.csv")
# happiness_2016_data = pandas.read_csv("WorldHappinessReport_2016.csv")
# happiness_2017_data = pandas.read_csv("WorldHappinessReport_2017.csv")
# happiness_2018_data = pandas.read_csv("WorldHappinessReport_2018.csv")
# happiness_2019_data = pandas.read_csv("WorldHappinessReport_2019.csv")


# choosing dataset to use
print("Choose dataset to use: ")
print("\t1) World Happiness Report 2015\n" \
"\t2) World Happiness Report 2016\n" \
"\t3) World Happiness Report 2017\n" \
"\t4) World Happiness Report 2018\n" \
"\t5) World Happiness Report 2019\n")


# choose dataset and load it with feature matrix and label
while True: # loop till valid input (1-5)
    chosen_Dataset = input()
    if (chosen_Dataset == "1"): # if choosing 2015
        chosen_Dataset = "WorldHappinessReport_2015.csv" # file to open/load

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:,[ # feature matrix has features that actually matter
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        target_happiness = chosen_happiness_data.loc[:,["Happiness Score"]] # label

        break # break of loop
    elif (chosen_Dataset == "2"):
        chosen_Dataset = "WorldHappinessReport_2016.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:,[
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        target_happiness = chosen_happiness_data.loc[:,["Happiness Score"]]

        break
    elif (chosen_Dataset == "3"):
        chosen_Dataset = "WorldHappinessReport_2017.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:,[
                                               "Economy..GDP.per.Capita.",
                                               "Family","Health..Life.Expectancy.",
                                               "Freedom",
                                               "Generosity",
                                               "Trust..Government.Corruption.",
                                               "Dystopia.Residual"]]
        target_happiness = chosen_happiness_data.loc[:,["Happiness.Score"]]

        break
    elif (chosen_Dataset == "4"):
        chosen_Dataset = "WorldHappinessReport_2018.csv"

        print("Loading.. " + chosen_Dataset)
        precleaned_chosen_happiness_data = pandas.read_csv(chosen_Dataset) # 2018 dataset has missing values
        chosen_happiness_data = precleaned_chosen_happiness_data.dropna() # clean it

        feature_matrix = chosen_happiness_data.loc[:,[
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        target_happiness = chosen_happiness_data.loc[:,["Score"]]


        break
    elif (chosen_Dataset == "5"):
        chosen_Dataset = "WorldHappinessReport_2019.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:,[
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        target_happiness = chosen_happiness_data.loc[:,["Score"]]

        break
    else:
        print("Invalid input, please try again (1-5) \n") # if invalid input restart loop, ask for input again



# split data
features_train, features_test, labels_train, labels_test = train_test_split(feature_matrix, target_happiness, test_size=0.3, random_state=42)


# Build decision tree
decision_tree_regressor = DecisionTreeRegressor(criterion="absolute_error", max_depth=7, random_state=42)
decision_tree_regressor.fit(pandas.get_dummies(features_train, drop_first=True), labels_train)


# predict
predicted_labels = decision_tree_regressor.predict(features_test)

# get predict scores
# accuracy = accuracy_score(labels_test, predicted_labels)
score_of_model = decision_tree_regressor.score(features_test, labels_test) # r square score
score_of_model_MAE = mean_absolute_error(labels_test, predicted_labels) # MAE score of model
score_of_model_RMSE = root_mean_squared_error(labels_test, predicted_labels) # RMSE score of model


# print(accuracy)
print("Score of Decision tree Model: " + str(score_of_model))
print("MAE of Decision tree Model: " + str(score_of_model))
print("RMSE of Decision tree Model: " + str(score_of_model))