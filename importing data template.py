import pandas

happiness_2015_data = pandas.read_csv("WorldHappinessReport_2015.csv") # 12 columns
    # Country
    # Region
    # Happiness Rank
    # Happiness Score
    # Standard Error
    # Economy (GDP per Capita
    # Family,Health (Life Expectancy
    # Freedom
    # Trust (Government Corruption
    # Generosity
    # Dystopia Residual
happiness_2016_data = pandas.read_csv("WorldHappinessReport_2016.csv") # 13 columns 
    # Country
    # Region
    # Happiness Rank
    # Happiness Score
    # Lower Confidence Interval
    # Upper Confidence Interval
    # Economy (GDP per Capita)
    # Family,Health (Life Expectancy)
    # Freedom
    # Trust (Government Corruption)
    # Generosity
    # Dystopia Residual
happiness_2017_data = pandas.read_csv("WorldHappinessReport_2017.csv") # 12 columns 
    # "Country"
    # "Happiness.Rank"
    # "Happiness.Score"
    # "Whisker.high"
    # "Whisker.low"
    # "Economy..GDP.per.Capita."
    # "Family"
    # "Health..Life.Expectancy."
    # "Freedom"
    # "Generosity"
    # "Trust..Government.Corruption."
    # "Dystopia.Residual"
happiness_2018_data = pandas.read_csv("WorldHappinessReport_2018.csv") # 9 columns 
    # Overall rank
    # Country or region
    # Score
    # GDP per capita
    # Social support
    # Healthy life expectancy
    # Freedom to make life choices
    # Generosity
    # Perceptions of corruption
happiness_2019_data = pandas.read_csv("WorldHappinessReport_2019.csv") # 9 columns 
    # Overall rank
    # Country or region
    # Score
    # GDP per capita
    # Social support
    # Healthy life expectancy
    # Freedom to make life choices
    # Generosity
    # Perceptions of corruption


# feature_matrix = happiness_data.loc[:,[ STRING OF FEATURES TO BE USED ]]
# target_happiness = happiness_data.loc[:,["Happiness Score"]]
# features_train, features_test, happiness_train, happiness_test = train_test_split(feature_matrix, target_happiness,test_size=0.2) # 20,80, test train split