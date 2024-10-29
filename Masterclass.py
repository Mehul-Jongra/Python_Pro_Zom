# We are doing an Exploratory Analysis of an Zomato Data Provided by WSCube Tech
import pandas as pd  # data manipulation
import seaborn as sns  # visualization
import numpy as np  # maths + stats
import matplotlib.pyplot as plt  # visualization

# Load the datasets
orders = pd.read_csv("Orders.csv")
customers = pd.read_csv("Customers.csv")
restaurants = pd.read_csv("Restaurants.csv")

# Check the info of the orders DataFrame
orders.info()

# Convert 'Order_Date' to datetime
orders["Order_Date"] = pd.to_datetime(orders["Order_Date"], errors='coerce')

# Extract month from the Order_Date
orders["Month"] = orders["Order_Date"].dt.strftime("%B")

# Display the modified DataFrame
print(orders)

#Generating a Bar Graph to display the Count of the Orders with Respect to Month.
plt.figure(figsize= (6,3))
sns.countplot(x = "Month", data = orders, palette="pastel")
plt.xticks(rotation = 45)
plt.show()

#performing a merge operation between two DataFrames: orders and customers.
df = pd.merge(left = orders, right = customers, on = "Customer_ID", how = "inner" )
print(df)

#creates a count plot that visualizes the distribution of customers by location, with different colors representing different age groups
plt.figure(figsize = (12,5)) #width, height
sns.countplot(x = "Customer_Location", data = df, hue = "Customer_Age_Group", palette = "viridis", edgecolor = "black")
plt.legend(bbox_to_anchor = (1,1))
plt.show()
