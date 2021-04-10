"""
Demonstration of os.walk() function.
"""


import os

os.system("clear")
print("-"*80)
print("OS Walk Program")
print("-"*80)
print("")



print("Root prints out directories only from what you specified")
print("-"*70)

print("Dirs prints out sub-directories from root")
print("-"*70)

print("Files prints out all files from root and directories")
print("-"*70)

print("This program will do ann os.walk on the folder that you specify")
print("-"*70)

path = input("Enter directory name: ")

for root, dirs, files in os.walk(path):
    print(root)
    print("-----------------")
    print(dirs)
    print("-----------------")
    print(files)
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")