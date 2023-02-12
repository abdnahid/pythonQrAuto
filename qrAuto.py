import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://bstiqrcode.gov.bd/')

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
        driver.get('https://bstiqrcode.gov.bd/process/metrology-verification/add/8EgOciakJoL6iTfKlzpCH5bxfT9AUR7_fckdrqwpxC0')

print("done")