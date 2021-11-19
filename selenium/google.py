from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.ca/imghp?hl=en&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("vanier swimming")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

#Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    #Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    #Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".rg_i.Q4LuWd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".bRMDJf.islir")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(3)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass
driver.close()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
