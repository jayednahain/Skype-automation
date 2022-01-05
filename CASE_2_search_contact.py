from selenium import webdriver
import time
import pandas as pd


option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='Driver/chromedriver.exe', options=option)
skype_web_path = 'https://web.skype.com/'
driver.get(skype_web_path)



"""data section"""
data_set = pd.read_excel(r'Xlsx_file/contact_list_skypee.xlsx', engine='openpyxl')
id_list = list(data_set['Unique_id'])


lock = 5
data = int(input("unlock !: "))
if data == lock:
   search_bar = driver.find_element_by_xpath('//button[@title="People, groups & messages"]')
   search_bar.click()
   for i in range(len(id_list)):
      time.sleep(2)
      active_search_bar =driver.find_element_by_xpath('//input[@placeholder="Search Skype"]')
      time.sleep(2)
      active_search_bar.send_keys(id_list[i])
      time.sleep(3)
      active_search_bar.clear()
      time.sleep(1)







