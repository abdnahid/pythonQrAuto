import time
import math
import pandas
from bn_words import BnWords
from bn_number import En2Bn
from pandas import Series
import json
import pprint



data = pandas.read_csv("daily.csv")

insertedData = []

for i,x in data.iterrows():
    if len(insertedData)==0:
        insertedData.append({
            "name":x["name"],
            "address":x.address,
            "thana":x.thana,
            "district":x.district,
            "scales":[
                {"capacity":x.capacity,"quantity":x.quantity,"model":x.model if x.model!="none" else "","brand":x.brand if x.brand!="none" else "","serial":x.serial if x.serial!="none" else ""},
            ],
            "receipt":x.receipt
        })
    else:
        matched_index=None
        for index,value in enumerate(insertedData):
            if value["name"]==x["name"] and value["address"]==x["address"]:
                matched_index=index
                insertedData[index]["scales"].append({"capacity":x.capacity,"quantity":x.quantity,"model":x.model if x.model!="none" else "","brand":x.brand if x.brand!="none" else "","serial":x.serial if x.serial!="none" else ""})
        if matched_index ==None:
            insertedData.append({
                "name":x["name"],
                "address":x["address"],
                "thana":x["thana"],
                "district":x["district"],
                "scales":[
                    {"capacity":x.capacity,"quantity":x.quantity,"model":x.model if x.model!="none" else "","brand":x.brand if x.brand!="none" else "","serial":x.serial if x.serial!="none" else ""},
                ],
                "receipt":x.receipt
            })

for company in insertedData:
    capacity = x.capacity.split(',')
    quantity = x.quantity.split(',')
    quantity_int = [int(item) for item in quantity]
    total_quantity = sum(quantity_int)
    fees = x.fee.split(',')
    fee_int = [int(item) for item in fees]
    subtotal = sum(fee_int)
    vat = math.ceil(sum(fee_int)*0.15)
    total = math.ceil(sum(fee_int)*1.15)
    word_instance = EnWords(total)
    total_in_words = word_instance.in_words()
    time.sleep(1)
    table_row_data=''
    for j,scale in enumerate(company["scales"]):
        table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;">{(j+1)}</td><td style="width: 20%; border: 0.5px solid #000000;"><p>{x.type}</p><p>Brand: {"-" if x.brand=="none" else x.brand}</p></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{y}</td><td style="width: 10%; border: 0.5px solid #000000;">{f'{int(scale.capacity*1000)}g' if scale.capacity<0 else f'{int(scale.capacity)}kg'}</td><td style="width: 15%; border: 0.5px solid #000000;">{"-" if x.denomination=="none" else x.denomination}</td><td style="width: 10%; border: 0.5px solid #000000;">{"-" if x.weight_class=="none" else x.weight_class}</td><td style="width: 20%; border: 0.5px solid #000000;">{fees[j]}</td></tr>'
    time.sleep(1)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;"><strong>Serial No</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Description</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Capacity</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Quantity</strong></td><td style="width: 15%; border: 0.5px solid #000000;"><strong>Weight Denomination</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Weight Class</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Verification Fee (Taka)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">Subtotal</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{subtotal}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">15% VAT</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{vat}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">Total</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{total}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;"><strong><u>In Words: </u></strong> {word_instance.words} Taka Only</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID,"memo_no").send_keys(f'{x.memo}/{x["name"]}')
    try:
        company_select_field = driver.find_element(By.XPATH,'//*[@id="company_id"]')
        Select(company_select_field).select_by_visible_text(x["name"])
        time.sleep(2)
        driver.find_element(By.ID,"verification_date").clear()
        driver.find_element(By.ID,"varification_address").clear()
        driver.find_element(By.ID,"equipment_verification").clear()
        driver.find_element(By.ID,"no_of_equipment").clear()
        driver.find_element(By.ID,"receipt_no").clear()
        driver.find_element(By.ID,"verification_date").clear()
    except:    
        driver.find_elements(By.NAME,"company_type")[0].click()
        time.sleep(1)
        driver.find_element(By.ID,"company_name").send_keys(x["name"])
    time.sleep(2)
    driver.find_element(By.ID,"varification_address").send_keys(x.address)
    time.sleep(1)
    driver.find_element(By.ID,"verification_date").send_keys("26-03-2023")
    select_district = driver.find_element(By.ID,"verification_district_id")
    Select(select_district).select_by_visible_text(x.district)
    time.sleep(2)
    select_thana = driver.find_element(By.ID,"verification_thana_id")
    Select(select_thana).select_by_visible_text("Select Thana")
    driver.find_element(By.ID,"equipment_verification").send_keys(total_quantity)
    driver.find_element(By.ID,"no_of_equipment").send_keys(total_quantity)
    time.sleep(1)
    driver.find_element(By.ID,"receipt_no").send_keys(x.receipt)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,"tox-mbtn__select-label")[5].click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"tox-collection__item--active").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"tox-textarea").clear()
    driver.find_element(By.CLASS_NAME,"tox-textarea").send_keys(table_data)
    driver.find_element(By.CSS_SELECTOR,"body > div.tox.tox-silver-sink.tox-tinymce-aux > div.tox-dialog-wrap > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)").click()
    driver.find_elements(By.NAME,"stamped_or_reject")[0].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#right_side_btn > button.btn.btn-info.cancel").click()

pprint.pprint(insertedData)
