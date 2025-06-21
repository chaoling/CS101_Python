'''

Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
'''
word = input()
password = ''

''' Type your code here. '''
tr = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
for c in word:
  if c in tr:
    password += tr[c]
  else:
    password += c

password += 'q*s'
print(password)
