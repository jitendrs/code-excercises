
def romanToInt(s: str) -> int:
    symbol = { 'I': 1, 'V': 5, 'X':10 , 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    form = {'IV': 4, 'IX': 9, 'XL':40 ,'XC':90,'CD':400, 'CM': 900}
    int_sum = 0
    index = 0

    if len(s) == 1 and s in symbol:
        return symbol[s]

    while index < len(s):


        if s[index] in symbol:
            if index+1 < len(s):
                num_char = str(s[index] + s[index+1])
            if num_char in form:
                int_sum +=form[num_char]
                index +=1
            if num_char not in form:
                int_sum +=symbol[s[index]]
        index +=1
    return int_sum


print(romanToInt("MDCXCV"))
                    
                            
                        