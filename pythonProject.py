import pandas as pd
import numpy as np

# Taking input from the user
gsheet_id = input("Enter the Google Sheet ID : ")
sheet_name = input("Enter the Sheet Name : ")


# Url of the Sheets
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id,sheet_name)

# gsheet_url = "https://docs.google.com/spreadsheets/d/16x0beH301HZ1WrPZef7qPMYudf7ZPnp54bUar0EPOeU/gviz/tq?tqx=out:csv&sheet=Sheet1"
# gsheet_url = "https://docs.google.com/spreadsheets/d/16x0beH301HZ1WrPZef7qPMYudf7ZPnp54bUar0EPOeU/export?format=xlsx&sheet=Sheet1"

# Creating the File for storing the JSON data
file_ext = ".json"
file_name = sheet_name+file_ext
print("File saved in ",file_name)

# Creating a dataframe, Reading and Converting the data into CSV
df = pd.read_csv(gsheet_url)

# List formatting of the multiple data in the single column

df["DependsOnSystem"] = df["DependsOnSystem"].str.split(",")
df["MotherSystem"] = df["MotherSystem"].str.split(",")
df["MotherSystem"] = df["MotherSystem"].apply(lambda d:d if isinstance(d,list) else [])



# Converting the data frame of CSV type in JSON and storing in the file
df.to_json(file_name, indent=1,orient='records')

print("Work Completed")