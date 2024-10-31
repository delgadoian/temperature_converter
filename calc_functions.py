# Package used for highlighting error messages
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


# Prompt the user to choose which unit their temperature is in
def unit_selection():
    print("Please select the number corresponding to your temperature:\n")
    print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
    unit_choice = input(">> ")
    # Continue to execute until valid input is chosen
    while True:
        # If the user has chosen a valid vaalue, then return
        if ((unit_choice == "1") or (unit_choice == "2") or (unit_choice == "3")):
            return unit_choice
        # Else, continue executing the unit_selection function
        else:
            print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection\n\n\n")
            unit_choice = unit_selection()

# This function will chose what unit to convert to
def convert_to():
    print("What unit would you like to convert to?\n")
    print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
    unit_convert_to = input(">> ")
     # Continue to execute until valid input is chosen
    while True:
        # If the user has chosen a valid vaalue, then return
        if ((unit_convert_to == "1") or (unit_convert_to == "2") or (unit_convert_to == "3")):
            return unit_convert_to
        # Else, continue executing the unit_selection function
        else:
            print("Please enter a valid selection\n\n\n")
            unit_convert_to = convert_to()

# This function will collect the numerical value of the temperature we are converting to
def temp_num():
    while True:
        try:
            num = float(input("How many degrees is your temperature? (Enter a numerical value) >> "))
            return num
        except ValueError:
            print("Please enter a numerical value for temperature\n")
            return -1