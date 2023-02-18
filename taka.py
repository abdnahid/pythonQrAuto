import math
from num_to_bd import num_bd_dict,division_words


class Money:
    def __init__(self,value) -> None:
        self.number = value
        self.words = ''
    def three_digit_enbn(self,three_digits):
        in_words = ''
        in_words += f'{num_bd_dict[three_digits[:-2]]}শত '
        in_words += num_bd_dict[three_digits[-2:]]
        return in_words
    def in_words(self):
        if len(self.number)>3:
            last_three = self.number[-3:]
            rest = self.number[:-3]
            self.words += self.three_digit_enbn(last_three)
            i=0
            x=-2
            while i<(math.ceil(len(rest)/2)):
                if i==0:
                    self.words= f'{num_bd_dict[rest[x:]]} {division_words[i]} '+self.words
                else:
                    self.words = f'{num_bd_dict[rest[x:x+2]]} {division_words[i]} '+self.words
                i+=1
                x-=2
        else:
            self.words = self.three_digit_enbn(self.number)