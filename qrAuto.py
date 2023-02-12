import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('bsti url')

time.sleep(1)

driver.find_element(By.ID,'user_email').send_keys('email')
driver.find_element(By.ID,'btnNext').click()

time.sleep(1)

driver.find_element(By.ID,'user_password').send_keys('password')
time.sleep(1)
driver.find_element(By.ID,'btnSignIn').click()

time.sleep(1)



with open('data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        driver.get('verification url')

print("done")