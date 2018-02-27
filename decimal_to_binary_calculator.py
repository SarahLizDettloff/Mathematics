binary_values = {
    1 : "001",
    2 : "0010",
    3 : "0011",
    4 : "0100",
    5 : "0101",
    6 : "0110",
    7 : "0111",
    8 : "1000",
    9 : "1001",
    10 : "1010",
    11 : "1011",
    12 : "1100",
    13 : "1101",
    14 : "1110",
    15 : "1111"
    }

def convert_to_binary(decimal):
    result = 0
    quotient = 0
    remainder = 0
    binary = []
    if decimal >= 16:
        while decimal > 0:
            quotient = (decimal) / 2
            remainder = round((float(decimal) / 2) - quotient)
            binary.append(int(remainder))
            decimal = quotient
        result = "".join(map(str,reversed(binary)))
        print(result)
        another()
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
    result = binary_values[decimal]
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
