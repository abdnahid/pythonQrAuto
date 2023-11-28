import time
import math
import pandas
import os
from taka import Money
from bn_number import En2Bn
from dotenv import load_dotenv


data = pandas.read_csv("swaptest.csv", encoding="utf8")

for i, x in data.iterrows():
    capacity = x.capacity.split(",")
    quantity = x.quantity.split(",")
    
    for j, y in enumerate(capacity):
        print(j,'j')
        print(y,'y')
    time.sleep(1)
    

print("done")
