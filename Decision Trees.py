### Python file for Decision Tree model
# Load in dataset
# preprocess
#   fill missing values
# 
# use model
###

# importing
import pandas

# happiness_2015_data = pandas.read_csv("WorldHappinessReport_2015.csv")
# happiness_2016_data = pandas.read_csv("WorldHappinessReport_2016.csv")
# happiness_2017_data = pandas.read_csv("WorldHappinessReport_2017.csv")
# happiness_2018_data = pandas.read_csv("WorldHappinessReport_2018.csv")
# happiness_2019_data = pandas.read_csv("WorldHappinessReport_2019.csv")


print("Choose dataset to use: ")
print("\t1) World Happiness Report 2015\n" \
"\t2) World Happiness Report 2016\n" \
"\t3) World Happiness Report 2017\n" \
"\t4) World Happiness Report 2018\n" \
"\t5) World Happiness Report 2019\n")



while True:
    chosen_Dataset = input()
    if (chosen_Dataset == "1"):
        chosen_Dataset = "WorldHappinessReport_2015.csv"
    elif (chosen_Dataset == "2"):
        chosen_Dataset = "WorldHappinessReport_2016.csv"
        break
    elif (chosen_Dataset == "3"):
        chosen_Dataset = "WorldHappinessReport_2017.csv"
        break
    elif (chosen_Dataset == "4"):
        chosen_Dataset = "WorldHappinessReport_2018.csv"
        break
    elif (chosen_Dataset == "5"):
        chosen_Dataset = "WorldHappinessReport_2019.csv"
        break
    else:
        print("Invalid input, please try again (1-5) \n")


print("Loading.. " + chosen_Dataset)
chosen_happiness_data = pandas.read_csv(chosen_Dataset)
