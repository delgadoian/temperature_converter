# Package used for highlighting error messages
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


# Prompt the user to choose which unit their temperature is in
def unit_selection():
    # Continue to execute until valid input is chosen
    while True:
        print("\nPlease select the number corresponding to your temperature:\n")
        print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
        try:
            unit_choice = int(input(">> "))
        except ValueError:
            print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection" + Style.RESET_ALL)
            continue

        try:
            # If the user has chosen a valid vaalue, then return
            if ((unit_choice == 1) or (unit_choice == 2) or (unit_choice == 3)):
                return unit_choice
            else:
                print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection" + Style.RESET_ALL)
                continue
        except ValueError:
            print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection\n" + Style.RESET_ALL)
            continue
        except OverflowError:
            print(Back.YELLOW + Fore.WHITE + "ERROR: please enter a smaller number\n" + Style.RESET_ALL)
            continue
            
            
            

# This function will chose what unit to convert to
def convert_to():
    while True:
        print("\nWhat unit would you like to convert to?\n")
        print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
        try:
            unit_convert_to = int(input(">> "))
        except ValueError:
            print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection" + Style.RESET_ALL)
            continue
        # Continue to execute until valid input is chosen
        try:
            # If the user has chosen a valid vaalue, then return
            if ((unit_convert_to == 1) or (unit_convert_to == 2) or (unit_convert_to == 3)):
                return unit_convert_to
            else:
                print(Back.RED + Fore.WHITE + "ERROR: please enter a valid selection" + Style.RESET_ALL)
                continue
        # Else, continue executing the unit_selection function
        except ValueError:
            print(Back.RED + Fore.WHITE + "Please enter a valid selection\n\n\n" + Style.RESET_ALL)
            continue
        except OverflowError:
            print(Back.YELLOW + Fore.WHITE + "ERROR: please enter a smaller number\n\n\n" + Style.RESET_ALL)
            

# This function will collect the numerical value of the temperature we are converting to
def temp_num():
    while True:
        try:
            num = float(input("How many degrees is your temperature? (Enter a numerical value) >> "))
            return num
        except ValueError:
            print(Back.RED + Fore.WHITE + "ERROR: please enter a numerical value for temperature" + Style.RESET_ALL)
            continue
            