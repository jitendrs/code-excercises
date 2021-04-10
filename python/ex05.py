
def romanToInt(s: str) -> int:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(s):
        if (i + 1) == len(s) or roman_numerals[c] >= roman_numerals[s[i + 1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result


print(romanToInt("MDCXCV"))
                    
                            
