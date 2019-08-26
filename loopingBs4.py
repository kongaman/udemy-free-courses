from bs4 import BeautifulSoup

def bs4loop(response):
    links = set()
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for link in html.find_all('a'):
            target = link.get('href')
            if target.startswith('https://www.discudemy.com/English/'):
                links.add(target)
    return links