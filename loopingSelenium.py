from selenium import webdriver

def selenloop(links, clicklinks):
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    daRealLinks = set()

    for entry in links:
        driver.get(entry)
        python_button = driver.find_element_by_class_name('discBtn')
        python_button.click()
        realBtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/a')
        ulink = realBtn.text
        if ulink.startswith('https://www.udemy.com/course/'):
            daRealLinks.add(ulink)
            if clicklinks:
                realBtn.click()
    return daRealLinks