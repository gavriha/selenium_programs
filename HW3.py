from selenium import webdriver
from selenium.webdriver.common.by import By

my_cdriver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe')
my_cdriver.get('http://www.walla.co.il/')

ttl1= my_cdriver.title
my_cdriver.refresh()
ttl2=my_cdriver.title

if ttl1==ttl2:
    print("same")
else:
    print ("differnt")

# print ("ttl1" + ttl1)
# print ("ttl2" + ttl2)