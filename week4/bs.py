#Scraping HTML Data with BeautifulSoup
#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1806856.html (Sum ends with 56)
#You do not need to save these files to your folder since your program will read the data directly from the URL.

import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = input('Enter - ')

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print(count)
print(sum)

#output
#Enter - http://py4e-data.dr-chuck.net/comments_1806856.html 
#50
#2556