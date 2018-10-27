#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[112]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[113]:


#Let's check the data first and find out what our headers are
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[114]:


# Since each data point in our csv is a player, we can just run a 'len' function to find the total number of players.
TotalPlayers = len(purchase_data)
print("Your Total Players are: "+ str(TotalPlayers))


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

# In[115]:


# We're checking the head to see the file we're using
purchase_data.head()
#Need to find the length of unique items list.
#Find the average price. That should just be a mean.


# In[116]:


#Let's find a list of unique items
#Then we're going to find the length of the unique items. This should give us a number of uniques.
UniqueItems = purchase_data["Item Name"].unique()
UniqueItemsNum = len(UniqueItems)
print("There are "+str(UniqueItemsNum)+" unique items.")


# In[117]:


#Now we just find the mean of the price column, to find the average price.
avgprice = purchase_data["Price"].mean()
print("The average price is "+str(avgprice))


# In[118]:


# Now we need to find the total number of purchases
# To do this, we're going to find the length of the price colum in the purchase data.
TotalPurchases = len(purchase_data["Price"])
print("The total number of purchases are: "+str(TotalPurchases))


# In[119]:


#Next is Total Revenue
# To do that, we're going to find the sum of the price column.
# This should give us the total revenue
TotalRevenue=purchase_data["Price"].sum()
print("The total revenue is: "+str(TotalRevenue))


# In[120]:


#Cool, so let's put it all in a summary table to make it look pretty. We like pretty.
Summary = pd.DataFrame({'Number of Unique Items': [UniqueItemsNum], 'Average Price': [avgprice], 'Total Number of Purchases':[TotalPurchases], 'Total Revenue':[TotalRevenue]})
Summary


# In[ ]:





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

# In[121]:


# We're gonna start with the count of male players and female players. This way we can get the total count of both genders at once.
# To do this, we're going to do a value_counts on the Gender column
TotalGender = purchase_data["Gender"].value_counts()
TotalGender


# In[122]:


# To find the exact reason count of players, we'll have to eliminate duplicates, so let's make a variable for it cause we may need it later.
# avg. purchase total per person = the average price of purchase based on person, because people pop up multiple times in the data.
# so we just want to know what the average purchase value is per person
NoDupes_df = purchase_data.drop_duplicates(subset=["SN"],keep='first')
TrueGender = NoDupes_df["Gender"].value_counts()
TrueGender


# In[ ]:





# In[123]:


# Now we're going to show the percentage of Male and Female players
# We'll do this by getting the value counts of the gender column, multiplying by 100, then dividing by the total number of people in the gender column 
GenderPercent = purchase_data["Gender"].value_counts() * 100 / purchase_data["Gender"].count()
round(GenderPercent,2)


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

# In[124]:


# THESE SHOULD ALL BE GROUPBYS
# I mean, from the sounds of it, we're grouping by gender and that should give us the rest of the table

#?pd.DataFrame.groupby
#purchase_data.groupby("Gender").sum()


# In[125]:


# Let's save the groupby into a variable first
Gender_group = purchase_data.groupby("Gender")
# Then run the sum to see the data
Gender_group.count()


# In[126]:


# Let's find the number of purchases first through the GroupBy
# To do this, we're going to do a count of the Purchase ID column to see how many players are in each gender
Gender_Purchases = Gender_group["Purchase ID"].count()
# We also have to put this to a dataframe for the summary table
Gender_Purchases_df = Gender_Purchases.to_frame()
# Then we'll reset the index for later merging
Gender_Purchases_df.reset_index()


# In[127]:


# Now we find the average purchase price per gender
# We do this by finding the mean of the Price column in the gender groupby
GenderAvgPurchase = Gender_group["Price"].mean()
RoundedAvgGenderPurchase=round(GenderAvgPurchase,2)
RoundedAvgGenderPurchase
# Let's put it to a Dataframe
GenderAvgPurchase_df = RoundedAvgGenderPurchase.to_frame()
# Now we reset the index for later merging
GenderAvgPurchase_df = GenderAvgPurchase_df.reset_index()
GenderAvgPurchase_df


# In[128]:


# And now we find Total Purchase Value.
# To find that, we're gonna take the sum of the price column in the gender groupby
TotalGenderPurchase = Gender_group["Price"].sum()
RTotalGenderPurchase = round(TotalGenderPurchase,2)
# Let's take the total gender purchases, and then put it into a dataframe
TotalGenderPurchase_df = RTotalGenderPurchase.to_frame()
# We also have to reset the index for later merging
TotalGenderPurchase_df = TotalGenderPurchase_df.reset_index()
TotalGenderPurchase_df


# In[183]:


# Finally, we get to average total purchase per person
# To find this, we take total count of female and male players, then divide total purchase values by the total count
AvgPersonPurchase = TotalGenderPurchase/TrueGender
RoundedAvgPurchase=round(AvgPersonPurchase,2)
# We're going to put everything we found into a dataframe so we can store it into a summary table
AvgPurchase_df = RoundedAvgPurchase.to_frame("Average Purchase Price Per Person")
# Then we're going to reset the index so we can merge them later
AvgPurchase_df = AvgPurchase_df.reset_index()
# We have to rename the index column to Gender
ReAvgPurchase_df=AvgPurchase_df.rename(columns={"index":"Gender"})
ReAvgPurchase_df


# In[186]:


# Let's make a Data Summary!
# We're going to merge all of the Dataframes we made together into one big summary table

GenderSummary = pd.merge(ReAvgPurchase_df,TotalGenderPurchase_df, on="Gender")
GenderSummary = pd.merge(GenderSummary, GenderAvgPurchase_df, on="Gender")
GenderSummary = pd.merge(GenderSummary,Gender_Purchases_df, on="Gender")
FinalGenderSummary = GenderSummary.rename(columns={"Price_x":"Total Purchase Price", "Price_y":"Average Purchase Price"})
FinalGenderSummary
# GenderAvgPurchase_df,Gender_Purchases_df,
#Failed idea:
#SummaryGender = pd.DataFrame({'Number of Purchases': [Gender_Purchases], 'Average Purchase Price': [RoundedAvgGenderPurchase]})
#SummaryGender


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

# In[131]:


# First we're going to establish bins for each age
# We're going to do this by storing the bins to a variable
# Then creating the bin's names
bins = [0, 9, 14, 19, 24, 29, 34, 39, 201] 
AgeGroups = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
AgeGroups


# In[132]:


#sorted(AgeGroups)


# In[133]:


# Now we put the data in the bins
NoDupes_df["Age Group"] = pd.cut(NoDupes_df["Age"], bins, labels=AgeGroups)
NoDupes_df


# In[134]:


# Okay let's do a value_counts to get all of the Age Group's Purchase number
AgeGroupTotals = NoDupes_df["Age Group"].value_counts()
#.tolist()
AgeGroupTotals


# In[135]:


#Now we turn them into a table
AgeGroupTotals_df = AgeGroupTotals.to_frame('Age Group Totals')
AgeGroupTotals_df=AgeGroupTotals_df.reset_index()
AgeGroupTotals_df = AgeGroupTotals_df.rename(columns={"index":"Age Group"})
AgeGroupTotals_df


# In[136]:


#...and a list. We may need these for our summary table.
ListAgeTotals=NoDupes_df["Age Group"].value_counts().tolist()
ListAgeTotals


# In[137]:


# Then we'll find the number of people int he entire age group
AgeGroupAll = NoDupes_df["Age Group"].count()
AgeGroupAll


# In[138]:


# Then we find the percentage for each age group's purchases
AgeGroupPercent = AgeGroupTotals/AgeGroupAll*100
RoundedPercent = round(AgeGroupPercent,2)
RoundedPercent


# In[139]:


# and turn it into a list for the summary
AgeGroupPercentList = RoundedPercent.tolist()
AgeGroupPercentList


# In[140]:


#... and a table.
PercentTable = RoundedPercent.to_frame('Percent')
PercentTable=PercentTable.reset_index()
PercentTable=PercentTable.rename(columns={"index":"Age Group"})
PercentTable


# In[141]:


#Alright to make the summary table, let's turn all of the values into a list
MergedSummary = pd.merge(AgeGroupTotals_df, PercentTable,on="Age Group")
MergedSummary

# Failed Ideas:
# from the list we can then turn it into a data array like on the merging instrtuctor demo
# we do this through to.list
# THEN we turn it into a table!
#Age_Data = {
#    "Age Groups": sorted(AgeGroups),
#    "Age Group Totals": ListAgeTotals,
#    "Age Group Percentage": AgeGroupPercentList
#}
#AgeTable = pd.DataFrame(Age_Data, columns=["Age Groups","Age Group Totals", "Age Group Percentage"])
#AgeTable


# In[142]:


#SummaryAge =pd.DataFrame(AgeGroupTotals, columns=["Age Group Total"])
#SummaryAge


# ## Purchasing Analysis (Age)

# In[143]:


purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels=AgeGroups)
purchase_data


# In[144]:


# Let's make the group by and see our data
AgeGroupBy = purchase_data.groupby("Age Group")
AgeGroupBy.sum()


# In[145]:


# First we find the purchase count by counting the number of purchase IDs there are in the full data set
AgeGroupCount = AgeGroupBy["Purchase ID"].count()


# In[146]:


# Let's turn this into a dataframe for later summary
AgeGroupCount = AgeGroupCount.to_frame()
AgeGroupCount = AgeGroupCount.reset_index()
AgeGroupCount


# In[147]:


# Next we find the average purchase price by getting the average of the price column
AvgAgePP = AgeGroupBy["Price"].mean()
RoundedAvgAgePP = round(AvgAgePP,2)
RoundedAvgAgePP
#.to_frame()


# In[148]:


# Then we turn it into a table for the summary
RoundedAvgAgePP = RoundedAvgAgePP.to_frame().reset_index()
RoundedAvgAgePP


# In[156]:


# Then we find the total purchase value by running a sum on age each for the price
AgeTotalPurchaseValue = AgeGroupBy["Price"].sum()
AgeTotalPurchaseValue


# In[157]:


# ANd we store it into a table for the summary at the end
AgeTotalPurchaseValue_df = AgeTotalPurchaseValue.to_frame().reset_index()
AgeTotalPurchaseValue_df


# In[174]:


# Finally, we find the avergage total purchase per person by dividing the total purchase value by the number of people
TrueAge = NoDupes_df["Age Group"].value_counts()
AgeAvgPPP = AgeTotalPurchaseValue/TrueAge
RoundAgeAvgPPP = round(AgeAvgPPP,2)
RoundAgeAvgPPP


# In[175]:


# Then we store this last variable into a table
RoundAgeAvgPPP = RoundAgeAvgPPP.to_frame("Average Total Purchase per person").reset_index()
AgeAvgPPP_df = RoundAgeAvgPPP.rename(columns={"index":"Age Group"})
AgeAvgPPP_df


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

# In[181]:


# Summary!
AgeGroupSummary = pd.merge(AgeGroupCount, RoundedAvgAgePP, on="Age Group")
AgeGroupSummary = pd.merge(AgeGroupSummary, AgeTotalPurchaseValue_df, on="Age Group")
AgeGroupSummary = pd.merge(AgeGroupSummary, AgeAvgPPP_df, on="Age Group")
FinalAgeGroupSummary = AgeGroupSummary.rename(columns={"Price_x":"Average Purchase Price", "Price_y":"Total Purchase Price"})
FinalAgeGroupSummary
#AgeTotalPurchaseValue_df, AgeAvgPPP_df,


# In[ ]:





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

# In[236]:


# We need to find who our top players are, so let's create a groupby sorted by screen name
playergroup = purchase_data.groupby("SN")
#Screen_Price = purchase_data.sort_values(by=['SN', 'Price'],ascending=False)
#Screen_Price.head()
playergroup.sort_values()


# In[348]:


# Next we'll find a sum of all the prices each player has spent
TotalSpent = playergroup["Price"].sum()
# Then we put it into a dataframe to make sorting easier
TotalSpent_df = TotalSpent.to_frame("Price")
# Now we can sort it and find the top 5 spenders
Totalspent_df = TotalSpent_df.sort_values("Price",ascending=False)
# Then we're going to show the top 5 spenders and reset the index for later merging
Top5SpendersTotal = Totalspent_df.head(5).reset_index()
# We're also going to create a variable that saves their screen names to a list
# This way you can run this script and always get the top 5 spenders
Top5Spenders = Top5SpendersTotal["SN"].tolist()
Top5SpendersTotal
#Top5Spenders


# In[345]:


# Let's find the Average purchase price of these players next:
# First we're going to find where they are in the data with the loc function
Top5=purchase_data.loc[purchase_data['SN'].isin(Top5Spenders)]
# THen we're going to take that data and group it by their screen names
Top5Group=Top5.groupby("SN")
# After that, we calculate the mean of their purchases
Top5AvgPrice=Top5Group["Price"].mean()
# Make it look a bit prettier
Top5AvgPrice=round(Top5AvgPrice,2)
# Then put it to a table and reset the index for merging later
Top5AvgPrice_df = Top5AvgPrice.to_frame("Average Price").reset_index()
Top5AvgPrice_df
#AvgPlayerSpent = playergroup["Price"].mean()
#AvgPlayerSpent_df = AvgPlayerSpent.to_frame("Average Price")
#AvgPlayerSpent_df = AvgPlayerSpent_df.sort_values("Average Price",ascending=False)
#AvgPlayerSpent_df.head(5)


# In[342]:


# Now let's find their number of purchases each of these people did
# We can find this with a value_counts on the loc-ed data through their SN
Top5TotalPurchase = Top5["SN"].value_counts()
# Then we make it pretty and throw it into a dataframe for the summary
Top5TotalPurchase = Top5TotalPurchase.to_frame().reset_index()
Top5TotalPurchase = Top5TotalPurchase.rename(columns={"SN":"Total Number of Purchases", "index":"SN"})
Top5TotalPurchase


# In[351]:


# Now for the Summary Table!
Top5Summary = pd.merge(Top5TotalPurchase, Top5AvgPrice_df, on="SN")
Top5Summary = pd.merge(Top5Summary, Top5SpendersTotal, on="SN")
Top5Summary = Top5Summary.rename(columns={"Price":"Total Price"})
Top5Summary
#AgeGroupSummary = pd.merge(AgeGroupSummary, AgeTotalPurchaseValue_df, on="Age Group")
#AgeGroupSummary = pd.merge(AgeGroupSummary, AgeAvgPPP_df, on="Age Group")


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

# In[367]:


# Let's first get a dataframe of just Item ID, Item Name, and Price
Items=purchase_data[["Item ID", "Item Name", "Price"]]
# After that we groupby Item ID and Item Name
ItemGroup=Items.groupby(['Item ID','Item Name'])
ItemGroup.head()


# In[398]:


# Now let's find the purchase count
ItemCount = ItemGroup["Item Name"].count()
ItemCount_df = ItemCount.to_frame("Purchased")
ItemCount_df = ItemCount_df.sort_values("Purchased",ascending=False)
ItemCount_df


# In[399]:


# Next is the item price
# We can find this just by sorting by the value
ItemPrice = purchase_data[["Item Name", "Price"]]
ItemPrice = ItemPrice.sort_values("Price",ascending=False)
OnlyItemPrice = ItemPrice.drop_duplicates(subset=["Item Name"],keep='first')
OnlyItemPrice


# In[406]:


#And now we find the total Purchase Value
TotalPurchaseValue = ItemGroup.sum()
#Mistakes:
#.groupby("Item Name")
#TotalPurchaseValue = TotalPurchaseValue.sum()
TotalPurchaseValue = TotalPurchaseValue.sort_values("Price",ascending=False)
TotalPurchaseValue


# In[407]:


#Summary!
ItemsSummary = pd.merge(ItemCount_df,OnlyItemPrice, on="Item Name")
ItemsSummary = pd.merge(ItemsSummary,TotalPurchaseValue, on="Item Name")
ItemsSummary = ItemsSummary.rename(columns={"Price_x":"Price", "Price_y":"Total Purchase Value"})
#Upon Review, I noticed that there were several item duplicates that kept popping up.
# I don't know why they are appearing, but I think we can safely drop the second duplicates.
ItemsSummary = ItemsSummary.drop_duplicates(subset=["Item Name"],keep='first')
ItemsSummary


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

# In[408]:


#Let's sort the above table to find the most profitable items
SortedItemsSummary=ItemsSummary.sort_values("Total Purchase Value",ascending=False)
SortedItemsSummary


# In[ ]:




