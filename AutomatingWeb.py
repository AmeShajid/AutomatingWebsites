#this is how you automate web browsing
#first we will pip3 install selenium


#after installing now import selenium
#also just import all of these
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#right here we need to get a chrome webdriver and then this is how we hop on the webdriver
service = Service(exercutable_path="chromedriver 2")
driver = webdriver.Chrome(service=service)

#driver.get will get us any website we want
driver.get("https://www.google.com")

#we need to wait for the presence of the element located by the Class
#the number is the time we wait until we want to find the class
webdriverwait = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

#this is getting the google xpath and we want to click into it
#we are doing class name because using xpath is a bit more diffferent we are going to be using class name alot more so get used to it
input_element = driver.find_element(By.CLASS_NAME, "gLFyf") #gLFyf is the class name for the google search bar

#we will frist clear anything in the search bar
input_element.clear()

#now we will send actual keys / words into the search bar
#the keys.return is basically us pressing the enter page on the search bar using mac
input_element.send_keys("Rick Roll" + Keys.RETURN)

#so we want to wait and make sure the element is present on the page so we will do the wait thing again
webdriverwait = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Rick Astley - Never Gonna Give You Up"))#i put specfic text in the link
)

#right here we want to find an element based on its text
#The second half is basically where we are looking for the somethign that has something similar to rick roll
#if we want to find the exact text we can use By.LINK_TEXT
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Rick Astley - Never Gonna Give You Up")#both inside need to match


#then we will click on the link
link.click()


#we will let it run for 10 seconds and then quit the driver
time.sleep(10)

#quit the driver
driver.quit()



