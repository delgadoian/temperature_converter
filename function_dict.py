# Import the conversion functions
import conversion_functions as con_func

# Dictionary that will hold the different options of conversion, we will use this when we ask 
# the user what unit they are in and what unit they would like to convert to

convert_dict = {
    "1,2": con_func.fah_to_cel,
    "1,3": con_func.fah_to_cel,
    "2,1": con_func.cel_to_fah,
    "2,3": con_func.cel_to_kelvin,
    "3,1": con_func.kelvin_to_fah,
    "3,2": con_func.kelvin_to_celsius
}