import math
from colorama import Fore, Style

def find_century_code(year):
    if year >= 1500 and year <= 1599:
        century_code = 0
    elif year >= 1600 and year <= 1699:
        century_code = 6
    elif year >= 1700 and year <= 1799:
        century_code = 4
    elif year >= 1800 and year <= 1899:
        century_code = 2
    elif year >= 1900 and year <= 1999:
        century_code = 0
    elif year >= 2000 and year <= 2099:
        century_code = 6
    elif year >= 2200 and year <= 2299:
        century_code = 4
    else:
        print("Year Is Out Of Range, Sorry")
        return None
    return century_code

def find_month_code(month):
    month_codes = {
        "January": 0, "February": 3, "March": 3, "April": 6, "May": 1, "June": 4,
        "July": 6, "August": 2, "September": 5, "October": 0, "November": 3, "December": 5
    }
    return month_codes.get(month, None)

def find_day_code(day):
    day_codes = {
        "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6
    }
    return day_codes.get(day, None)

def main():
    print(Fore.CYAN + Style.BRIGHT + "THIS PROGRAM WILL FIND THE DAY OF YOUR BIRTHDAY" + Style.RESET_ALL)

    dob = input("Enter Your Date Of Birth In DD/MM/YYYY Format: ")
    day, month, year = map(int, dob.split('/'))

    if month < 1 or month > 12 or day < 1 or day > 31 or year < 1500 or year > 2299:
        print("Invalid input or calculation error.")
        return
    
    century = year // 100
    year_within_century = year % 100

    century_code = find_century_code(century * 100)
    month_name = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ][month - 1]
    month_code = find_month_code(month_name)
    
    if century_code is None or month_code is None:
        print("Invalid input or calculation error.")
        return
    
    day_code = (day + month_code + year_within_century + year_within_century // 4 + century_code) % 7
    
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    birth_day = day_names[day_code]
    
    print(f"Your birth day is: {birth_day}")

if __name__ == "__main__":
    main()
    
