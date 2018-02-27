hexadecimal_values = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9
    }

def get_result(values):
    result = []
    results = []
    count = 0
    power = len(values) - 1
    sum = 0
    values = map(int, values)
    for value in values:
        result = (value * 16)
        base_16 = 16**power
        result = value * base_16
        results.append(result)
        power -= 1
    for result in results:
        sum += result
    print sum
    another()

def another():
    answer = raw_input("Is there another hexadecimal you want to convert?\n")
    if answer == "Y":
        get_hexadecimal()
    elif answer == "N":
        exit()
    else:
        print ("Enter Y to enter another hexadecimal or N to exit.")
        another()


def get_hexadecimal():
    hexadecimal = raw_input("What hexadecimal do you want to convert?\n")
    values = []
    for letter in hexadecimal:
        values.append(hexadecimal_values[letter])
        if not letter:
            print ("Enter values only including the following:\n0123456789ABCDEF\nInput invalid.")
    values = map(int, values)
    get_result(values)          


if __name__=="__main__":
    get_hexadecimal()
