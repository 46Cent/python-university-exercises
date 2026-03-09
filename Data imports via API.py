# a) Import necessary packages. Extract all the cocktails that contain gin as an ingredient and store it as
# gin_cocktails.

import requests
import pandas as pd
import time

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin")  # Send Request

data = response.json()  #  Save the request results as a .json

gin_cocktails = pd.DataFrame(data['drinks'])

gin_cocktails.head()


# b) Extract the IDs of all gin-based cocktails and store them in a separate vector or list called gin_ids.

gin_ids = gin_cocktails['idDrink']


# c) Use the list of drink IDs to fetch detailed information for each gin-based cocktail from the API. Store
# all results in a new data frame called cocktails_full. To avoid overloading the API server, make sure
# to include a short delay between requests (e.g., use Sys.sleep() in R or time.sleep() in Python).
# Implement this using a for loop

cocktails_full = []

for i in gin_ids:
  resp = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={i}")
  dat = resp.json()
  cocktails_full.append(dat['drinks'][0])
  time.sleep(0.2)



cocktails_full = pd.DataFrame(cocktails_full)