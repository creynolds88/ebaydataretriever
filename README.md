# ebaydataretriever
Retrieves Ebay data from auctions and writes it to csv

This fetches data from ebay using beautifulsoup to scrape the listing name, price, seller ID, item number, and url and adds it to a new line in the ebay.csv

It then converts the csv to a dataframe with pandas and outputs a list of other rows containing the same keyword in the "Keyword" or "Name" column


