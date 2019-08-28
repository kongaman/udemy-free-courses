from loopingBs4 import bs4loop
from loopingSelenium import selenloop
from simpleG import simple_get
from writeToF import writeToFile
links = set()
#Configurable Params
filemode = "w"      # "w" = overwrite, "a" = append
lang = "english"    # "german" "spanish" "arabic" "russian" "turkish" "Italian" "french" "japanese" "portuguese"
pagecount = 1       # number of discudemy pages to scan
clicklinks = True   # wether or not to click the udemy links - True False
#Scraping
for i in range(1, pagecount + 1):
    response = simple_get("https://www.discudemy.com/language/" + lang + "/" + str(i))
    pagelinks = bs4loop(response)
    for link in pagelinks:
        links.add(link)
daRealLinks = selenloop(links, clicklinks)
#Write to output-file
writeToFile(daRealLinks, filemode)
