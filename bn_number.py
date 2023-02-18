class En2Bn():
    def __init__(self, number) -> None:
        self.number = number
        self.bn_number_dict = {"0":"","1":"১","2":"২","3":"৩","4":"৪","5":"৫","6":"৬","7":"৭","8":"৮","9":"৯"}
    def translate(self):
        return self.bn_number_dict[self.number]