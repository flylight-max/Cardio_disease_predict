# **Cardio_disease_predict**  

Information taken from Kaggle
(https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)  

Here is a dataset of 70000 rows and 14 cols. Our target variable is "cardio", which is a binary variable whether the patien has (1) or not (0) a cardiovascular disease.  
There are 2 columns of indexes that will be of course removed.  
Features:

    Age | Objective Feature | age | int (days)
    Height | Objective Feature | height | int (cm) |
    Weight | Objective Feature | weight | float (kg) |
    Gender | Objective Feature | gender | categorical code | 1:f, 2:m
    Systolic blood pressure | Examination Feature | ap_hi | int |
    Diastolic blood pressure | Examination Feature | ap_lo | int |
    Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
    Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
    Smoking | Subjective Feature | smoke | binary | 1:smoker, 0:non-smoker
    Alcohol intake | Subjective Feature | alco | binary |
    Physical activity | Subjective Feature | active | binary |
    Presence or absence of cardiovascular disease | Target Variable | cardio | binary |  

    After preprocessing and feature engineering I will look for the best model classifier. I will look at KNN, logistic regression and Decision tree using scikit-learn package.  

Note that for the ordered categorical variables (already switched to numerical), some do not correspond to the numbers presented here.  