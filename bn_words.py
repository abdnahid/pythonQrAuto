import math
from words_book import num_bd_dict,num_bd_letter_dict,division_words


class BnWords:
    def __init__(self,value) -> None:
        self.number = value
        self.words = ''
    
    def in_bn_letter(self):
        number_list = str(self.number)
        number_bn_list = [num_bd_letter_dict[i] for i in number_list]
        number_bn_letter = ''.join(number_bn_list)
        return number_bn_letter
    def three_digit_enbn(self,three_digits):
        in_words = ''
        in_words += f'{num_bd_dict[three_digits[:-2]]}শত '
        in_words += num_bd_dict[three_digits[-2:]]
        return in_words 
    def in_words(self):
        if len(self.number)>3:
            last_three = self.number[-3:]
            rest = self.number[:-3]
            print(rest)
            self.words += self.three_digit_enbn(last_three)
            i=0
            x=-2
            while i<(math.ceil(len(rest)/2)):
                if i==0:
                    print(rest[x:])
                    self.words= f'{num_bd_dict[rest[x:]]} {division_words[i]} '+self.words
                else:
                    self.words = f'{num_bd_dict[rest[x:x+2]]} {division_words[i]} '+self.words
                i+=1
                x-=2
        else:
            self.words = self.three_digit_enbn(self.number)