"""Define a function that computes the length of a
given list or string. (It is true that Python has
the len() function built in, but writing it yourself
is nevertheless a good exercise.)"""


def len1(lst):
    counter = 1
    for c in lst:
        counter += 1
    return counter

len()

print(len('jitendra'))
print(len([1,2,3]))