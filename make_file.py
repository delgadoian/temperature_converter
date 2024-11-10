import os
import platform
import subprocess
import sys

# Package used for highlighting error messages
from colorama import Fore, Back, Style, init

# Clear the terminal
def clear_terminal():
    # If the operating system is windows, run the windows command to clear the screen
    if platform.system() == "Windows":
        os.system('cls')
    # Use the clear command on other os's, most likely UNIX based
    else:
        os.system("Clear")

# Run the temperature converter program
def run_temperature_converter():
    try:
        subprocess.run([sys.executable, "temperature_converter.py"], check=True)
    except subprocess.CalledProcessError as error:
        print(Back.RED + Fore.WHITE + f"An error occurred when running temperature_converter.py: {error}")
        sys.exit()
    except FileNotFoundError:
        print(Back.RED + Fore.WHITE + "Error: Could not find temperature_converter.py, please make sure the file is downloaded\n")
        sys.exit()

# Call the functions
def main():
    clear_terminal()
    run_temperature_converter()

main()