from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_driver.get('https://translate.google.co.il/?hl=en&tab=wT')
my_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")