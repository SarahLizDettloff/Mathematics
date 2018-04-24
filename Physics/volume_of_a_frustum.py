def get_volume(height, lower_r, upper_r):
    volume = ((1/ float(3)) * height) * (float ((upper_r**2) + (upper_r*lower_r) + (lower_r**2)))
    print ("The volume of the frustum is: " + str(volume))

def main():
    height = input("What is the height of the frustum?:\n")
    lower_r = input("What is the width of the top of the frustum?:\n")
    upper_r = input("What is the length of the bottom of the frustum?:\n")
    get_volume(height, lower_r, upper_r)

if __name__ == "__main__":
    main()
