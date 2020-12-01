import urllib.request, urllib.parse, urllib.error
import json
import ssl
#E:\py4e\assignment_15.py
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
s = 0

url = input('Enter location: ')
	
print('Retrieving ' + url)
data = urllib.request.urlopen(url, context=ctx).read().decode()

js = json.loads(data)

for i in js['comments']:

	count += 1
	s += int(i['count'])
print("count:",count)
print("sum:",s)	