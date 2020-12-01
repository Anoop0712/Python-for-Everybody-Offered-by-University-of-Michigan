import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
s = 0

url = input('Enter location: ')
	
print('Retrieving ' + url)
data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)
lists=tree.findall('.//count')

for i in lists:
	count += 1
	s += int(i.text)
print("count:",count)
print("sum:",s)	