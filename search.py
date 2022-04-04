from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/home/Hp/VSC/python/scripts/chromedriver') 


driver.maximize_window()
driver.get("https://google.com")
form = driver.find_element_by_name("q")
with open('scraped.txt', mode='r') as file:
    text=file.readlines()
    # for i in range(len(text)):
        # form.send_keys(text[i])
        
for i in range(len(text)):
    tabno='tab'+str(i)
    driver.execute_script(f"window.open('about:blank','{tabno}');")
    driver.switch_to.window(tabno)
    link='https://www.google.com/search?q='+text[i]
    driver.get(link)