
# The program will convert temperatures between Celsius, Kelvin, and Fahrenheit

# Welcome the user to the program and display a menus of the metric options for their temperature

def welcome_menu():
    print("\n------------Welcome to the temperature converter!------------\n\n")
   
    
# Prompt the user to choose which metric their temperature is in
def metric_selection():
    print("Please select the number corresponding to your temperature:\n")
    print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
    metric_choice = input(">> ")
    # Continue to execute until valid input is chosen
    while True:
        # If the user has chosen a valid vaalue, then return
        if ((metric_choice == "1") or (metric_choice == "2") or (metric_choice == "3")):
            return metric_choice
        # Else, continue executing the metric_selection function
        else:
            print("Please enter a valid selection\n\n\n")
            metric_choice = metric_selection()

# This function will chose what metric to convert to
def convert_to():
    print("What metric would you like to convert to?\n")
    print("1. Fahrenheit\n2. Celsius\n3. Kelvin\n")
    metric_convert_to = input(">> ")
     # Continue to execute until valid input is chosen
    while True:
        # If the user has chosen a valid vaalue, then return
        if ((metric_convert_to == "1") or (metric_convert_to == "2") or (metric_convert_to == "3")):
            return metric_convert_to
        # Else, continue executing the metric_selection function
        else:
            print("Please enter a valid selection\n\n\n")
            metric_convert_to = convert_to()

# Function converts temperature from fahrenheit to celsius
def fah_to_cel(fah_temp):
    cel_temp = (fah_temp - 32) * 5/9
    return round(cel_temp, 3)

# Function converts temperature from fahrenheit to Kelvin
def fah_to_kelvin(fah_temp):
    # Call fah_to_cell function because the formual for fahrenheit to kelvin is similar but it has an additional 273.15 degrees added
    kel_temp = fah_to_cel(fah_temp) + 273.15
    # Round to the nearst thousands place
    return round(kel_temp, 3)



# Function converts temperature from celsius to fahrenheit
def cel_to_fah(cel_temp):
    fah_temp = ((9/5) * cel_temp) + 32
    return round(fah_temp,3)

# Function converts from celsius to kelvin
def cel_to_kelvin(cel_temp):
    kelvin_temp = cel_temp + 273.15
    return round(kelvin_temp, 3)



# Function converts from kelvin to celsius
def kelvin_to_celsius(kelvin_temp):
    cel_temp = kelvin_temp - 273.15
    return round(cel_temp, 3)

# Function converts from kelvin to fahrenheit
def kelvin_to_fah(kelvin_temp):
    cel_temp = kelvin_to_celsius(kelvin_temp)
    fah_temp = cel_to_fah(cel_temp)
    return round(fah_temp, 3)


# def main():
#     welcome_menu()
#     chosen_metric = metric_selection()
#     convert_to_metric = convert_to()

#     print(f"chosen_metric: {chosen_metric}")
#     print(f"convert_to: {convert_to_metric}")


# main()

print(kelvin_to_fah(0))