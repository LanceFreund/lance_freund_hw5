#This is homework 5
#This is my 1st python assignment

#!/usr/bin/env python3

# The def or function below
    #1)Takes the input PIN from the user
    #2)Ensures that the PIN is not greater than 4 digits
    #3)Ensures that the PIN is not less than 4 digits
    #4)Informs the user if the PIN is not the intended "1234" target
def GetInput():
    PIN = input()
    if len(PIN) < 4:
        print("Invalid PIN length. The correct format is: 9999")
    elif len(PIN) > 4:
        print("Invalid PIN length. The correct format is: 9999")
    elif PIN != "1234":
        print("Your PIN is incorrect")
    return PIN

# This is the count variable used to count 3 wrong choices of PIN
count = 1

# While loop that continues to prompt user for 3 chances
    #1)Prompts user to enter PIN
    #2)Calls the GetInput function
    #3)Breaks out of while loop if PIN is "1234"
    #4)Ensures that all digits in the string are valid numbers
    #5)Breaks out of while loop if count is greater than 3

    #In this loop count is incremented for each incorrect choice
while True:
    count = count + 1
    print("Please enter your PIN:")
    PIN = GetInput()
    if PIN == "1234":
        print("Your PIN is correct")
        break
   
    if not PIN.isdigit():
        print("Invalid PIN character. Correct format is: 9999")

    if count > 3:
        print("Your bank card is blocked")
        exit(1)

exit(0)
