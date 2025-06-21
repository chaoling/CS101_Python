'''
Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

Ex: If the input is:

hey hi Mark hi mark
the output is:

hey 1
hi 2
Mark 1
hi 2
mark 1
'''
user_input = input("enter list of words: ").split()
'''
for i in range(len(user_input)):
    print(f"{user_input[i]} {user_input.count(user_input[i])}")
'''
counter = {}
for i in range(len(user_input)):
    count = counter.get(user_input[i],0)
    counter[user_input[i]] = count + 1

for k,v in counter.items():
    print(k,v)
