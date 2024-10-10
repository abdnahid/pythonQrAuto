# from bn_words import BnWords
# # from bn_number import En2Bn

# # new_number = En2Bn("4").translate()

# # print(new_number)
# # from taka import Money
# # val = "215"

# # new_money = Money(val)
# # bn_letter_list = new_money.in_bn_letter()
# # print(bn_letter_list)
# # val = '১'
# # val_split = val.split(',')
# # value = ['১','২','৪']

# # value_int = [int(i) for i in value]
# # summed = sum(value_int)

# # print(val_split)

# newNumber = BnWords("55321178")
# newNumber.in_words()
# print(newNumber.words
# import tkinter
# from tkinter import filedialog
# import os
# import pandas

# root = tkinter.Tk()

# currdir = os.getcwd()
# tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please select a directory',filetypes=[("Excel files", ".csv")])
# data = pandas.read_csv(tempdir)
# for i,x in data.iterrows():
#     print (x)
# from bn_words import BnWords

# instance = BnWords("523").in_bn_letter()
# print(instance)

# from bn_words import BnWords

# a = BnWords("3000")
# b= a.in_bn_letter()
# c=a.in_words()
# print(f'মোটঃ {b}\nকথায়ঃ {c}')
import pandas
from pandas import Series
from pprint import pprint

data = pandas.read_csv("ag.csv")

insertedData = []

def insert_company(x:Series)->dict:
    return {
            "name":x["name"],
            "address":x.address,
            "thana":x.thana if x.thana !="none" else '',
            "district":x.district,
            "scales":[
                {"capacity":x.capacity,"type":x.type,"quantity":x.quantity,"model":x.model,"brand":x.brand,"serial":x.serial},
            ],
            "receipt":str(x.receipt).split(".")[0]
        }

for i,x in data.iterrows():
    if len(insertedData)==0:
        insertedData.append(insert_company(x))
    else:
        matched_index=None
        for index,value in enumerate(insertedData):
            if value["name"]==x["name"] and value["address"]==x["address"]:
                matched_index=index
                insertedData[index]["scales"].append({"capacity":x.capacity,"type":x.type,"quantity":x.quantity,"model":x.model ,"brand":x.brand,"serial":str(x.serial).split(".")[0]})
        if matched_index ==None:
            insertedData.append(insert_company(x))


pprint(insertedData)