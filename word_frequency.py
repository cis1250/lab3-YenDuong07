#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_input = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")

words = []
numbers = []
index = 0

words_list = user_sentence.split()

for x in words_list:

    normal_form = x.lower()
    normal_form = normal_form.replace(",", "")
    normal_form = normal_form.replace(".", "")
    normal_form = normal_form.replace("!", "")

    if normal_form in words:
        index = words.index(normal_form)
        numbers[index] += 1;
    else:
        words.append(normal_form)
        numbers.append(1)

for z in range (len(words)):
    print(words[z] + ": " + str(numbers[z]));
