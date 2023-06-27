#Assignment: Following Links in HTML Using BeautifulSoup
#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: K

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print(s[position-1])
    print(t[position-1])
    url = s[position-1]

#output
#Enter Url: http://py4e-data.dr-chuck.net/known_by_Lauri.html
#Enter count: 7
#Enter position:18
#http://py4e-data.dr-chuck.net/known_by_Amina.html
#Amina
#http://py4e-data.dr-chuck.net/known_by_Amie.html
#Amie
#http://py4e-data.dr-chuck.net/known_by_Riva.html
#Riva
#http://py4e-data.dr-chuck.net/known_by_Digby.html
#Digby
#http://py4e-data.dr-chuck.net/known_by_Triniti.html
#Triniti
#http://py4e-data.dr-chuck.net/known_by_Frederick.html
#Frederick
#http://py4e-data.dr-chuck.net/known_by_Keilan.html
#Keilan