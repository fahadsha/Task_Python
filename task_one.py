# -*- coding: utf-8 -*-
"""
Task one: The purpose this task is generate arithematic number sequence
User will be asked what is the sequential order according to relevant
pattern.
"""
def compare(user_input, answer):
    """check the right input inserted by user"""
    return user_input == answer

print("Start the quiz")
print("Use only one space while answering the sequence")
ANSWER = ['56 92 141', '10 30 28', '280 450 730']
while True:
    INPUT_FIRST = input("enter appropriate sequence for these numbers:2 6 15 31 "
                        "enter the input:")
    if compare(INPUT_FIRST, ANSWER[0]):
        print("your answer is correct")
        break
    else:
        print("The desired input is incorrect\n Hint: double of the previous difference")
        continue

while True:
    INPUT_SECOND = input("what is the correct sequence to check the complex numbers:2 6 4 12 "
                         "enter the input:")
    if compare(INPUT_SECOND, ANSWER[1]):
        print("you have guessed it right")
        break
    else:
        print("your could have done better! try again\n Hint:difference of two")
        continue

while True:
    INPUT_THIRD = input("what is the correct sequence for fibonacci numbers:50 60 110 170 "
                        "enter the input:")
    if compare(INPUT_THIRD, ANSWER[2]):
        print("you have guessed it right")
        break
    else:
        print("your could have done better! try again\n Hint: sum it up")
print("Congrats! you have exceed expectations")
