#!/usr/bin/ env python3
#pckg import
import sys
import os
import math
import time
from sys import platform
from datetime import datetime
#global variable declarations
y = ["Y", "y", "YES", "yes", "Yes", "1"]
n = ["N", "n", "NO", "no", "No", "0"]
percent = "%"
today = datetime.today()
date = today.strftime("\n%d/%m/%Y @ %H:%M:%S")
#global functions
def clear():
    if "linux" in sys.platform:
        os.system("clear")
    if "win32" in sys.platform:
        os.system("cls")
def exit():
    clear()
    sys.exit("Exiting...")
def loady(msg:int, times:int):
    clear()
    animation = "|/-\\"
    if str(msg) == "1":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Resetting... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "2":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Doing Maths... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "3":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Loading Module... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "4":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Logging... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "5":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Loading...  " + animation[i % len(animation)])
            sys.stdout.flush()
    clear()
#main function
def intro():
    loady(5, 15)
    c = 1
    while c > 0:
        print("""
Welcome to Quick Maths!\n
    1.) Percent Change Calculator.\n
    2.) Dollar Cost Averager.\n
    3.) Entry Maths.\n
    4.) Interest Calculator.\n
    0.) To Exit.\n\n
    X.) Log Tools.
        """)
        introSelection = input("Please select an option: ")
        if introSelection == "1":
            pChange()
            continue
        if introSelection == "2":
            dca()
            continue
        if introSelection == "3":
            eMath()
            continue
        if introSelection == "4":
            iMath()
            continue
        if introSelection.lower() == "x":
            logtools()
        if introSelection == "0":
            exit()
        else:
            clear()
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d.lower() in y:
                intro()
            else:
                exit()
#referenced functions
def pChange():
    loady(3, 10)
    func = "Percent Change Calculator"
    pcCurrent = float(input("Enter the current price: "))
    pcFinal = float(input("Enter the final price: "))
    pcChange = (pcCurrent - pcFinal) / pcCurrent
    pcFormat = "%.0f%%" % (-100 * pcChange)
    result = "Current Price: $" + str(pcCurrent) + "\nFinal Price: $" + str(pcFinal) + "\nPercent Change: " + pcFormat + "\n"
    clear()
    loady(2, 20)
    print(result)
    f = input("Do you want to log this output? (Y/N) ")
    if f.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady(4, 12)
        loady(1, 15)
    else:
        loady(1, 15)
        intro()
def dca():
    loady(3, 10)
    func = "Dollar Cost Average"
    dcaInput = [float(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dcaAverage = (sum(dcaInput) / len(dcaInput))
    values = "Values: $" + str(dcaInput)
    result = "Average: $" + str(dcaAverage) + "\n"
    loady(2, 20)
    print(values)
    print(result)
    f = input("Do you want to log this output? (Y/N) ")
    if f.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady(4, 12)
        loady(1, 15)
    else:
        loady(1, 15)
        intro()
def eMath():
    loady(3, 10)
    func = "Entry Maths"
    emTicker = str(input("Please enter the emTicker:\n: "))
    emEntry = [float(x) for x in input("Please enter the entry point. *add spaces for dca*\n$: ").split()]
    emEntry = (sum(emEntry) / len(emEntry))
    emVolume = float(input("Please enter number of " + emTicker.upper() + " purchased:\n#: "))
    clear()
    print("""How would you like to setup your trade?\n
    1.) 3:6
    2.) 6:12
    3.) Custom
    """)
    emTradeParams = int(input("Please select an option: "))
    clear()
    if emTradeParams == 1:
        emTake = (emEntry * 0.06) + emEntry
        emStop = emEntry - (emEntry * 0.03)
    elif emTradeParams == 2:
        emTake = (emEntry * 0.12) + emEntry
        emStop = emEntry - (emEntry * 0.06)
    elif emTradeParams == 3:
        emTake = float(input("Where will you sell?\n$: "))
        emStopIN = str(input("Do you want to set a stop loss?(Y/N)\n: "))
        if emStopIN in y:
            emStop  = input("Where do you want to set a stop? *for percent of postion add percent sign*\n$: ")
        if emStopIN in n:
            emStop = "NA"
    else:
        print("Not a valid option...")
        loady(1, 15)
        eMath()
    emPosition = emEntry * emVolume
    emProfit = (emTake - emEntry) * emVolume
    emFutPlus = emProfit + emPosition
    if emStop == "NA":
        emLoss = "NA"
    elif "%" in emStop:
        emStop = emStop.replace("%", "")
        emStop =  emEntry - ((int(emStop) / 100) * emEntry)
    emLoss = ((emEntry - emStop) * emVolume)
    emFutMinus = emPosition - emLoss
    result = "emTicker: " + str(emTicker.upper()) + "\n\nEntry: $" + str(emEntry) + "\nVolume: x" + str(emVolume) + "\nPosition: $" + str(emPosition) + "\nFuture Position: (+)$" + str(emFutPlus) + " | (-)$" + str(emFutMinus)+ "\n\nTake: $" + str(emTake) + "\nStop: $" + str(emStop) + "\n\nProfit: $" + str(emProfit) + "\nLoss: $" + str(emLoss) + "\n"
    loady(2, 20)
    print(result)
    f = input("Do you want to log this output? (Y/N) ")
    if f.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func  + "\n" + result)
        loady(4, 12)
        loady(1, 15)
    else:
        loady(1, 15)
        intro()
def iMath():
    loady(3, 10)
    func = "Interest Calculator"
    imRate = float(input("Please enter the interest rate:\n%: "))
    imVolume = float(input("Please enter borrowed amount:\n$: "))
    loady(2, 7)
    im3 = (imRate / 100) * imVolume
    result = "Interest Rate: " + str(imRate) + "%\n" + "Borrowed Amount: $" + str(imVolume) + "\n" +"Interest Expense: $" + str(im3) + "\n"
    print(result)
    f = input("Do you want to log this output? (Y/N) ")        
    if f.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady(4, 12)
        loady(1, 15)
    else:
        loady(1, 15)
        intro()
def logtools():
    loady(3,10)
    while True:
        print("""Log tools:\n
        1.) Read Log.
        2.) Reset Log.
        0.) Back
        """)
        a = input("How would you like to proceed?: ")
        if a == "1":
            clear()
            with open("trade.log", "r") as file:
                p = file.read()
                print(p)
            input("Press enter to continue...")
            logtools()
        if a == "2":
            clear()
            d = input("Are you sure you want to continue? This will reset the log file. (Y/N) ")
            if d.lower() in y:
                loady(1, 10)
                with open("trade.log", "w") as file:
                    p = file.write("")
                logtools()
            else:
                loady(1, 15)
                logtools()
        if a == "0":
            intro()
        else:
            clear()
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d.lower() in y:
                logtools()
            else:
                intro()
#main function call
def main():
    intro()
#dunder check
if __name__ == "__main__":
    main()