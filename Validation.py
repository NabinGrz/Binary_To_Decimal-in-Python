import Conversion

def validation(x):
    validity = False
    while validity == False:
        if (x < 0 or x > 255):
            x = int(input("Invalid Input!!. Please enter the number between 0 and 255 again: "))            
        else:
            validity = True
