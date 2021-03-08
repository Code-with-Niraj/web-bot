from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

a = webdriver.Chrome('/home/niraj/Downloads/chromedriver/chromedriver',chrome_options=options)
a.get('https://www.google.nl/')