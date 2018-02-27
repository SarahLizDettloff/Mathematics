import math


def get_buoyancy():
    volume = raw_input("What is the volume of the submerged object?\nEnter help if you need assistance to calculate the volume.\n")
    if volume == "help":
        get_volume()
    else:
        density = raw_input("What is the density of the fluid?\nIf using water enter 1 to accept the density of 1,000 kilograms/meters^3\n")
        if density == "1":
            density = int(1000)
        force = raw_input("What is the frce of gravity?\nIf using constant downward force which is 9.81 Newtons/kilogram then enter 1.\n")
        if force == "1":
            force = float(9.81)
        result = float(volume) * float(density) * float(force)
        print("The bouyancy is " + str(result) + " Newtons.")
        
    
def get_volume():
    shape = raw_input("Enter the number correlating with the shape you want to find the volume for:\n1.Cube\n2.Recetangular Prism\n3.Cylinder\n4.Regular Square Pyramid\n5.Cone\n6.Sphere\n")
    if shape == "1":
        length = int(raw_input("What is the length of one of the sides of the cube in meters?\n"))
        volume = float(length * length * length)
        print("The volume of a cube is " + str(volume) + "  meters^3\n")
        volume = float(volume) / 2
        print("The volume of a cube submerged is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    elif shape == "2":
        length = int(raw_input("What is the length of the rectangular prism in meters?\n"))
        width = int(raw_input("What is the width of the rectangular prism in meters?\n"))
        height = int(raw_input("What is the height of the rectangular prism in meters?\n"))
        volume = float(length * width * height)
        print("The volume of a rectangular prism is " + str(volume) + "  meters^3\n")
        volume = float(volume) / 2
        print("The volume of a rectangular prism submerged is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    elif shape == "3":
        diameter = int(raw_input("What is the diameter of the cylinder in meters?\n"))
        r = float(diameter / 2)
        height = int(raw_input("What is the height of the rectangular prism in meters?\n"))       
        volume = float(math.pi * r**2 * height)
        print("The volume of a cylinder is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    elif shape == "4":
        base = int(raw_input("What is the length of the base of the square pyramid in meters?\n"))
        base = float(base * base)
        height = int(raw_input("What is the height of the square pyramid in meters?\n"))
        stuff = float(1) / float(3)
        volume = float(base * height) * float(stuff)
        print("The volume of a regular square pyramid is " + str(volume) + " meters\n")
        volume = float(volume) / 2
        print("The volume of a regular square pyramid submerged is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    elif shape == "5":
        diameter = int(raw_input("What is the diameter of the cylinder in meters?\n"))
        r = float(diameter / 2)
        r = float(r * r)
        division = float(1) / float(3)
        height = int(raw_input("What is the height of the cone in meters?\n"))
        volume = float(division * (math.pi * r * height))
        print("The volume of a cone is " + str(volume) + "  meters^3\n")
        volume = float(volume) / 2
        print("The volume of a cone submerged is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    elif shape == "6":
        diameter = int(input("What is the diameter of the sphere in meters?\n"))
        r = float(diameter) / 2
        r = float(r**3)
        division = float(4) / float(3)
        volume = float(division) * r * float(math.pi)
        print("The volume of a sphere is " + str(volume) + "  meters^3\n")
        volume = float(volume) / 2
        print("The volume of a sphere submerged is " + str(volume) + "  meters^3\n")
        get_buoyancy()
    else:
        print("Enter one of the options by hitting the correlating number. Only 1 through 6.")
        get_volume()

if __name__ == "__main__":
    get_buoyancy()
