"""
Demo class 
"""

balance = 0

def deposite(amount):
    global balance
    balance += amount

def withd(amount):
    global balance
    if balance >= amount:
        balance -= amount
    else:
       print("Sorry, amount is greater than balance please try again..")

def balan():
    print("Your balance is ",balance)

while True:
    print("Please enter action from below list:")
    print("1. Balance Check")
    print("2. Deposite")
    print("3. Withdrawal")
    print("0. Exit")
    
    in_put = int(input())
    if in_put == 1:
        balan()
    elif in_put == 2:
        amount = int(input("Please enter amount: "))
        deposite(amount)
    elif in_put == 3:
        amount = int(input("Please enter amount: "))
        withd(amount)
    elif in_put == 0:
        print("Good Bye..!!")
        break
    else:
        print("Sorry please provide correct input..")
        