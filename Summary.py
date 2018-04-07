import math


class BinetsFibonacciNumber(object):
    """
    Simple calculator using Binet's Fibonacci formula will calculate for the n-th of a fibonacci number.
    The formula is Phi to the square root of n subtracted by negative Phi to the negative square root of n
    which is then divided by the square root of 5. Phi is the golden ratio which in this case is inputted into
    the seventh decimal place. The fibonacci sequence can be seen throughout nature from the petals in flowers,
    to pinecones, to seashells, to facial characteristics, to animals, to insects, and to sprial galaxies.
    """
    def __init__(self):
        self.calculate_fib()
        another_problem()

    def calculate_fib(self):
        """
        Gets the fib number
        Calculates the result of the fib to fibonacci
        """
        n = float(raw_input("Enter the value of Fib(n):\n"))
        phi_positive = float(1.6180339 ** n)
        phi_negative = -(float(1.6180339 ** -n))
        result = float((phi_positive - phi_negative) / float(math.sqrt(5)))
        print("The Fibonacci number for " + str(n) + " is " + str(result))


class VolumeFrustum(object):
    """
    This volume was first introduced in ancient Egyptian times.
    It is theorized to be the equation whic was used to originally build pyramids.
    """
    def __init__(self):
        self.get_volume()
        another_problem()

    def get_volume(self):
        height = input("What is the height of the frustum?:\n")
        lower_r = input("What is the width of the top of the frustum?:\n")
        upper_r = input("What is the length of the bottom of the frustum?:\n")
        volume = ((1 / float(3)) * height) * (float((upper_r ** 2) + (upper_r * lower_r) + (lower_r ** 2)))
        print ("The volume of the frustum is: " + str(volume))


class PlanckConstant(object):
    """
    Planck Constant is used as a foundational concept in quantum mechanics since it is the quantum of action
    in a phsyical constant. Max Planck developed this concept along with many others that resulted in him
    winning the Nobel Prize in 1918.
    """
    def __init__(self):
        self.which_planck()
        another_problem()

    def calculate_energy_of_light(self):
        """
        Calculates the energy of a light photon
        """
        planck_constant_answer = raw_input(
            "Enter 1 to use Joules to the second power: 6.626070040 (81)  x 10^-35\n"
            "Enter 2 to use Electronvolt to the second power: 4.135667662 (25)  x 10^-15\n"
            "Enter 3 to use Planck Energy: 2 pi \n"
            "Enter 4 to enter the value: \n")
        if planck_constant_answer == "1":
            planck_constant = float(6.626070040 * 81) * float(10 ** -34)
        elif planck_constant_answer == "2":
            planck_constant = float(4.135667662 * 25) * float(10 ** -15)
        elif planck_constant_answer == "3":
            planck_constant = math.pi * 2
        elif planck_constant_answer == "4":
            planck_constant = input("Enter Planck's constant per second: \n")

        frequency = input("Enter the frequency of light in hertz: \n")
        result = float(planck_constant) * float(frequency)
        print("The energy of a light photo is: " + str(result))

    def calculate_frequency(self):
        """
        Calculates the frequency.
        """
        speed_of_light_answer = input(
            "Enter 1 to use 299792458 meters per a second as the speed of light.\n"
            "Enter 2 to input the speed of light meters per a second.\n")
        if speed_of_light_answer == 1:
            speed_of_light = 299792458
        elif speed_of_light_answer == 2:
            speed_of_light = input("Enter the speed of light:\n")
        wavelength = input("Enter the wavelength in meters:\n")
        result = float(speed_of_light) / float(wavelength)
        print("The frequency of light in hertz is: " + str(result))

    def calculate_plancks_constant_freq(self):
        """
        Calculates Planck's Constant with known frequency
        """
        energy_of_light_photon = input("Enter the energy of light photon:\n")
        frequency = input("Enter the frequency of light in hertz:\n")
        result = float(energy_of_light_photon) / float(frequency)
        print("Planck's constant per second is:  " + str(result))

    def calculate_plancks_constant_light(self):
        """
        Calculates Planck's Constant by wavelength and speed of light
        """
        energy_of_light_photon = input("Enter the energy of the light photon: \n")
        wavelength_of_light = input("Enter the wavelength of light in meters: \n")
        speed_of_light_answer = input(
            "Enter 1 to use 299792458 meters per a second as the speed of light.\n"
            "Enter 2 to input the speed of light meters per a second.\n")
        if speed_of_light_answer == 1:
            speed_of_light = 299792458
        elif speed_of_light_answer == 2:
            speed_of_light = input("Enter the speed of light:\n")
        result = float(energy_of_light_photon * (wavelength_of_light / speed_of_light))
        print("Planck's constant per a second is:  " + str(result))

    def which_planck(self):
        answer = raw_input(
            "What would you like to calculate?\n"
            "Enter 1 for Energy of a light photon.\n"
            "Enter 2 for Frequency.\n"
            "Enter 3 for Planck's Constant with known frequency\n"
            "Enter 4 for Planck's Constant by wavelength and speed of light.\n")
        if answer == "1":
            self.calculate_energy_of_light()
        elif answer == "2":
            self.calculate_frequency()
        elif answer == "3":
            self.calculate_plancks_constant_freq()
        elif answer == "4":
            self.calculate_plancks_constant_light()
        else:
            print("Enter a number within the range of 1 to 4 only.")
            self.which_planck()


class Buoyancy(object):
    """
    This calculator contains a function to calculate the volume of six different shapes for you,
    finding the radius by diameter, and of course calculates the buoyancy force using the following equation:
    Fb = Vs x D x g
    """
    def __init__(self):
        self.get_buoyancy()
        another_problem()

    def find_volume(self):
        shape = raw_input(
            "Enter the number correlating with the shape you want to find the volume for:\n"
            "1.Cube\n"
            "2.Rectangular Prism\n"
            "3.Cylinder\n"
            "4.Regular Square Pyramid\n"
            "5.Cone\n"
            "6.Sphere\n")

        if shape == "1":
            """
            To find volume for a cube.
            """
            length = int(raw_input("What is the length of one of the sides of the cube in meters?\n"))
            volume = float(length * length * length)
            print("The volume of a cube is " + str(volume) + "  meters^3\n")
            volume = float(volume) / 2
            print("The volume of a cube submerged is " + str(volume) + "  meters^3\n")
        elif shape == "2":
            """
            To find volume for a rectangular prism.
            """
            length = int(raw_input("What is the length of the rectangular prism in meters?\n"))
            width = int(raw_input("What is the width of the rectangular prism in meters?\n"))
            height = int(raw_input("What is the height of the rectangular prism in meters?\n"))
            volume = float(length * width * height)
            print("The volume of a rectangular prism is " + str(volume) + "  meters^3\n")
            volume = float(volume) / 2
            print("The volume of a rectangular prism submerged is " + str(volume) + "  meters^3\n")
        elif shape == "3":
            """
            To find volume for a cylinder.
            """
            diameter = int(raw_input("What is the diameter of the cylinder in meters?\n"))
            r = float(diameter / 2)
            height = int(raw_input("What is the height of the rectangular prism in meters?\n"))
            volume = float(math.pi * r ** 2 * height)
            print("The volume of a cylinder is " + str(volume) + "  meters^3\n")
        elif shape == "4":
            """
            To find volume for a regular square pyramid.
            """
            base = int(raw_input("What is the length of the base of the square pyramid in meters?\n"))
            base = float(base * base)
            height = int(raw_input("What is the height of the square pyramid in meters?\n"))
            stuff = float(1) / float(3)
            volume = float(base * height) * float(stuff)
            print("The volume of a regular square pyramid is " + str(volume) + " meters\n")
            volume = float(volume) / 2
            print("The volume of a regular square pyramid submerged is " + str(volume) + "  meters^3\n")
        elif shape == "5":
            """
            To find volume for a cone.
            """
            diameter = int(raw_input("What is the diameter of the cylinder in meters?\n"))
            r = float(diameter / 2)
            r = float(r * r)
            division = float(1) / float(3)
            height = int(raw_input("What is the height of the cone in meters?\n"))
            volume = float(division * (math.pi * r * height))
            print("The volume of a cone is " + str(volume) + "  meters^3\n")
            volume = float(volume) / 2
            print("The volume of a cone submerged is " + str(volume) + "  meters^3\n")
        elif shape == "6":
            """
            To find volume for a sphere.
            """
            diameter = int(input("What is the diameter of the sphere in meters?\n"))
            r = float(diameter) / 2
            r = float(r ** 3)
            division = float(4) / float(3)
            volume = float(division) * r * float(math.pi)
            print("The volume of a sphere is " + str(volume) + "  meters^3\n")
            volume = float(volume) / 2
            print("The volume of a sphere submerged is " + str(volume) + "  meters^3\n")
        else:
            print("Enter one of the options by hitting the correlating number. Only 1 through 6.")

    def get_buoyancy(self):
        volume = raw_input(
            "What is the volume of the submerged object?\n"
            "Enter help if you need assistance to calculate the volume.\n")
        if volume == "help":
            self.find_volume()
        else:
            density = raw_input(
                "What is the density of the fluid?\n"
                "If using water enter 1 to accept the density of 1,000 kilograms/meters^3\n")
            if density == "1":
                density = int(1000)
            force = raw_input(
                "What is the force of gravity?\n"
                "If using constant downward force which is 9.81 Newtons/kilogram then enter 1.\n")
            if force == "1":
                force = float(9.81)
            result = float(volume) * float(density) * float(force)
            print("The bouyancy is " + str(result) + " Newtons.")


class BigFour(object):
    """
    The big four is a set of four equations which can be executed to find an unknown information about an object's
    motion. The kinematic equations are distributed in this application to execute the actual equation;
    however, in practical use the approach will be alerted to find the variable which is unknown. D is for displacement,
    A is for acceleration, T is for time, vi is for initial velocity, and vf is for final velocity.
    The four equations are:
    d = vi * t + 1/2 * a * t^2
    vf^2 = vi^2 + 2 * a * d
    vf = vi + a * t
    d = ((vi + vf) / 2 ) * 2
    """
    def __init__(self):
        self.which_equation()
        another_problem()

    def displacement_with_acceleration(self):
        initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
        time = float(raw_input("Enter the time in seconds: \n"))
        acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
        result = (float(initial_velocity) * float(time) + float(0.5) * float(acceleration) * float(time ** 2))
        print("The displacement with acceleration is: " + str(result) + "m \n")

    def final_velocity(self):
        initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
        time = float(raw_input("Enter the time in seconds: \n"))
        acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
        result = (float(initial_velocity) + (float(time) * float(acceleration)))
        print("The final velocity is: " + str(result) + "m \n")

    def displacement_without_acceleration(self):
        initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
        time = float(raw_input("Enter the time in seconds: \n"))
        final_velocity = float(raw_input("Enter the final velocity of the object in m/s: \n"))
        result = (((float(initial_velocity) * float(final_velocity)) / 2) * float(time))
        print("The displacement is: " + str(result) + "m \n")

    def final_velocity_squared(self):
        acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
        initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
        displacement = float(raw_input("Enter the displacement in m:\n"))
        result = float(float(initial_velocity * 2) + (2 * float(acceleration) * float(displacement)))
        print("The final velocity squared is: " + str(result) + "m \n")

    def which_equation(self):
        answer = raw_input(
            "Enter the number of the kinematic equation you want to solve:\n"
            "1.Displacement with known acceleration.\n"
            "2.Displacement without known acceleration.\n"
            "3.Final Velocity.\n"
            "4.Final Velocity Squared.\n")
        if answer == "1":
            self.displacement_with_acceleration()
        elif answer == "2":
            self.displacement_without_acceleration()
        elif answer == "3":
            self.final_velocity()
        elif answer == "4":
            self.final_velocity_squared()
        else:
            print("This will only accept an input of 1, 2, 3, or 4.")
            BigFour()


class DecimalBinary(object):
    """
    Binary is a two base number system which is the simplest numeric system.
    Each digit represents a bit, which is why it is preferred by many computer engineers.
    Binary has a rich history that affected minds such as the philosopher Francis Bacon to the mathematician
    George Boole.
    """
    binary_values = {
        1: "001",
        2: "0010",
        3: "0011",
        4: "0100",
        5: "0101",
        6: "0110",
        7: "0111",
        8: "1000",
        9: "1001",
        10: "1010",
        11: "1011",
        12: "1100",
        13: "1101",
        14: "1110",
        15: "1111"
    }

    def __init__(self):
        self.get_decimal()
        another_problem()

    def convert_to_binary(self, decimal):
        result = 0
        binary = []

        if decimal >= 16:
            while decimal > 0:
                quotient = decimal / 2
                remainder = round((float(decimal) / 2) - quotient)
                binary.append(int(remainder))
                decimal = quotient
            result = "".join(map(str, reversed(binary)))
        elif decimal <= 15:
            result = self.binary_values[decimal]
        elif decimal < 0:
            print("A negative number cannot be converted into a decimal.\n")
            self.get_decimal()
        elif decimal == 0:
            result = 0000

        print(result)

    def get_decimal(self):
        decimal = raw_input("What decimal do you want to convert to binary?\n")
        try:
            decimal = int(decimal)
            self.convert_to_binary(int(decimal))
        except ValueError:
            print("Input must be a numeric value.")
            DecimalBinary()


class HexadecimalDecimal(object):
    """
    Hexadecimal is also known as base 16 since it is a numeric system which contains 16 numbers.
    It has a rich history for being used in ancient times, as well as being an essential concept
     in computer science in modern times.
    """
    hexadecimal_values = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    def __init__(self):
        self.get_hexadecimal()
        another_problem()

    def get_result(self, values):
        results = []
        power = len(values) - 1
        sum = 0
        values = map(int, values)
        for value in values:
            base_16 = 16 ** power
            result = value * base_16
            results.append(result)
            power -= 1
        for result in results:
            sum += result
        print sum

    def get_hexadecimal(self):
        hexadecimal = raw_input("What hexadecimal do you want to convert?\n")
        values = []
        for letter in hexadecimal:
            values.append(self.hexadecimal_values[letter])
            if not letter:
                print ("Enter values only including the following:\n0123456789ABCDEF\nInput invalid.")
        values = map(int, values)
        self.get_result(values)


class Main(object):

    def __init__(self):
        self.get_answer()

    def get_answer(self):
        answer = raw_input("Enter the following number to choose what mathematics function you would like to preform.\n"
                           "1.Binet's Fibbonacci Number\n"
                           "2.Volume of a Frustum\n"
                           "3.Planck Constant\n"
                           "4.Buoyancy\n"
                           "5.The Big Four\n"
                           "6.Decimal to Binary\n"
                           "7.Hexadecimal to Decimal\n")
        if answer < "8":
            math_options = {
                "1": BinetsFibonacciNumber,
                "2": VolumeFrustum,
                "3": PlanckConstant,
                "4": Buoyancy,
                "5": BigFour,
                "6": DecimalBinary,
                "7": HexadecimalDecimal
            }
            math_options[answer]()
        else:
            print("Please enter a value between 1 and 7.\n")
            self.get_answer()


def another_problem():
    another = raw_input("Is there another problem you would like to solve?\nEnter 1 for Yes or 2 for No.\n")
    if another == "1":
        Main()
    else:
        exit()


if __name__ == "__main__":
    Main()
