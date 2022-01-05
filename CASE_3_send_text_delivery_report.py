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
# search_bar = driver.find_element_by_xpath('//button[@title="People, groups & messages"]')
# search_bar.click()
content = 'hellow this is boat'
for i in range(len(new_data)):
   search_bar = driver.find_element_by_xpath('//button[@title="People, groups & messages"]')
   search_bar.click()
   time.sleep(2)
   active_search_bar =driver.find_element_by_xpath('//input[@placeholder="Search Skype"]')
   time.sleep(2)
   active_search_bar.send_keys(id_list[i])
   time.sleep(3)


      #(//div[@role='group' and @aria-label ='People']//div[@role='none'])[3]
   time.sleep(3)
   user_click = driver.find_element_by_xpath('(//div[@role="group" and @aria-label ="People"]//div[@role="none"])[3]')
   user_click.click()
   time.sleep(3)
   send_text_div = driver.find_element_by_xpath('//span[@data-offset-key="0-0-0"]')
   send_text_div.send_keys(content)


   time.sleep(3)
   send_buttton =driver.find_element_by_xpath('//button[@title="Send message"]')
   send_buttton.click()
   time.sleep(2)
   new_data.at[i, 'Delivary report'] = 'sent'

   time.sleep(2)


new_data.to_excel('XLSX_output_data/Delivary_report_skypee.xlsx')

   #time.sleep(1)

