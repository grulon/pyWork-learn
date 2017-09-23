# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:19:59 2017

@author: glrulon

How long until your birthday?

"""

import datetime

def print_header():
    print('-----------------------')
    print('     BIRTHDAY APP')
    print('-----------------------')
    print()
    

def get_birthday_from_user():
    print("Where were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    
    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_btwn_dates(original_date, target_date):
    this_year = (datetime.date(target_date.year, original_date.month, original_date.day))
    
    dt = this_year - target_date
    return dt.days 


def print_birthday_info(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is coming up in {} days!".format(days))
    else:
        print("TODAY IS YOUR BIRTHDAY!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_btwn_dates(bday, today)
    print_birthday_info(number_of_days)
    
    
main()

