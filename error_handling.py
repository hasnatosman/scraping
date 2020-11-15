from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.pythonscraping21s.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("Server could not be found")
else:
    print("It is working")