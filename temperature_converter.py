
""" 
TODO continue to refactor the code and add red highlights to the
error messages 

"""

import function_dict as dict
import calc_functions as calc

# Package used for highlighting error messages
from colorama import Fore, Back, Style, init

# The program will convert temperatures between Celsius, Kelvin, and Fahrenheit

# Welcome the user to the program and display a menus of the unit options for their temperature

def welcome_menu():
    print("\n------------Welcome to the temperature converter!------------\n\n")

# # Ask the user if they would like to make another temperature conversion
# def another_conversion():


def recv_input():
    while True:
        global outer_flag 
        welcome_menu()
        chosen_unit = calc.unit_selection()
        convert_to_unit = calc.convert_to()
        if chosen_unit == convert_to_unit:
            print(Back.RED + Fore.WHITE + "Error: Temperature units are the same, please choose different temperature units" + Style.RESET_ALL)
            continue
        
        temp_value = calc.temp_num()
        
        # combine the chosen unit and convert to unit so that we can get the appropriate function from the dictionary
        convert_dict_code = str(chosen_unit) + "," + str(convert_to_unit)

        # Call the corresponding function by using the .get() method on the switch dictionary
        print(dict.convert_dict.get(convert_dict_code)(int(temp_value)))

        # Ask user if they would like to do additional conversions
        while True:
            print("\n Would you like to do another temperature conversion?\n")
            answer = int(input("\n1. Yes\n2. No\n"))
            if answer == 1:
                outer_flag = True
                break
            elif answer == 2:
                break
            elif answer != 1 or answer != 2: 
                print(Back.RED + Fore.WHITE + "Invalid selection, please try again" + Style.RESET_ALL)
                continue
            if outer_flag == True:
                continue




   
def main():
    recv_input()
       
        

main()

