#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1806858.xml (Sum ends with 45)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import urllib
from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum=0
for item in results:
    x = int(item.find('count').text)
    sum = sum+x

print("Sum : ",sum)

#output
#Enter - http://py4e-data.dr-chuck.net/comments_1806858.xml
#Sum :  2545