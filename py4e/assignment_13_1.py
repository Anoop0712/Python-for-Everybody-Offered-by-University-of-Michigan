# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# E:\py4e\assignment_13_1.py

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Convert the values in that class into text and append it to the numlist
comments_class = soup.select('span[class="comments"]') 
numlist = list()
for comment in comments_class:
	numlist.append(comment.get_text())

#Parse through each individual value in numlist and add it to the totalsum and count
s=0
count=0
if len(numlist) > 0:
	for num in numlist:
		s = s + int(num)
		count = count + 1
#Print out the final values
print("Count :",count)
print("Total Sum :", s)
    