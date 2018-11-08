# -*- coding: utf-8 -*-
"""
Spyder Editor
Task one: numbering sequence
"""
def compare(user_input, answer):
    """check the right input inserted by user"""
    return user_input == answer

print("Start the quiz")
ANSWER = ['56 92 141', '10 30 28', '280 450 730']
while True:
    INPUT_FIRST = input("what is the correct sequence for these numbers:2 6 15 31\n")
    if compare(INPUT_FIRST, ANSWER[0]):
        print("your answer is correct")
        break
    else:
        print("The desired input is incorrect\n Hint: double of the previous difference")
        continue

while True:
    INPUT_SECOND = input("what is the correct sequence to check the complex numbers:2 6 4 12\n")
    if compare(INPUT_SECOND, ANSWER[1]):
        print("you have guessed it right")
        break
    else:
        print("your could have done better! try again\n Hint:difference of two")
        continue

while True:
    INPUT_THIRD = input("what is the correct sequence for fibonacci numbers:50 60 110 170\n")
    if compare(INPUT_THIRD, ANSWER[2]):
        print("you have guessed it right")
        break
    else:
        print("your could have done better! try again\n Hint: sum it up")
print("Congrats! you have exceed expectations")
