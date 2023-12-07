'''
Currency Converter
@description: 
    This Python code provides a simple command-line tool to convert currencies using the forex_python library. 
    It parses arguments, validates currencies, handles errors, and prints the conversion result.
@program: currency_converter.py
@author: Gopinathan Munappy
@date: 12th December, 2023

Packages used:
    pip install forex-python
    pip install requests 

How to run or Usage:
    python currency_converter.py <[amount]> <BASE> to <DESTINATION>
example:
    python currency-converter.py 1.5 USD to GBP

'''
# Imports:
# from forex_python.converter import CurrencyRates, CurrencyCodes - Imports modules needed for currency conversion and codes.
# from requests.exceptions import ConnectionError - Imports exception handling for connection errors.
# from sys import argv - Imports the sys module and retrieves command-line arguments.

from forex_python.converter import CurrencyRates, CurrencyCodes
from requests.exceptions import ConnectionError
from sys import argv

# Initialize objects:
converter = CurrencyRates()  # Creates a currency converter object.
codes = CurrencyCodes()      # Creates a currency codes object.

# Define function parse_arguments
def parse_arguments():
    """
    This function parses the command-line arguments.
    It checks if the first argument is a number and parses it as a float if present.
    It verifies if the correct syntax is used: program_name <amount> <base> to <destination>.
    If the syntax is incorrect or information is missing, it raises an exception.
    Otherwise, it returns the amount, base currency, and destination currency as uppercase strings.
    """
    amount = 1
    try:
        amount = float(argv[1])
        del argv[1]

    except ValueError:
        #no amount entered
        #default amount
        pass

    #argv:
    #[0] - program name
    #[1] - SRC
    #[2] - 'to'
    #[3] - DST
    if len(argv) != 4 or argv[2] != 'to':
        raise Exception

    return amount, argv[1].upper(), argv[3].upper()


# Main function:
# parse arguments
# usage = '[<amount>] <BASE> to <DESTINATION>' - Defines usage information for the program.
def main():
    """
    Retrieves the symbol for the base and destination currencies using the codes object.
    Checks if the currencies are valid. If not, it raises an exception.
    Uses the converter object to convert the amount from the base currency to the destination currency.
    Rounds the result to three decimal places.
    Prints the conversion result with the corresponding symbols.
    """
    usage = '[<amount>] <BASE> to <DESTINATION>'
    try:
        amount, base, dest = parse_arguments()  # Tries to parse arguments using the parse_arguments function.
        # If an exception is raised, it prints the usage information and exits the program.
    except:                                     # Catches exceptions and prints an error message.
        print('usage:')
        print(usage)
        exit(1)

    # Convert currency:
    try:
 
        base_symbol = codes.get_symbol(base)      
                                            
        dest_symbol = codes.get_symbol(dest)

        #validate currencies
        if base_symbol is None:
            raise Exception(f'Currency {base} is invalid')
        if dest_symbol is None:
            raise Exception(f'Currency {dest} is invalid')

        result = converter.convert(base_cur=base, dest_cur=dest, amount=amount)
        result = round(result, 3)

        print(f'{amount}{base_symbol} equals to {result}{dest_symbol}')

    except ConnectionError as e:    # Catches connection errors and prints a message.
        print('Connection error')
        exit(1)                     

    except Exception as e:          # Catches other exceptions and prints the error message.
        print(e.args[0])
        exit(1)

if __name__ == "__main__":
    main()
    
# End of the program




