# Functions that do the calculations
import calc_functions as calc 
# Dictionary that holds our conversion codes
import function_dict as dict
# Package to add colors to outputs
from colorama import Fore, Back, Style, init
# We are going to use this to exit
import sys

# Welcome the user to the program and display a menus of the unit options for their temperature
def welcome_menu():
    print("\n------------Welcome to the temperature converter!------------\n\n")

# Handle input from the user to get the units they want to do their conversions on
def recv_input():
    while True:
        welcome_menu()
        try: 
            # Call the function that asks for the user's unit
            chosen_unit = calc.unit_selection()
        except ValueError:
            print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
            continue

        try:
            # Call the function that gets the unit that we are converting to
            convert_to_unit = calc.convert_to()
        except ValueError:
            print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
            continue
        # Handles the edge case if the user choses the same unit for converting to and converting from
        if chosen_unit == convert_to_unit:
            print(Back.RED + Fore.WHITE + "Error: Temperature units are the same, please choose different temperature units" + Style.RESET_ALL)
            continue
        
        # Get the numerical value of the temperature they are converting 
        try:
            temp_value = calc.temp_num()
        except ValueError:
            print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
            continue

        
        # combine the chosen unit and convert to unit so that we can get the appropriate function from the dictionary
        convert_dict_code = str(chosen_unit) + "," + str(convert_to_unit)

        # Call the corresponding function by using the .get() method on the switch dictionary
        print(dict.convert_dict.get(convert_dict_code)(temp_value))
        # Function asks the user if they would like to do another conversion
        another_conversion()

       

# Function that will ask user for additional conversions
def another_conversion():
     # Ask user if they would like to do additional conversions
        while True:
            print("\n Would you like to do another temperature conversion?\n")
            try:
                answer = int(input("\n1. Yes\n2. No\n>> "))
            except ValueError:
                print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
                continue
            try:
                if answer == 1:
                    break
                elif answer == 2:
                    sys.exit()
                elif answer != 1 or answer != 2: 
                    print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
                continue