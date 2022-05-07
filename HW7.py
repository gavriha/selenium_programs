from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_driver.get('https://facebook.com')

my_driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("gavrih@gmail.com")
my_driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("BookBook22")

my_driver.find_element(By.NAME, 'login').click()

