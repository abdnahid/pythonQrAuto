# import time
# import math
# import pandas
# import os
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select


# driver = webdriver.Chrome()

# driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
# driver.maximize_window() 


# select_field = driver.find_element(By.NAME,"UserTitle")

# try:
#     Select(select_field).select_by_visible_text("IT Manager")
#     time.sleep(5)
#     print("hoise")
# except:
#     print("hoinai")

# data = pandas.read_csv("data.csv")

# for i,x in data.iterrows():
#     capacity = x.capacity.split(',')
#     quantity = x.quantity.split(',')
#     fee_string = x.fee.split(',')
#     fee=[eval(i) for i in fee_string]
#     time.sleep(1)
#     table_row_data=''
#     for j,y in enumerate(capacity):
#         table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%;">{j+1}</td><td style="width: 20%;"><p>{x.type}</p><p>ব্রান্ডঃ {"-" if x.brand=="none" else x.brand}</p></td><td style="width: 10%; text-align: center;">{y}</td><td style="width: 10%;">{quantity[j]}</td><td style="width: 15%;">{"-" if x.denomination=="none" else x.denomination}</td><td style="width: 10%;">{"-" if x.weight_class=="none" else x.weight_class}</td><td style="width: 20%;">{fee[j]}</td></tr>'
#     time.sleep(1)
#     table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%;"><strong>ক্রমিক নং</strong></td><td style="width: 20%;"><strong>ওজন/পরিমাপণ ও পরিমাপণ যন্ত্রের বিবরণ</strong></td><td style="width: 10%;"><strong>ওজন/ ধারণক্ষমতা</strong></td><td style="width: 10%;"><strong>সংখ্যা/পরিমাণ</strong></td><td style="width: 15%;"><strong>ওজন/পরিমাপণের ডিনোমিনেশন</strong></td><td style="width: 10%;"><strong>ওজন/পরিমাপণের শ্রেণি</strong></td><td style="width: 20%;"><strong>ভেরিফিকেশন ফি (টাকা)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">মোট</p></td><td style="width: 20%; text-align: center;">{sum(fee)}</td></tr><tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">১৫% ভ্যাট</p></td><td style="width: 18.0581%; text-align: center;">{math.ceil(sum(fee)*0.15)}</td></tr><tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">সর্বমোট</p></td><td style="width: 18.0581%; text-align: center; height: 54px;">{math.ceil(sum(fee)*1.15)}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;">zxc</p></td></tr></tbody></table>'

#     print(table_data)

# from bn_number import En2Bn

# new_number = En2Bn("4").translate()

# print(new_number)
# from taka import Money
# val = "215"

# new_money = Money(val)
# bn_letter_list = new_money.in_bn_letter()
# print(bn_letter_list)
val = '১'
val_split = val.split(',')
value = ['১','২','৪']

value_int = [int(i) for i in value]
summed = sum(value_int)

print(val_split)