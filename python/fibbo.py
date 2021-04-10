
# Python code for fibbonacci series with recursion



def feb(n):

    if n <= 1:
        return n
    else:
        return (feb(n-1) + feb(n-2))


for i in range(10):
    print(feb(i))  
