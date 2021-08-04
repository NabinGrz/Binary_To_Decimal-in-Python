import Conversion as c
import Addition as add
import Validation as v

repeat = False
valid_input_a = False
valid_input_b = False

while (repeat == False):
    while(valid_input_a == False):
        try:
            a = int(input("Enter the first number: "))
            v.validation(a)
            c.decimalToBinary(a) #is a list for proper binary placement in 8
            valid_input_a = True
        except:
            print("Invalid Input. Please enter an integer value")
        
    print()
    
    while(valid_input_b == False):
        try:
            b = int(input("Enter the second number: "))
            v.validation(b)
            c.decimalToBinary(b) #is a list
            valid_input_b = True
        except:
            print("Invalid Input. Please enter an integer value")
            

    add.binaryAddition(a, b)

    print()
    print()

    # validity of input is reset if the user wants to try again
    valid_input_a = False
    valid_input_b = False
    yes_no = input("Do you want to continue? Type Yes/No. ")
    user_reply = yes_no.lower()
    if(user_reply == "yes" or user_reply == "y" or user_reply == "YES"):
        repeat = False
    elif(user_reply == "no" or user_reply == "n" or user_reply == "NO"):
        repeat = True
        break
