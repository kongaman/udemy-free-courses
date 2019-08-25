# Webscraping Excercise

Gets all the udemy links from page 1 on discudemy and opens them in a new firefox browser tab.<br>
AND puts all udemy-links into a txt-file (folder "target") you can chose to overwrite or append

TODO:

- check on windows
- make scraped amount of discudemy-pages customizable via command line arg
- customizable language to scrape via parameter
- autobuy for udemy
- regex to grab only specific courses
- make it work with chrome browser


## Configuration
### Errors:
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.<br>
#### Linux:
Selenium requires geckodriver to interface with Firefox. Here's how to install geckodriver:

1. Download geckodriver from https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz (or if you need the 32 bit version, go to https://github.com/mozilla/geckodriver/releases to see more download options)
2. Extract the file into your Downloads folder
3. Open a console and run ```sudo mv ~/Downloads/geckodriver /usr/bin```

Forget about adding to PATH or specifying the location in ```webdriver.Firefox()```.  I tried, it doesn't work