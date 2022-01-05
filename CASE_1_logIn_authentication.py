from selenium import webdriver
import time
import pandas as pd


option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='Driver/chromedriver.exe', options=option)
skype_web_path = 'https://web.skype.com/'
driver.get(skype_web_path)
skyuser = ''
password = ''
lock = 5
















time.sleep(5)
data = int(input("unlock !: "))
if data == lock:
   #input_field = driver.find_element_by_id('i0116')
   email_field = driver.find_element_by_xpath("//input[@placeholder='Email, phone, or Skype']").send_keys(skyuser)
   time.sleep(4)
   user_button = driver.find_element_by_xpath("//input[@class='win-button button_primary button ext-button primary ext-primary']")
   time.sleep(3)
   user_button.click()
   time.sleep(4)
   password_field = driver.find_element_by_xpath("//input[@id='i0118']")
   password_field.send_keys(password)


   password_button = driver.find_element_by_xpath("//input[@class='win-button button_primary button ext-button primary ext-primary']")
   password_button.click()


