import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Set an input function for the url address and parse it through BeautifulSoup
url = input('Enter URL : ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Set up an input functions for the repeat
count = int(input('Enter count : '))

#Set up an input function for the position
position = int(input('Enter position : '))

#Initialize i to 0
i = 0

#Repeat the loop for the required amount of repeats
while i < count :
	
	# Retrieve the url for the required position and print it
	tags = soup('a')
	for tag in tags:
		tag = tags[position - 1].get('href', None)
	print("Retrieving : " + tag)
	
	#Update url and parse it through BeautifulSoup
	url = tag
	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	
	#Update i by 1 each step
	i += 1