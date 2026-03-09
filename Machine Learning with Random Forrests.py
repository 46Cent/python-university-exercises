# In this task. we are working with bike rental data. We want to predict the number of rented bikes based on a
# variety of variables.

# First, load all the necessary packages.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# a) Load the SeoulBikeData and view its shape and take a look at the first few rows.

bikes = pd.read_csv("SeoulBikeData.csv")

print(bikes.head())

np.shape(bikes)


# b) Identify the target variable and split the data into X and y. Then, use the train_test_split() function
# to divide the data into a 70/30 training and test set. Don’t forget to set a random seed (choose ‘1234’).

X = bikes.drop("Rented Bike Count", axis = 1)

y = bikes["Rented Bike Count"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = True, random_state = 1234)


# c) Now, train a Random Forest Regressor. Look at the documentation of the RandomForestRegressor()
# function to see which default parameters it uses.

rf = RandomForestRegressor(random_state = 1234)

rf = rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)


# d) Evaluate the model by computing the Mean Squared Error (MSE) and the Root Mean Squared Error
# (RMSE).

mse = mean_squared_error(y_test, y_pred)

print(mse)

rmse = np.sqrt(mse)

print(rmse)


# e) In RandomForestRegressor, there is a property called feature_importances_ which holds the Gini
# importance of each feature (the higher this value, the more important the feature). We can list and plot
# feature_importances_ to see which features influence predictions most.

import seaborn as sns
# Create a sorted Series of feature importance
importances_df = pd.DataFrame({
"Feature": X_train.columns,
"Importance": rf.feature_importances_
}).sort_values("Importance", ascending=False)
# Plot a horizontal barplot of importances_sorted
plt.figure(figsize=(6, 4))
sns.barplot(x="Importance", y="Feature", data=importances_df)
plt.title("Feature Importances")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.subplots_adjust(left=0.4, bottom=0.3)
plt.show()