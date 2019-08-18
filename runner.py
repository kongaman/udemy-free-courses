from bs4 import BeautifulSoup
from simpleG import simple_get

for i in range(1, 2):
    response = simple_get("https://www.discudemy.com/language/english/"+str(i))
    print("Durchgang" + str(i))
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        links = set()
        for link in html.find_all('a'):
            target = link.get('href')
            if target.startswith('https://www.discudemy.com/English/'):
                print(target)
                links.add(target)
        daRealLinks = set()
        for entry in links:
            singleSite = simple_get(entry)
            if singleSite is not None:
                sSHtml = BeautifulSoup(singleSite, 'html.parser')
                for realLink in sSHtml.find_all('a'):
                    realTarget = realLink.get('href')
                    if realTarget.startswith('https://www.discudemy.com/go/'):
                        print(target)
                        daRealLinks.add(realTarget)



