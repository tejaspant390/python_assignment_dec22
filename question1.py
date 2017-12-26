#To Ask for a number (n) as an input from user. Using the use input (n), write a program to generate a dictionary that contains
# (i, i*i) where i  is key and i*i is a value for numbers between the range 1 and n (both included). and then the program should
#  print the dictionary.

num = input("Enter the number: ")
dict1 = dict()

for i in range(1, num+1):
    dict1[i] = i*i

print(dict1)