#This is homework 5
#This is my 1st python assignment

#!/usr/bin/env python3

def GetInput():
    PIN = input()
    return PIN

count = 1

while True:
    count = count + 1
    print("Please enter your PIN:")
    PIN = GetInput()
    if PIN == "1234":
        print("Your PIN is correct")
        break
    elif len(PIN) < 4:
        print("Invalid PIN length. The correct format is: 9999")
    elif len(PIN) > 4:
        print("Invalid PIN length. The correct format is: 9999")
    else:
        print("Your PIN is incorrect")
   
    if not PIN.isdigit():
        print("Invalid PIN character. Correct format is: 9999")

    if count > 3:
        print("Your bank card is blocked")
        break
        exit(1)

exit(0)
