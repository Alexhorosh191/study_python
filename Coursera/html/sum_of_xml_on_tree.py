import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
print('Retrieving -', url)
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')

tree = ET.fromstring(html)
results = tree.findall('.//count')

sum_of_numbers = 0
for item in range(len(results)):
    sum_of_numbers += (int(results[item].text))

print('Count:', (len(results)))
print('Summa:', sum_of_numbers)

