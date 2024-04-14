import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


load_dotenv()

driver = webdriver.Chrome()
driver.get(os.getenv("LOGIN_URL"))
driver.maximize_window()


time.sleep(0.5)

driver.find_element(By.ID, "user_email").send_keys(os.getenv("LOGIN_EMAIL"))
driver.find_element(By.ID, "btnNext").click()

time.sleep(0.5)

driver.find_element(By.ID, "user_password").send_keys(os.getenv("ACCESS_KEY"))
time.sleep(0.5)
driver.find_element(By.ID, "btnSignIn").click()

time.sleep(2)
driver.get("https://bstiqrcode.gov.bd/metrology-verification/list/NfeGkqGglTmyL1ARYF7aaXl8IHld5TjTKKQXcDxECJI")
driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/a/div/div').click()
driver.find_element(By.CSS_SELECTOR,'#list_3').click()
driver.find_element(By.CSS_SELECTOR,'#accordion3 > div:nth-child(5)').click()

for i in range(25):
    driver.find_element(By.XPATH,f'//*[@id="table_desk"]/tbody/tr[{i+1}]/td[8]/a').click()
    time.sleep(2)
    


