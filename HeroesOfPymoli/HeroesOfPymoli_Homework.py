#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[221]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[222]:


purchase_data


# In[223]:


Number_of_Purchases = purchase_data["SN"].nunique()


# In[224]:


total_players = pd.DataFrame([{"Total Players":Number_of_Purchases}])
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[225]:


unique_items = purchase_data["Item Name"].nunique()
unique_items


# In[226]:


purchase_data["Price"] = purchase_data["Price"].astype(float)


# In[227]:


average_price = purchase_data["Price"].mean()
average_price = '${:.2f}'.format(average_price)
average_price


# In[228]:


total_revenue = purchase_data["Price"].sum()
total_revenue = '${:.2f}'.format(total_revenue)
total_revenue


# In[229]:


summary_dataframe = pd.DataFrame([
    {"Number of Unique Items":unique_items,
     "Average Price":average_price,
     "Number of Purchase":Number_of_Purchases,
     "Total Revenue":total_revenue}])
summary_dataframe


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[230]:


grouped_gender = purchase_data.groupby("Gender")["SN"].nunique()
grouped_gender = pd.DataFrame(grouped_gender)


# In[231]:


grouped_gender["Percentage of Players"] = grouped_gender/ grouped_gender.sum()*100
grouped_gender["Percentage of Players"] = grouped_gender["Percentage of Players"].map(
    "{0:,.2f}%".format)


# In[232]:


grouped_gender = grouped_gender.rename(columns={"SN":"Total Count"})
grouped_gender


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[233]:


grouped_purchase =  purchase_data.groupby("Gender")
purchase_count = grouped_purchase["Purchase ID"].count()
purchase_summary = pd.DataFrame(purchase_count)


# In[234]:


purchase_summary["Average Purchase Price"] = grouped_purchase['Price'].mean()
purchase_summary["Total Purchase Value"]= grouped_purchase["Price"].sum()
purchase_summary["Avg Total Purchase per Person"] = grouped_purchase["Price"].sum()/ purchase_data.groupby("Gender")["SN"].nunique().astype(float)


# In[235]:


purchase_summary["Average Purchase Price"] = purchase_summary["Average Purchase Price"].map(
    "${0:,.2f}".format)
purchase_summary["Total Purchase Value"] = purchase_summary["Total Purchase Value"].map(
    "${0:,.2f}".format)
purchase_summary["Avg Total Purchase per Person"] = purchase_summary["Avg Total Purchase per Person"].map(
    "${0:,.2f}".format) 


# In[236]:


purchase_summary


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[237]:


print(purchase_data["Age"].min())
print(purchase_data["Age"].max())


# In[238]:


bins = [ 0, 10, 15, 20, 25, 30, 35, 40, 50]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29","30-34","35-39","40+"]


# In[239]:


purchase_data["Age Bin"] = pd.cut(purchase_data["Age"], 
                                  bins,  
                                  right = False,
                                  labels=group_names,
                                  include_lowest=True)


# In[240]:


age_group = purchase_data.groupby("Age Bin")["SN"].nunique()
age_summary = pd.DataFrame(age_group)


# In[241]:


age_summary["Percentage of Players"] = age_group/age_group.sum()*100
age_summary["Percentage of Players"] = age_summary["Percentage of Players"].map(
    "{0:,.2f}%".format)
age_summary = age_summary.rename(columns = {"SN":"Total Count"})
age_summary


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[242]:


purchase_age_group = purchase_data.groupby(["Age Bin"])
purchase_summary = purchase_age_group.count()["Purchase ID"]
purchase_summary = pd.DataFrame(purchase_summary)


# In[243]:


purchase_summary["Average Purchase Price"] = purchase_age_group["Price"].mean()
purchase_summary["Total Purchase Value"] = purchase_age_group["Price"].sum()
purchase_summary["Avg Total Purchase per Person"] = purchase_age_group["Price"].sum()/ purchase_data.groupby("Age Bin")["SN"].nunique().astype(float)


# In[244]:


purchase_summary["Average Purchase Price"] = purchase_summary["Average Purchase Price"].map(
    "${0:,.2f}".format)
purchase_summary["Total Purchase Value"] = purchase_summary["Total Purchase Value"].map("${0:,.2f}".format)
purchase_summary["Avg Total Purchase per Person"] = purchase_summary["Avg Total Purchase per Person"].map(
    "${0:,.2f}".format)
purchase_summary


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[245]:


spender_group = purchase_data.groupby(["SN"])
spender_summary = spender_group.count()["Purchase ID"]
spender_summary = pd.DataFrame(spender_summary)


# In[246]:


spender_summary["Average Purchase Price"] = spender_group["Price"].mean()
spender_summary["Total Purchase Value"] = spender_group["Price"].sum()


# In[247]:


spender_summary =spender_summary.rename(columns={"Purchase ID":"Purchase Count"})


# In[248]:


spender_summary = spender_summary.sort_values(by="Total Purchase Value", ascending=False)


# In[249]:


spender_summary["Average Purchase Price"] = spender_summary["Average Purchase Price"].map(
    "${0:,.2f}".format)
spender_summary["Total Purchase Value"] = spender_summary["Total Purchase Value"].map(
    "${0:,.2f}".format)


# In[250]:


spender_summary.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[251]:


item_data = purchase_data[['Item ID', 'Item Name', 'Price']]


# In[252]:


item_group = item_data.groupby(["Item ID","Item Name"])
item_count = item_group.count()
item_summary = pd.DataFrame(item_count)
item_summary["Total Purchase Value"] = item_group["Price"].sum()
item_summary = item_summary.rename(columns={"Price":"Purchase Count"})


# In[258]:


merge_summary = item_summary.merge(item_data,on=["Item ID","Item Name"], how='left')
merge_summary = merge_summary.drop_duplicates()


# In[254]:


final_item_summary =merge_summary.sort_values(by='Purchase Count', ascending=False)


# In[255]:


final_item_summary["Price"] = final_item_summary["Price"].map("${0:,.2f}".format)
final_item_summary["Total Purchase Value"] = final_item_summary["Total Purchase Value"].map("${0:,.2f}".format)
final_item_summary.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[256]:


most_profitable_items = merge_summary.sort_values(by='Total Purchase Value', ascending=False)


# In[257]:


most_profitable_items["Price"] = most_profitable_items["Price"].map("${0:,.2f}".format)
most_profitable_items["Total Purchase Value"] = most_profitable_items["Total Purchase Value"].map("${0:,.2f}".format)
most_profitable_items.head()


# ## Three observable trends

# ###### 1. There are more male players in this game. 
# ###### 2. Nearly half of the players are 20-24 years old, and most players are younger than 30 years old.
# ###### 3. Oathbreaker, Last Hope of the Breaking Storm is the most popular game.
