#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1806859.json (Sum ends with 10)
#You do not need to save these files to your folder since your program will read the data directly from the URL. 

from urllib.request import urlopen
import json


json_url = input("Enter url: ")
print("Retrieving ", json_url)
data = urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)

#output
#Enter url: http://py4e-data.dr-chuck.net/comments_1806859.json
#Retrieving  http://py4e-data.dr-chuck.net/comments_1806859.json
#Retrieved 2735 characters
#Count: 50
#Sum: 2410