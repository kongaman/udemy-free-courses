from bs4 import BeautifulSoup
from simpleG import simple_get
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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

        driver = webdriver.Firefox()
        #binary = FirefoxBinary('/usr/bin/firefox')
        #driver = webdriver.Firefox(firefox_binary=binary)
        driver.implicitly_wait(30)

        daRealLinks = set()
        for entry in links:
            driver.get(entry)
            python_button = driver.find_element_by_class_name('discBtn')
            python_button.click()
            sSHtml = driver.page_source
            realBtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/a')
            realBtn.click()
            udemy = driver.page_source




