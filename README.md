# Webscraping Excercise

Gets all the udemy links from as many pages as you want on discudemy.<br>
You can customise behaviour via parameters in runny.py
```
#Configurable Params
filemode = "w"      # "w" = overwrite, "a" = append
lang = "english"    # "german" "spanish" "arabic" "russian" "turkish" "Italian" "french" "japanese" "portuguese"
pagecount = 1       # number of discudemy pages to scrape
clicklinks = True   # wether or not to click the udemy links - True False
```

## Problems - Configuration / Installation
### Errors:
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.<br>
#### Linux:
Selenium requires geckodriver to interface with Firefox. Here's how to install geckodriver:

1. Download geckodriver from https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz (or if you need the 32 bit version, go to https://github.com/mozilla/geckodriver/releases to see more download options)
2. Extract the file into your Downloads folder
3. Open a console and run ```sudo mv ~/Downloads/geckodriver /usr/bin```

Forget about adding to PATH or specifying the location in ```webdriver.Firefox()```.  I tried, it doesn't work

## TODO:
- check line terminator under linux
- make scraped amount of discudemy-pages customizable via command line arg
- customizable language to scrape via command line arg
- autobuy for udemy
- regex to grab only specific courses
- make it work with chrome browser
- maybe gui


