from time import sleep
import mechanize
from bs4 import BeautifulSoup

#target page address
myAddress = "http://finance.yahoo.com/q?s=yhoo"

#create Browser object
myBrowser = mechanize.Browser()

#obtain 1 stock quote per minute for the next 3 minutes
#if load the page after the loop
#the method myBrowser.reload() is also a good way to refresh
for i in range(0,3):
	htmlPage = myBrowser.open(myAddress)
	htmlText = htmlPage.get_data()

	mySoup = BeautifulSoup(htmlText)
	myTags = mySoup.find_all("span", id="yfs_l84_yhoo")

	myPrice = myTags[0].string
	print "The current price of YHOO is: {}".format(myPrice)

	if i<2:
		sleep(5)

