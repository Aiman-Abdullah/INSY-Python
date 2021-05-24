# Objective:
# Scraping Data From CNN Website
# Using Beatufilsoup lib

The CNN Money’s Market Movers website (https://money.cnn.com/data/hotstocks/ ) tracks the most active stocks on a real time basis.  Specifically, the most active, the top gainers and top losers are listed at any instance in time. You will first write Python scripts that collect the list of most actives, gainers and losers from the above website. Next, your programs should take the ticker symbols and names of these companies (and categories) and build a csv file (called stocks.csv) with data about each stock from the website: 
https://finance.yahoo.com/quote/AMD? , which gives the quote for ticker symbol AMD as an example. 
Or, you can also use the stock info page from CNN website: 
https://money.cnn.com/quote/quote.html?symb=GE , which gives the quote for ticker symbol GE as an example. 
The data to be collected from the Yahoo Finance site should include: 
OPEN price 
PREV CLOSE price 
VOLUME 
MARKET CAP 


# Libraries:
from bs4 import BeautifulSoup as soup <br /> 
from urllib.request import urlopen as uReq <br />
import csv <br />
Use Dictionary <br />
Use List <br />
