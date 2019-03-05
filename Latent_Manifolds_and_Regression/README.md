# CMPE257
# Team JEMS

# Emmeline Tsen
# Jonathan Gee
# Matt DiPietro
# Sindhuja Ramini


# 1. Data Story: 

As a new business, we only have a certain amount of grapes to produce new wine. Using this data set, we would like to know what types of wines were rated best (and with a good price) in specific areas. From the new information we gather, we want to predict the cost of the new wine that would be on the market based on the price of similar types of wine.

As a consumer new to drinking wine, we want to know what types of wine were rated best for a given province and year. That way, when we are looking at bottles of wines in stores, we would know whether a specific bottle had high ratings.


# 2. Initial strong data set:

The original dataset was received was a dataset with wine reviews, ratings, price for wines throughout the world. The original dataset was taken from Kaggle (https://www.kaggle.com/zynicide/wine-reviews#winemag-data-130k-v2.csv) and had 130,000 rows.



# 3.1. Linear Regression on Original Dataset:
We performed linear regression between several different combinations on the original dataset. Through our linear regression analysis, we found that there was a decent correlation between vintage and price to the ratings of the wine.


# 3.2. Linear Regression on Enriched Dataset using California Wildfire Data:



# 4. Data preparation of original dataset: 
During the data cleaning process, we transformed the categorical data from province into a numerical value. We also used the name of the wines to retrieve the vintage of the wine. After, we removed all the rows that had null values for the vintage, province, points, and price columns. Once all the null values were removed, we normalized all of our data so it would not skew the clustering of the data.


# 5. Data enrichment to base dataset: 

We used the US Wildfires dataset found on Kaggle (https://www.kaggle.com/rtatman/188-million-us-wildfires) to enrich the base dataset. 


# 6. Latent manifold: 



# 7. Use the manifold to add features to your data set and run regression or clustering based on those new features. How does this improve the interpretability of your model? How does it add value to your business case?

 
