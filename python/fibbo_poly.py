
# Python code for fibbonacci series with polynomial algorithm



def feb(n):
    
    ar = list(range(0,n))
    ar[0] = 0
    ar[1] = 1
    if n <= 1:
        ar[n] = n
    for e in range(2,n):
        ar[e] = ar[e-1] + ar[e-2]
    return ar[n]



print(feb(10))  
