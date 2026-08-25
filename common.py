from math import e
import pandas as pd
import datetime as dt

# depreciation function 
def monthly_depreciation(amount,rate):
    return amount * rate * 1/12
def Yearly_depreciation(amount,rate,month):
    return amount*rate*month/12


#calculating the rate constant
def Constant(life):
    return (1200/life)/100

#user input 
def Get_amount():
    while True :
        try :
            amount = float(input("Please enter the amount: "))

            if amount > 0 :
                break
        except ValueError:
            pass

        print("Invalid input plz try again \n ")
    return amount

#life cycle
def get_life():
    while True :
        try :
            life = int(input("Please enter the life cycle of the asset in months: "))

            if life > 0 :
                break
        except ValueError:
            pass

        print("Invalid input plz try again \n ")
    return life
#Entry date & quiting date 

def Entery():
    while True:
        user_input = input("Please provide the usage date for the asset (Y.M.D): ").strip()
        try:
            Entry_Date = dt.datetime.strptime(user_input, "%Y.%m.%d")
            break
        except ValueError:
            print("Invalid format. Please use: year.month.day (e.g., 2026.06.08) \n")
    return Entry_Date

def Retiring(entry_Date):
    while True:
        user_input = input("Please provide the retiring date for the asset (Y.M.D): ").strip()
        try:
            Retiring_Date = dt.datetime.strptime(user_input, "%Y.%m.%d")
            if Retiring_Date < entry_Date :
                print("Note the retiring date should be ahead of purchase date , please rewrite the correct date. \n ")
            else :
                break
        except ValueError:
            print("Invalid format. Please use: year.month.day (e.g., 2026.06.08) \n")
    return Retiring_Date



#calculating life cycle

def life_cycle(Entry_Date,Retiring_Date,life):
    date_diff= (Retiring_Date.year - Entry_Date.year)*12 + (Retiring_Date.month - Entry_Date.month)+1
    if date_diff > life :
        life_cycle = life
    else :
        life_cycle = date_diff
    return life_cycle

def rate(life,Constant_rate) :
    if life > 72 :
        return Constant_rate*3
    if life >=60 :
        return Constant_rate*2
    if life >=36 :
        return Constant_rate*1.5
