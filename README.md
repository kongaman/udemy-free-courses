# Webscraping Excercise
Windows only atm :-(<br>
Gets all the udemy Links from Page 1 on Discudemy and opens them in a new Firefox browser tab.



TODO:
- get udemy links as a list
- make it work on linux
- make it work with chrome browser
- make scraped amount of discudemy-pages customizable via parameter
- customizable language via parameter
- working autobuy for udemy
- regex to grab only specific courses


## Configuration
### Errors:
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.<br>
#### Linux:
Selenium requires geckodriver to interface with Firefox. Here's how to install geckodriver:

1. Download geckodriver from https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz (or if you need the 32 bit version, go to https://github.com/mozilla/geckodriver/releases to see more download options)
2. Extract the file into your Downloads folder
3. Open a console and run ```sudo mv ~/Downloads/geckodriver /usr/bin```