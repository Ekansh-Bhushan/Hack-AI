import re
from datetime import datetime, date
from random import choice as r_c
import mysql.connector as my
from tabulate import tabulate
from forex_python.converter import CurrencyRates
import time


print("""Connecting to the server...
Secure connection established.\n\n\n\n""")

mydb = my.connect(host='localhost', user='root', passwd='password', autocommit=True)
mycursor = mydb.cursor()
mycursor.execute("Create Database if not exists HackAI")
print("CHECKING AND CREATING DATABASE...")
mycursor.execute("use HackAI")
print("DATABASE CREATED AND CHECKED SUCCESSFULLY.\n\n\n\n\n\n\n")

SEED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_1234567890#"


# DEFINING FUNCTIONS


def random_id():
    buffer = ""
    for i in range(9):
        buffer += r_c(SEED)
    return buffer

def is_valid_username(username):
    # Username should contain only letters, numbers, underscores, or hyphens
    if re.match(r'^[a-zA-Z0-9_-]+$', username):
        return True
    else:
        print("Invalid username. It should contain only letters, numbers, underscores, or hyphens.")
        return False


def is_valid_password(password):
    # Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', password):
        return True
    else:
        print("Invalid password. It should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
        return False


def is_valid_email(email):
    # Basic email validation using a simple regular expression
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True
    else:
        print("Invalid email address. Please enter a valid email address.")
        return False


def get_dob():
    while True:
        date = input("Enter The dob (dd-mm-yyyy) : ")
        if is_validate_date(date):
            day, month, year = [int(field) for field in date.split("-")]
            try:
                date = datetime(year, month, day)
                if date > datetime.today():
                    raise ValueError
                return date
            except ValueError:
                print("The Date You Entered Doesn't Exists, Or it is grater than today. Try That Again...")
        else:
            print("Your Answer Might Not Be In The Mentioned Date Format, Try That Again...")


def main():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter an email address: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    if is_valid_username(username) and is_valid_password(password) and is_valid_email(email) and is_valid_dob(dob):
        print("Valid input.")
    else:
        print("Invalid input. Please check your details and try again.")

if __name__ == "__main__":
    main()

def currency_converter():
    c = CurrencyRates()
    
    base_currency = "EUR"  # Fixed base currency
    amount = float(input(f"Enter the amount in {base_currency}: "))

    print("Available foreign currencies:")
    foreign_currencies = input("Enter foreign currencies to convert to (comma-separated, e.g., USD,GBP): ").upper().split(',')

    converted_amounts = {}
    
    for foreign_currency in foreign_currencies:
        foreign_currency = foreign_currency.strip()
        if foreign_currency in c.get_rates(base_currency):
            converted_amount = c.convert(base_currency, foreign_currency, amount)
            converted_amounts[foreign_currency] = converted_amount
        else:
            print(f"Skipping invalid currency: {foreign_currency}")

    if converted_amounts:
        print(f"{amount} {base_currency} is equal to:")
        for foreign_currency, converted_amount in converted_amounts.items():
            print(f"{converted_amount:.2f} {foreign_currency}")
    else:
        print("No valid foreign currencies provided.")

if __name__ == "__main__":
    currency_converter()



def set_currency_thresholds():
    c = CurrencyRates()

    # Get the list of available foreign currencies
    base_currency = "EUR"  # Fixed base currency
    available_currencies = list(c.get_rates(base_currency).keys())

    # Initialize a dictionary to store currency thresholds
    currency_thresholds = {}

    # Allow the user to input thresholds for multiple foreign currencies
    print("Available foreign currencies:")
    for i, currency in enumerate(available_currencies):
        print(f"{i + 1}. {currency}")
    
    while True:
        try:
            currency_index = int(input("Enter the number corresponding to the currency (0 to finish): "))
            if currency_index == 0:
                break
            if currency_index < 1 or currency_index > len(available_currencies):
                print("Invalid choice. Please enter a valid number.")
                continue
            currency = available_currencies[currency_index - 1]
            threshold = float(input(f"Enter the threshold value for {currency}: "))
            currency_thresholds[currency] = threshold
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Poll exchange rates and send alerts
    while True:
        for currency, threshold in currency_thresholds.items():
            current_rate = c.get_rate(base_currency, currency)
            print(f"Current exchange rate for {currency}: {current_rate:.2f}")
            if current_rate > threshold:
                print(f"ALERT: Exchange rate for {currency} has surpassed the threshold of {threshold}")
        time.sleep(60)  # Poll every minute

if __name__ == "__main__":
    set_currency_thresholds()

'''This code defines three functions (is_valid_username, is_valid_password, and is_valid_email) to 
check the validity of the username, password, and email using regular expressions. 
The main function takes user input for these three fields and checks their validity. 
If all fields are valid, it prints "Valid input." Otherwise, it prints "Invalid input."'''







# def is_valid_gender(gender):
#     accepted_genders = ['male', 'female', 'others']
#     return gender in accepted_genders


# def get_gender():
#     while True:
#         gender = input('Enter the gender (Male,Female,Others)  :  ').lower()
#         if is_valid_gender(gender):
#             return gender
#         else:
#             print('The Gender Is Not Valid.')



#----------------------------------------------------------i checked till here as of now ------------------------------

