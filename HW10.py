
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-extensions")

my_driver=webdriver.Chrome(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\chromedriver.exe',options=opt)
my_driver.get('https://www.github.com/')

fopt = webdriver.FirefoxOptions()
fopt.add_argument("--disable-extensions")

my_ffdriver = webdriver.Firefox(executable_path='C:\\Users\\gavri\\Documents\\DevOps Class\\geckodriver.exe', options=fopt)
my_ffdriver.get('http://www.ynet.co.il/')
