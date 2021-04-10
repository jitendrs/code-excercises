"""Define a function max_of_three() that takes three
numbers as arguments and returns the largest of them."""

def max_of_three(num1: int, num2:int, num3: int) -> int:
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_of_three(3,4,2))