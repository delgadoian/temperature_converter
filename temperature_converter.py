
""" 
TODO continue to refactor the code and add red highlights to the
error messages 

"""

import function_dict as dict
import calc_functions as calc

# The program will convert temperatures between Celsius, Kelvin, and Fahrenheit

# Welcome the user to the program and display a menus of the unit options for their temperature

def welcome_menu():
    print("\n------------Welcome to the temperature converter!------------\n\n")

def recv_input():
    while True:
        welcome_menu()
        chosen_unit = calc.unit_selection()
        convert_to_unit = calc.convert_to()
        if chosen_unit == convert_to_unit:
            print("Error: Temperature units are the same, please choose different temperature units\n")
            continue
        
        temp_value = calc.temp_num()
        # if we have invalid input for the temperature value
        if temp_value == -1:
            continue
        
        # combine the chosen unit and convert to unit so that we can get the appropriate function from the dictionary
        convert_dict_code = chosen_unit + "," + convert_to_unit

        # Call the corresponding function by using the .get() method on the switch dictionary
        print(dict.convert_dict.get(convert_dict_code)(int(temp_value)))

        # Ask user if they would like to do additional conversions
        print("\n Would you like to do another temperature conversion?\n")
        answer = int(input("\n1. Yes\n2. No\n"))
        if answer == 1:
            continue
        else:
            break




   
def main():
    recv_input()
       
        

main()

