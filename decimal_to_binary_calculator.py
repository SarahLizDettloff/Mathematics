def convert_to_binary(decimal):
    result = 0
    quotient = 0
    remainder = 0
    binary = []
    if decimal >= 16:
        try:
            while decimal > 0:
                quotient = (decimal) / 2
                remainder = round((float(decimal) / 2) - quotient)
                binary.append(int(remainder))
                decimal = quotient
            result = "".join(map(str,reversed(binary)))
            print(result)
            another()
        except:
            pass
    elif decimal <= 15:
        get_binary_value(decimal)
    elif decimal < 0:
        print("A negative number cannot be converted into a decimal.\n")
        get_decimal()
    elif decimal == 0:
        result = 0000
    print(result)

def get_binary_value(decimal):
    result = 0
    if decimal == 1:
        result = "0001"
    elif decimal == 2:
        result = "0010"
    elif decimal == 3:
        result = "0011"
    elif decimal == 4:
        result = "0100"
    elif decimal == 5:
        result = "0101"
    elif decimal == 6:
        result = "0110"
    elif decimal == 7:
        result = "0111"
    elif decimal == 8:
        result = "1000"
    elif decimal == 9:
        result = "1001"
    elif decimal == 10:
        result = "1010"
    elif decimal == 11:
        result = "1011"
    elif decimal == 12:
        result = "1100"
    elif decimal == 13:
        result = "1101"
    elif decimal == 14:
        result = "1110"
    elif decimal == 15:
        result = "1111"
    print(result)
    another()

    

def another():
    answer = raw_input("Would you like to convert another decimal to binary? (Y/N)\n")
    if answer == "Y":
        get_decimal()
    elif answer == "N":
        exit()
    else:
        print("Enter either Y or N.")
        another()


def get_decimal():
    decimal = 0
    decimal = raw_input("What decimal do you want to convert to binary?\n")
    try:
        decimal = int(decimal)
        convert_to_binary(int(decimal))
    except ValueError:
        print("Input must be a numeric value.")
        get_decimal()


if __name__=="__main__":
    get_decimal()
