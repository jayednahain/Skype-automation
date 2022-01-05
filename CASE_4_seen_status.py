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
new_data = data_set.fillna("No value")
name_list = list(data_set['Name'])
id_list = list(data_set['Unique_id'])


time.sleep(5)
search_bar = driver.find_element_by_xpath('//button[@title="People, groups & messages"]')
search_bar.click()



time.sleep(5)
for i in range(len(new_data)):

   time.sleep(2)
   active_search_bar =driver.find_element_by_xpath('//input[@placeholder="Search Skype"]')
   time.sleep(2)
   active_search_bar.send_keys(id_list[i])
   time.sleep(3)



   time.sleep(3)
   user_click = driver.find_element_by_xpath('(//div[@role="group" and @aria-label ="People"]//div[@role="none"])[3]')
   user_click.click()
   time.sleep(3)


   try:
      driver.find_element_by_xpath(f'//div[@title="{name_list[i]}"]').is_displayed() ==True
      new_data.at[i, 'Status'] = 'seen'
   except:
      new_data.at[i, 'Status'] = 'unseen'

   time.sleep(3)
   active_search_bar.clear()


new_data.to_excel('XLSX_output_data/status_report_skypee.xlsx')