import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Main_Page'

response = urllib.request.urlopen(url)
webContent = response.read()  # output is in byte datatype


#result = webContent.decode()  # convert byte to  str
soup = BeautifulSoup(webContent,'html.parser')
print(soup.get_text().strip())
