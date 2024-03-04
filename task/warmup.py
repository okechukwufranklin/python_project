number_of_word = 0
number_of_number = 0
word = input("enter input")
for index in word:
    if index.isalpha():
        number_of_word += 1
    if index.isdigit():
        number_of_number += 1

print("letter", number_of_word, "digit", number_of_number)
