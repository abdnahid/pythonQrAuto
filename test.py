from bn_words import BnWords
# from bn_number import En2Bn

# new_number = En2Bn("4").translate()

# print(new_number)
# from taka import Money
# val = "215"

# new_money = Money(val)
# bn_letter_list = new_money.in_bn_letter()
# print(bn_letter_list)
# val = '১'
# val_split = val.split(',')
# value = ['১','২','৪']

# value_int = [int(i) for i in value]
# summed = sum(value_int)

# print(val_split)

newNumber = BnWords("55321178")
newNumber.in_words()
print(newNumber.words)