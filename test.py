from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set up the WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://ibas.finance.gov.bd/Public/DistanceMatrix')

time.sleep(3)


# Initialize a 643x643 2D list with all values set to zero
rows, cols = 643, 643
distance_list = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(643):
    driver.find_element(By.XPATH,'//*[@id="DEPARTURE"]/li[1]/button').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, f'//*[@id="DEPARTURE"]/li[2]/ul/li[{str(i+3)}]').click()
    for j in range(643):
        driver.find_element(By.XPATH,'//*[@id="ARRIVAL"]/li[1]/button').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, f'//*[@id="ARRIVAL"]/li[2]/ul/li[{str(j+3)}]').click()
        driver.find_element(By.ID, 'btnGo').click()
        time.sleep(1)
        distance_val = driver.find_element(By.ID,'DistanceView').text
        distance_list[i][j] = int(distance_val)





# Open a new Python file and write the 2D list to it
with open('distance_list.py', 'w') as file:
    file.write('distance_list = [\n')
    for row in distance_list:
        file.write(f'    {row},\n')
    file.write(']\n')

print("2D list has been saved to 'distance_list.py'.")






# Optional: Close the browser
driver.quit()
