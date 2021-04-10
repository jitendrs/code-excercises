isbn = str(input())
if len(isbn) == 10 and sum([ index * int(x) for index,x in enumerate(isbn)]) % 11 != 0:
    print('Legal ISBN')
else:
    print('Illegal ISBN')