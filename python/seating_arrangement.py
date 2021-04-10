
for _ in range(int(input())):
    n = int(input())
    if n % 12 > 6 or n % 12 == 0:
        if n % 6 == 1:
            print(n-1, "WS")
        elif n % 6 == 2:
            print(n-3, "MS")  
        elif n % 6 == 3:
             print(n-5, "AS")   
        elif n % 6 == 4:
             print(n-7, "AS")   
        elif n % 6 == 5:
             print(n-9, "MS")   
        elif n % 6 == 0:
             print(n-11, "WS")   
                
    else:
        if n % 6 == 0:
            print(n+1, "WS")
        elif n % 6 == 5:
             print(n+3, "MS")   
        elif n % 6 == 4:
             print(n+5, "AS")   
        elif n % 6 == 3:
             print(n+7, "AS")   
        elif n % 6 == 2:
             print(n+9, "MS")       
        elif n % 6 == 1:
             print(n+11, "WS")   