from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_driver.get('https://translate.google.co.il/?hl=en&tab=wT')

cookie1 = my_driver.get_cookies()
print (cookie1)

my_driver.delete_all_cookies()
print ("xxx")
cookie1 = my_driver.get_cookies()
print (cookie1)