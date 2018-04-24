import math

def calculate_energy_of_light():
    planck_constant_answer = input("Enter 1 to use Joules to the second: 6.626070040(81) x 10^−34\nEnter 2 to use Electronvolt to the second: 4.135667662(25) x 10^−15\nEnter 3 to use Planck Energy: 2 pi \nEnter 4 to enter the value:\n")
    if planck_constant_answer == 1:
        planck_constant = float(6.626070040 * 81) * float(10**-34)
    elif planck_constant_answer == 2:
        planck_constant = float(4.135667662 * 25) * float(10**-15)
    elif planck_constant_answer == 3:
        planck_constant = math.pi * 2
    elif planck_constant_answer == 4:
        planck_constant = input("Enter Planck's constant per second: \n")
        
    frequency = input("Enter the frequency of light in hertz: \n")
    result = float(planck_constant) * float(frequency)
    print("The energy of a light photo is: " + str(result))
    again()

def calculate_frequency():
    speed_of_light_answer = input("Enter 1 to use 299792458 meters per a second as the speed of light.\nEnter 2 to input the speed of light meters per a second.\n")
    if speed_of_light_answer == 1:
        speed_of_light = 299792458
    elif speed_of_light_answer == 2:
        speed_of_light = input("Enter the speed of light:\n")
    wavelength = input("Enter the wavelength in meters:\n")
    result = float(speed_of_light) / float(wavelength)
    print("The frequency of light in hertz is: " + str(result))
    again()

def calculate_plancks_constant_freq():
    energy_of_light_photon = input("Enter the energy of light photon:\n")
    frequency = input("Enter the frequency of light in hertz:\n")
    result = float(energy_of_light_photon) / float(frequency)
    print("Planck's constant per second is:  " + str(result))
    again()    

def calculate_plancks_constant_light():
    energy_of_light_photon = input("Enter the energy of the light photon: \n")
    wavelength_of_light = input("Enter the wavelength of light in meters: \n")
    speed_of_light_answer = input("Enter 1 to use 299792458 meters per a second as the speed of light.\nEnter 2 to input the speed of light meters per a second.\n")
    if speed_of_light_answer == 1:
        speed_of_light = 299792458
    elif speed_of_light_answer == 2:
        speed_of_light = input("Enter the speed of light:\n")
    result = float(energy_of_light_photon * ( wavelength_of_light / speed_of_light))
    print("Planck's constant per a second is:  " + str(result))
    again()        

def again():
    again = raw_input("Is there another problem you would like to solve?\nEnter 1 for Yes or 2 for No.\n")
    if again == "1":
        main()
    else:
        exit()
def main():
    answer = raw_input("What would you like to calculate?\nEnter 1 for Energy of a light photon.\nEnter 2 for Frequency.\nEnter 3 for Planck's Constant with known frequency\nEnter 4 for Planck's Constant by wavelength and speed of light.\n")
    if answer == "1":
        calculate_energy_of_light()
    elif answer == "2":
        calculate_frequency()
    elif answer == "3":
        calculate_plancks_constant_freq()
    elif answer == "4":
        calculate_plancks_constant_light()
    else:
        print("Enter a number within the range of 1 to 4 only.")
        main()  

if __name__=="__main__":
    main()
    
