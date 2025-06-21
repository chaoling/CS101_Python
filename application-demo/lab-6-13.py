'''
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39 
'''
user_input = map(int,input("here: ").split())
output =[x for x in user_input if x >= 0]
output.sort()
print(output)