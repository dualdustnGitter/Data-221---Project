### Python file for Linear Repression model
# Load in dataset
# preprocess
#   fill missing values
# 
# use model
###

#Importing
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, mean_absolute_error

happiness_2015_data = pandas.read_csv("WorldHappinessReport_2015.csv")
happiness_2016_data = pandas.read_csv("WorldHappinessReport_2016.csv")
happiness_2017_data = pandas.read_csv("WorldHappinessReport_2017.csv")
happiness_2018_data = pandas.read_csv("WorldHappinessReport_2018.csv")
happiness_2019_data = pandas.read_csv("WorldHappinessReport_2019.csv")

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
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,["Country", # feature matrix has features that actually matter
                                               "Region",
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        y = chosen_happiness_data.loc[:,["Happiness Score"]] # label

        break # break of loop
    elif (chosen_Dataset == "2"): # if choosing 2016
        chosen_Dataset = "WorldHappinessReport_2016.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        feature_matrix = chosen_happiness_data.loc[:,["Country",
                                               "Economy (GDP per Capita)",
                                               "Family",
                                               "Health (Life Expectancy)",
                                               "Freedom",
                                               "Trust (Government Corruption)",
                                               "Generosity",
                                               "Dystopia Residual"]]
        target_happiness = chosen_happiness_data.loc[:,["Happiness Score"]]

        break
    elif (chosen_Dataset == "3"): # if choosing 2017
        chosen_Dataset = "WorldHappinessReport_2017.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        #print("\"Country\"")
        X = chosen_happiness_data.loc[:,["Country",
                                               "Economy..GDP.per.Capita.",
                                               "Family","Health..Life.Expectancy.",
                                               "Freedom",
                                               "Generosity",
                                               "Trust..Government.Corruption.",
                                               "Dystopia.Residual"]]
        y = chosen_happiness_data.loc[:,["Happiness.Score"]]

        break
    elif (chosen_Dataset == "4"): # if choosing 2018
        chosen_Dataset = "WorldHappinessReport_2018.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,["Country or region",
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        y = chosen_happiness_data.loc[:,["Score"]]

        break
    elif (chosen_Dataset == "5"): # if choosing 2019
        chosen_Dataset = "WorldHappinessReport_2019.csv"

        print("Loading.. " + chosen_Dataset)
        chosen_happiness_data = pandas.read_csv(chosen_Dataset)
        X = chosen_happiness_data.loc[:,["Country or region",
                                               "GDP per capita",
                                               "Social support",
                                               "Healthy life expectancy",
                                               "Freedom to make life choices",
                                               "Generosity",
                                               "Perceptions of corruption"]]
        y = chosen_happiness_data.loc[:,["Score"]]

        break
    else:
        print("Invalid input, please try again (1-5) \n") # if invalid input restart loop, ask for input again


# Split data using train_split_test (70% training, 30% testing)
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

print(X_train)


