from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get("http://google.com")
time.sleep(2)
# fetch the search input box using path
user_input = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea") #full XPath of the text area
user_input.send_keys("Campusx")
time.sleep(2)
user_input.send_keys(Keys.ENTER)
time.sleep(5)
link = driver.find_element(by = By.XPATH,value = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(2)
link2 = driver.find_element(by = By.XPATH,value = '//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()
time.sleep(20)

