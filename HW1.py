from selenium import webdriver
from selenium.webdriver.common.by import By

my_cdriver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_cdriver.get('http://www.walla.co.il/')


my_ffdriver = webdriver.Firefox(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\geckodriver.exe')
my_ffdriver.get('http://www.ynet.co.il/')