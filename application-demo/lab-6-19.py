'''
6.19 LAB: Replacement words
Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.

Ex: If the input is:

automobile car   manufacturer maker   children kids
The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
the output is:

The car maker recommends car seats for kids if the car doesn't already have one. 
'''

#grab the replacement word pairs from the input
tokens = input("enter your replacement words: ").split()

#build the dictionary
word_pairs = {}
for i in range(0,len(tokens),2):
    word_pairs[tokens[i]] = tokens[i+1]

print(word_pairs)
#Grab the sentence from the input
user_sentence = input("enter your original sentence: ")
#replace words
for a,b in word_pairs.items():
    user_sentence = user_sentence.replace(a,b)

print(user_sentence)


