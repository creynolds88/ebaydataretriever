import os
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# This fetches data from ebay using beautifulsoup and adds it to a new line in the ebay.csv
# It then converts the csv to a dataframe with pandas and outputs a list of other rows containing the same keyword in the "Keyword" or "Name" column


print("What is the eBay item url? Press return key when done")
itemUrl =  input() #generates ebay item url

print ('Enter description tag. ie. "bicycle"')
descriptionTag = input()

page = requests.get(itemUrl) #requests html from url entered earlier
soup = BeautifulSoup(page.text, 'html.parser') #parses html file, writes to text
price = soup.find(itemprop="price").get_text() #sold price 
name = soup.find("title").get_text() #listing name / page title
itemNumber = soup.find(id="descItemNumber").get_text() #eBay item number
sellerId = soup.find("span", {"class": "mbg-nw"}).get_text() #sellers username
#bids = soup.find(id="qty-test").get_text() #how many bids (need to fix for BIN items)
#endDate = soup.find(id="bb_tlft").get_text() #item end date (too much info being pulled, needs fix)

list1 = [name, price, sellerId , itemNumber , itemUrl,descriptionTag] #creates string to be written to csv
with open("ebay.csv", "a", newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(list1)
print('Item has been saved to CSV')

df = pd.read_csv('ebay.csv') #converts csv to dataframe for easier searching with pandas
df1 = df[df['Name'].str.contains(descriptionTag, case=False) | df['Keyword'].str.contains(descriptionTag, case=False)] #searches the "Name" column and "keyword" column on the data frame and returns all matching rows


print('Here are some similar listings you have saved: ')
print(df1)

#need to fix bid count and end date-add to list1

