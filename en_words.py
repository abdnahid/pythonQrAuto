import math
from words_book import num_en_list,tens,thousands


class EnWords:
    def __init__(self,value) -> None:
        self.number = value
        self.words = ''

    def three_digit_words(self,three_digits):
        in_words = ''
        first_digit = int(three_digits/100)
        last_two_digit = three_digits%100
        in_words = in_words + f'{num_en_list[first_digit]} hundred and ' + self.two_digit_words(last_two_digit)
        return in_words

    def two_digit_words(self,two_digit):
        in_words = ''
        if two_digit<19:
            in_words += num_en_list[two_digit]
        else:
            first_part = int(two_digit/10)
            last_part = two_digit%10
            in_words = in_words + tens[first_part]+ ' ' + num_en_list[last_part]
        return in_words

    def in_words(self):
        if self.number>999:
            last_three = self.number%1000
            print(last_three)
            rest = int(self.number/1000)
            print(rest)
            self.words += self.three_digit_words(last_three)
            i=0
            while  rest != 0:
                self.words = self.two_digit_words(rest%100) +' '+ thousands[i] + ' '+self.words
                rest = int(rest/100)
                i+=1
        else:
            self.words = self.three_digit_words(self.number)