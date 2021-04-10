

with open("f_r.txt", "r+") as file:
    file.write(file.read()[::-1])
