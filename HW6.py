from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_driver.get('https://translate.google.com')

# by XPATH
# my_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")

#by CSS SELECTOR
# my_driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').send_keys("שלום2")

#by CLASS
my_driver.find_element(By.CLASS_NAME, 'er8xn').send_keys("חלום")

