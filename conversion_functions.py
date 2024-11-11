# Function converts temperature from fahrenheit to celsius
def fah_to_cel(fah_temp):
    cel_temp = (fah_temp - 32) * 5/9
    return str(round(cel_temp, 3)) + chr(176) + "C"

# Function converts temperature from fahrenheit to Kelvin
def fah_to_kelvin(fah_temp):
    # Call fah_to_cell function because the formual for fahrenheit to kelvin is similar but it has an additional 273.15 degrees added
    kel_temp = ((fah_temp - 32) * (5/9)) + 273.15
    # Round to the nearst thousands place
    return str(round(kel_temp, 3)) + chr(176) + "K"



# Function converts temperature from celsius to fahrenheit
def cel_to_fah(cel_temp):
    fah_temp = ((9/5) * cel_temp) + 32
    return str(round(fah_temp,3)) + chr(176) + "F"


# Function converts from celsius to kelvin
def cel_to_kelvin(cel_temp):
    kelvin_temp = cel_temp + 273.15
    return str(round(kelvin_temp, 3)) + chr(176) + "K"



# Function converts from kelvin to celsius
def kelvin_to_celsius(kelvin_temp):
    cel_temp = kelvin_temp - 273.15
    return str(round(cel_temp, 3)) + chr(176) + "C"

# Function converts from kelvin to fahrenheit
def kelvin_to_fah(kelvin_temp):
    cel_temp = kelvin_to_celsius(kelvin_temp)
    fah_temp = cel_to_fah(cel_temp)
    return str(round(fah_temp, 3)) + chr(176) + "F"
