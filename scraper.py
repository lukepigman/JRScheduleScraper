
import login
import stripper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter
driver_path = '/Users/luke_/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('https://facebook.com')


email = driver.find_elements_by_id('email')
email[0].send_keys(login.emailText)
passw = driver.find_elements_by_id('pass')
passw[0].send_keys(login.passwordText)
passw[0].send_keys(Keys.ENTER)


driver.get('https://portal.joyrun.com/')
fb_button = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]")
fb_button.click()

driver.implicitly_wait(10)
prm_slot_mgmt = driver.find_element_by_xpath("/html/body/ul/li[2]/div/a")
prm_slot_mgmt.click()

cProgField = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/section/div[2]/div/input")
cProgField.send_keys("ilsu Spring 19 team")
team = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/section/div[2]/div/div/div").click()

calendar_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/section/div[3]/div[5]/div[5]")
calendar_button.click()

time_slots = driver.find_elements_by_class_name("rbc-event-content")

users = []

for slots in time_slots:
   users.append(stripper.chopString(slots.text))

print(Counter(users))
    

resultFile = open("users.txt", 'w')
resultFile.write(str(Counter(users)))
