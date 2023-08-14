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

def find_month_code(month) :
    if month == "January" :
        month_code = 0
    elif month =="February":
        month_code = 3
    elif month == "March" :
        month_code = 3
    elif month == "April" :
        month_code = 6
    elif month == "May" :
        month_code = 1
    elif month == "June":
        month_code = 4
    elif month == "July" :
        month_code = 6
    elif month == "August":
        month_code = 2
    elif month == "September":
        month_code = 5
    elif month == "October" :
        month_code = 0
    elif month == "November " :
        month_code = 3
    elif month_code == "December " :
        month_code = 5
    else :
        print(f"Enter A Valid Month")
    return month_code

def find_day_code(day) :
    if day == "Sunday" :
        day_code = 0
    elif day == "Monday" :
        day_code = 1
    elif day == "Tuesday" :
        day_code = 2
    elif day == "Wednesday" :
        day_code = 3
    elif day == "Thursday " :
        day_code = 4
    elif day == "Friday " :
        day_code = 5
    elif day_code == "Saturday" :
        day_code = 6
    else:
        print(f"Enter A Valid Date" ) 
    return day_code

def main() :
    print(Fore.CYAN + Style.BRIGHT + f"THIS PROGRAM WILL FIND THE DAY OF YOUR BIRTHDAY" + Style.RESET_ALL)
    
    dob = input(f"Enter Your Date Of Birth In DD/MM/YYYY Format : ")




    