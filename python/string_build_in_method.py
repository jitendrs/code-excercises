"""
Python string build-in methods example 
"""


s = "Hello World, from pendamic Hell..!"


print("*" * 60)
print(" S T R I N G   count()   M E T H O D ")
print("*" * 60)
print ("Check cout of string <{0}> in string <{1}> and returns the number of occurrences of substring".format(s,"Hell"))
print(s.count("Hell"))


print("*" * 60)
print(" S T R I N G   find()  M E T H O D ")
print("*" * 60)
print ("Find substring string <{0}> in string <{1}> and returns the index of the first occurrences of substring or return -1".format(s,"pend"))
print(s.find("pend"))



print("*" * 60)
print(" S T R I N G   isalnum()   M E T H O D ")
print("*" * 60)
print ("Checks for all characters are alpha numeric returns True otherwise return False.")
an = "jit12334"
print(an.isalnum())

print("*" * 60)
print(" S T R I N G   isalnum()   M E T H O D ")
print("*" * 60)
print ("Checks for all characters are alphabetics returns True otherwise return False.")
an = "jit12334"
print(an.isalnum())


print("*" * 60)
print(" S T R I N G   ISDIGIT   M E T H O D ")
print("*" * 60)
print ("Checks for all characters are digits returns True otherwise return False.")
an = "jit12334"
print(an.isalnum())


print("*" * 60)
print(" S T R I N G   JOIN    M E T H O D ")
print("*" * 60)
print ("This method Joins two strings")
an = "This is first string,"
print('.'.join([an,'ab', 'cd', 'df']))


print("*" * 60)
print(" S T R I N G   LOWER   M E T H O D ")
print("*" * 60)
print ("Methods to change string case to Lower.")
print(s.lower())


print("*" * 60)
print(" S T R I N G  REPLACE  M E T H O D ")
print("*" * 60)
print("This will replace matchig string old string with new string..")
print(s.replace('Hello', 'Hola'))



print("*" * 60)
print(" S T R I N G  STRIP  M E T H O D ")
print("*" * 60)
print("This method removes whitespaces and extra characters.")
print(s.strip('!'))


print("*" * 60)
print("S T R I N G  SPLIT  M E T H O D ")
print("*" * 60)
print("Splits string seperated by whitespaces or an optional seprator. Return a list")
print(s.split(","))