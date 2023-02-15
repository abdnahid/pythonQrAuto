import csv
import time
import math
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://paytm.com/')
driver.maximize_window()

time.sleep(0.5)

driver.find_elements(By.CLASS_NAME,"_3y5vS")[2].click()

time.sleep(2)