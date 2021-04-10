


"""
base_s = 'AAA'[::-1]
for index , c in enumerate(base_s):
    print(index,c)
"""



counter = 0
base_s = 'AAA'
counter = len(base_s)
for c in base_s[::-1]:
    s_value = ord(c)
    for r in range(s_value+1,ord('Z')+1):
        print(base_s[counter] + chr(r))
    counter -= 1
    #print(s_value)
#print(ord('Z'))
