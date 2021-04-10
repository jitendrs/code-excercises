"""Write a function that takes a character (i.e. a
string of length 1) and returns True if it is a vowel,
False otherwise."""

def check_vowel(s: str) -> bool:

    vowels = ['a','e','i','o','u']
    if s in vowels:
        return True
    return False


print(check_vowel('x'))