user_text = input()

count = 0
for x in user_text:
    if not(x in ('.', ',', ' ')):
        count += 1
print(count)



