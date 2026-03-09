# Load the pandas package.
import pandas as pd

# Task 1

# a) Create a dictionary called population that stores the population in millions. Convert it into a pandas
# Series.
population = {
    "Germany": 83,
    "France": 68,
    "Italy": 59,
    "Spain": 47,
}

population = pd.Series(population)

# b) Create a pandas Series called gdp in billion USD.
gdp = pd.Series({
    "Germany": 4300,
    "France": 3000,
    "Italy": 2100,
    "Spain": 1800
})

# c) Combine the two Series into a DataFrame called countries with the columns Population (millions)
# and GDP (billion UDS).
countries = pd.DataFrame({
    "Population (millions)": population,
    "GDP (billion USD)": gdp
})

print(countries)

# d) Add a new column called GDP per capita (USD) by dividing the GDP by the population and multiplying
# by 1000.
countries["GDP per capita (USD)"] = (countries['GDP (billion USD)'] / countries["Population (millions)"]) *1000

print(countries)

# e) Print the highest GDP per capita.
print(countries['GDP per capita (USD)'].max())

# Task 2

# a) Create a DataFrame named customers with customer information.
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "city": ["Berlin", "Paris", "Berlin", "Rome"]
})

# b) Create a DataFrame named orders with order information. Tip: Use pd.NA for NaN.
orders = pd.DataFrame({
    "order_id": range(101, 107),
    "customer_id": [1, 2, 1, 3, 4, 2],
    "amount": [250, 120, 75, pd.NA, 300, pd.NA ]
})

print(orders)

# c) Merge the orders and customers DataFrames and call the resulting DataFrame merged. Before merging,
# think about which key to merge on.
merged = pd.merge(orders, customers, on = "customer_id")

print(merged)
# d) Check for missing values in merged and replace them with 0.


print(merged.isna().sum())

merged["amount"] = merged["amount"].fillna(0)



# e) Group the merged DataFrame by name and calculate the total amount spent and the number of orders.
# Call the new DataFrame summary.
summary = merged.groupby("name").agg(
    total_spent = ("amount", "sum"),
    Number_of_Orders = ("customer_id", "count")
)

print(summary)

# f) Group the merged DataFrame by city and calculate the average order amount. Call the new DataFrame
# cityamount.
cityamount = merged.groupby("city").agg(
    avg_order_amount = ("amount", "mean")
)

print(cityamount)

# Alternative:
cityamount = merged.groupby("city")["amount"].mean()

# Task 3

# a) Load the titanic dataset from seaborn and save it as titanic.
import seaborn as sns
titanic = sns.load_dataset("titanic")

# b) Print the average age.
print(titanic["age"].mean())

# c) Count how many missing values there are in the age column.
print(titanic["age"].isna().sum())

# d) Fill the missing values in the age column with the mean age. Create a new column called age_mean.
titanic["age_mean"] = titanic["age"].fillna(titanic["age"].mean())

# e) Fill the missing values in the age column using forward fill. Create a new column called age_ffill.
titanic["age_ffill"] = titanic["age"].ffill()

# f) Fill the missing values in the age column using backward fill. Create a new column called age_bfill.
titanic["age_bfill"] = titanic["age"].bfill()

# g) Now we want to compare the filling methods. Calculate and print the average age for each of the filled
#versions.
print(titanic["age_mean"].mean())

print(titanic["age_ffill"].mean())

print(titanic["age_bfill"].mean())

titanic.head()

# h) Group by sex and pclass and calculate average age and fare.
titanic.groupby(["sex", "pclass"]).agg(
    avg_age = ("age", "mean"),
    avg_fare = ("fare", "mean"))