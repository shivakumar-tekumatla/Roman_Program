class roman:

    def __init__(self,number):#,int_roman_map):
        self.number=number
        self.int_roman_map=int_roman_map
    def int_to_roman(self):
        result=""
        for i in self.int_roman_map:
            result+=(self.number//self.int_roman_map[i][0])*self.int_roman_map[i][1]
            self.number=self.number%self.int_roman_map[i][0]
        return result