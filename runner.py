from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from simpleG import simple_get

for i in range(1, 2):
    response = simple_get("https://www.discudemy.com/language/english/"+str(i))
    print("Durchgang" + str(i) + " : " + str(response))
    if response is not None:
        print("Response is ok")
        html = BeautifulSoup(response, 'html.parser')
        print("bs gestartet")
        links = set()
        for a in html.select('a'):
            #print("a tag gefunden")
            for href in a:
                print(href)
                if len(href) > 10:
                    links.add(href.strip())
        #for entry in links:
         #   print(entry)


