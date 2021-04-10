a = 'gsadasfdashdasdkjgadhjdyjhasfdasgd'
b = 'ajdfaghfsdasgdfagsdhgasdfasfdahd'


#a = 'tttttttttttttttttttttttttttttttttttttsssssssssssssssss'
#b = 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'

a = 'abc'
b = 'dec'


'''
char_l = []
del_char = 0
for chr in a:
    a_d = a.count(chr)
    b_d = b.count(chr)
    if chr not in char_l:
        diff = 0
        if a_d > b_d:
            diff = a_d - b_d
        elif b_d > a_d:
            diff = b_d - a_d
        del_char += diff      
        char_l.append(chr)

for chr in b:
    if chr not in char_l:
        del_char += b.count(chr)      
        char_l.append(chr)
print(del_char)
'''


del_counter = 0
for c in set(a):
    if c not in b:
        del_counter += a.count(c)
    elif a.count(c) > b.count(c):
        del_counter += (a.count(c) - b.count(c))
    elif b.count(c) > a.count(c):
        del_counter += (b.count(c) - a.count(c))
for c in set(b):
    if c not in a:
        del_counter += b.count(c)    
print(del_counter)        
