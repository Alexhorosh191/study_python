import urllib.request, urllib.error
import ssl
import json


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
print('Retrieving -', url)
html = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(html), 'characters')

info = json.loads(html)
len_of_comments = len(info['comments'])
sum_of_numbers = 0
print('Count:', len_of_comments)

for item in range(len_of_comments):
    sum_of_numbers += (int(info["comments"][item]["count"]))

print(sum_of_numbers)





