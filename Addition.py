import Conversion as c
import LogicGates as l


def binaryAddition(a, b):
    print()
    print()
    x = c.decimalToBinary(a)  # is a list for proper binary placement
    print()
    y = c.decimalToBinary(b)  # is a list

    carry = []
    before_reverse = []
    last = []

    # For the half adder - let's take out the last digits from the lists a_bin and b_bin
    # XOR gate for the last digit
    # Sum = A XOR B , Co = A AND B

    s = l.xorGate(x[-1], y[-1])

    carry_1 = l.andGate(x[-1], y[-1])
    carry_in = carry_1
    before_reverse.append(s)
    print()

    # For the full adder - remaining seven places has to be added with a carry over too
    # Sum = A XOR B XOR C
    # Co = Cin AND ( A XOR B) + A AND B
    Co = 0
    for i in range(-2, -9, -1):
        sum_all = l.xorGate(carry_in, l.xorGate(x[i], y[i]))
        before_reverse.append(sum_all)

        Co = l.orGate(l.andGate(x[i], y[i]), l.andGate(carry_in, l.xorGate(x[i], y[i])))

        carry_in = Co

    print("Binary Addition of two binary numbers: ", end=" ")

    for numbers in before_reverse[::-1]:  # slicing
        last.append(numbers)
        print((numbers), end=" ")
    c.binaryToDecimal(last)
    return (last)




