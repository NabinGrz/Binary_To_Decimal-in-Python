def decimalToBinary(decimal_number):
    
    reverse = []
    binary = []

    # to display number as a byte ie 8 digits
    for i in range(8):
        r = decimal_number % 2
        reverse.append(r)
        decimal_number = int(decimal_number / 2)
    print("Binary Equivalent: ", end=" ")
    for each in reverse[::-1]:  # slicing
        binary.append(each)
        print((each), end=" ")

    return (binary)
    print()


def binaryToDecimal(binary_number):
    num = 0
    init = 0
    sum = 0
    print()
    for i in binary_number[::-1]:
        num = 2 ** (init) * i
        sum = sum + num
        init = init + 1
    print("Decimal Addition of two Decimal Numbers: ", sum)
    return sum

# dec_no = int(input("Enter a number: "))
# dec_to_bin(dec_no)

# bin_no = int(input("Enter binary number: "))
# bin_to_dec(dec_to_bin(dec_no))
