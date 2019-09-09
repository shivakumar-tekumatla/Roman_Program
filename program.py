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

if __name__=="__main__":
    int_roman_map={1:(1000,"M"),
                   2:(900,"CM"),
                   3:(500,"D"),
                   4:(400,"CD"),
                   5:(100,"C"),
                   6:(90,"XC"),
                   7:(50,"L"),
                   8:(40,"XL"),
                   9:(10,"X"),
                   10:(9,"IX"),
                   11:(5,"V"),
                   12:(4,"IV"),
                   13:(1,"I")                       
                    }