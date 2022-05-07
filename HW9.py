from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_driver.get('https://www.github.com/')

my_driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]').send_keys('selenium' + '\n')