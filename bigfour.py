def displacement_with_acceleration():
    initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
    time = float(raw_input("Enter the time in seconds: \n"))
    acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
    result = (float(initial_velocity) * float(time) + float(0.5) * float(acceleration) * float(time**2))
    print("The displacement with acceleration is: " + str(result) + "m \n")
    another()


def final_velocity():
    initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
    time = float(raw_input("Enter the time in seconds: \n"))
    acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
    result = (float(initial_velocity) + (float(time) * float(acceleration)))
    print("The final velocity is: " + str(result) + "m \n")    
    another()

def displacement_without_acceleration():
    initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
    time = float(raw_input("Enter the time in seconds: \n"))
    final_velocity = float(raw_input("Enter the final velocity of the object in m/s: \n"))
    result = (((float(initial_velocity) * float(final_velocity)) / 2) * float(time))
    print("The displacement is: " + str(result) + "m \n")    
    another()

def final_velocity_squared():
    acceleration = float(raw_input("Enter the acceleration in m/s^2:\n"))
    initial_velocity = float(raw_input("Enter the inital velocity of the object in m/s: \n"))
    displacement = float(raw_input("Enter the displacement in m:\n"))
    result = float(float(initial_velocity * 2) + (2 * float(acceleration) * float(displacement)))
    print("The final velocity squared is: " + str(result) + "m \n")    
    another()

def another():
    answer = raw_input("Would you like to solve another equation? Enter Y for yes or N for no\n")
    if answer == "Y":
        which_equation()
    else:
        exit()

def which_equation():
    answer = raw_input("Enter the number of the kinematic equation you want to solve:\n1.Displacement with known acceleration.\n2.Displacement without known acceleration.\n3.Final Velocity.\n4.Final Velocity Squared.\n")
    if answer == "1":
        displacement_with_acceleration()
    elif answer == "2":
        displacement_without_acceleration()
    elif answer == "3":
        final_velocity()
    elif answer == "4":
        final_velocity_squared()
    else:
        print("This will only accept an input of 1, 2, 3, or 4.")
        which_equation()


if __name__ == "__main__":
    which_equation()
